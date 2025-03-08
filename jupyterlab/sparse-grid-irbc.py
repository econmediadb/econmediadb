import numpy as np
import Tasmanian
from scipy import optimize
import matplotlib.pyplot as plt
import argparse
import copy

# fixing the argparse issue in Jupyter
import sys

# Type of IRBC model ({'smooth','non-smooth'})
typeIRBC = 'non-smooth'
# Type of numerical integration: ({'GH-quadrature','monomials_2d','monomials_power'})
typeInt = 'monomials_power'

# Number of countries
nCountries = 2
# Number of shocks (Country-specific shocks + aggregate shock)
nShocks = nCountries+1
# Number of policies (nCountries+1 for smooth IRBC, nCountries*2+1 for nonsmooth)
if typeIRBC=='non-smooth':
    nPols = nCountries*2+1
elif typeIRBC=='smooth':
    nPols = nCountries+1
else:
    print('Error in determining the type of IRBC')
    exit()

# Intertemporal elasticity of substitution
a_eis = 0.25
b_eis = 1.0
gamma = np.zeros(nCountries)
for j1 in range(nCountries):
    gamma[j1] = a_eis+j1*(b_eis-a_eis)/(nCountries-1)
# Discount factor
betta = 0.99
# Capital share of income
zeta = 0.36
# Depreciation rate
delta = 0.01
# Persistence of TFP shocks
rhoZ = 0.95
# Standard deviation of TFP shocks
sigE = 0.01
# Intensity of capital adjustment costs
kappa = 0.5
# Steady state for capital
k_ss = 1.0
# Aggregate productivity
A_tfp = (1.0-betta*(1.0-delta))/(zeta*betta)
# Welfare weight
pareto = A_tfp**(1.0/gamma)

# Lower bound for capital
kMin = 0.8
# Upper bound for capital
kMax = 1.2
# Lower bound for TFP
aMin = -0.8*sigE/(1.0-rhoZ)
# Upper bound for TFP
aMax = 0.8*sigE/(1.0-rhoZ)


# Iteration to start at (start from scratch -- numstart =0; restart: numstart >0)
numstart = 0
# Maximum number of iterations
maxiter = 300
# Iteration at which the refinement starts
iterRefStart = 25
# Convergence criterion in time iteration
tol_ti = 1e-4
# Number of random draws for the error computation
TT = 10000
# Number of burn-in periods for SIMULATION
burnin = 1000
# Location where data is stored
data_location_nonsmooth = "data/data_nonsmooth/"
data_location_smooth = "data/data_smooth/"
# Frequency of saving grid
savefreq = 10


if typeInt=='GH-quadrature':

    # Number of dimensions (One shock per country and the aggregate shock)
    int_dim = nCountries+1
    # Number of outputs
    int_out = 1
    # Level of integration grid (Number of points in each dimension; starts at 0)
    int_depth = 2
    # Tensor selection strategy
    int_type = "tensor"
    # Integration rule
    int_rule = "gauss-hermite"

    # Generate the grid structure
    int_grid = Tasmanian.makeGlobalGrid(int_dim, int_out, int_depth, int_type, int_rule)
    # Transform the nodes accordingly
    IntNodes = np.sqrt(2)*sigE*int_grid.getNeededPoints()
    # Get the corresponding quadrature weights
    IntWeights = int_grid.getQuadratureWeights()
    # Number of integration nodes
    numNodes = len(IntNodes)


elif typeInt=='monomials_2d':

    # Number of integration nodes
    numNodes = 2*nShocks
    # Pre-allocate nodes array
    z1 = np.zeros((numNodes,nShocks))
    # Fill nodes array with [1.0;-1.0]
    for i1 in range(nShocks):
        z1[i1*2,i1] = 1.0
        z1[i1*2+1,i1] = -1.0
    # Compute integration nodes
    IntNodes = z1*np.sqrt(nShocks)*sigE
    # Compute integration weights
    IntWeights = np.ones(numNodes)*1.0/numNodes

elif typeInt=='monomials_power':

    # Number of integration nodes
    numNodes = 2*nShocks**2 + 1

    z0 = np.zeros((numNodes,nShocks))

    # Deviations in one dimension (note that the origin is row zero)
    for i1 in range(nShocks):
        z0[i1*2+1,i1] = 1.0
        z0[i1*2+2,i1] = -1.0

    i0 = 0
    # Deviations in two dimensions
    for i1 in range(nShocks):
        for i2 in range(i1+1,nShocks):
            z0[2*nShocks+1+i0*4,i1] = 1.0
            z0[2*nShocks+2+i0*4,i1] = 1.0
            z0[2*nShocks+3+i0*4,i1] = -1.0
            z0[2*nShocks+4+i0*4,i1] = -1.0
            z0[2*nShocks+1+i0*4,i2] = 1.0
            z0[2*nShocks+2+i0*4,i2] = -1.0
            z0[2*nShocks+3+i0*4,i2] = 1.0
            z0[2*nShocks+4+i0*4,i2] = -1.0
            i0 += 1

    # Nodes
    IntNodes = np.zeros((numNodes,nShocks))
    IntNodes[1:nShocks*2+1,:] = z0[1:nShocks*2+1,:]*np.sqrt(2.0+nShocks)*sigE
    IntNodes[nShocks*2+1:] = z0[nShocks*2+1:]*np.sqrt((2.0+nShocks)/2.0)*sigE

    # Weights
    IntWeights = np.zeros(numNodes)

    IntWeights[0] = 2.0/(2.0+nShocks)
    IntWeights[1:nShocks*2+1] = (4-nShocks)/(2*(2+nShocks)**2)
    IntWeights[nShocks*2+1:] = 1.0/(nShocks+2)**2


else:

    print('Error in determining the type of numerical integration')
    exit()


################################################################################
#                           Production function                                #
################################################################################

def F(capital,sh):

    FF = A_tfp * np.exp(sh)*np.maximum(capital,1e-6)**zeta

    return FF


################################################################################
#                      Marginal product of capital                             #
################################################################################

def Fk(capital,sh):

    F_k =  A_tfp * zeta*np.exp(sh)*np.maximum(capital,1e-6)**(zeta-1.0)

    return F_k


################################################################################
#                          Capital adjustment cost                             #
################################################################################

def AdjCost(ktod,ktom):

    captod = np.maximum(ktod,1e-6)
    captom = np.maximum(ktom,1e-6)

    j = captom/captod - 1.0
    Adj_cost = 0.5 * kappa * j * j * captod

    return Adj_cost


################################################################################
#        Derivative of capital adjustment cost w.r.t today's cap stock         #
################################################################################

def AdjCost_k(ktod,ktom):

    captod = np.maximum(ktod,1e-6)
    captom = np.maximum(ktom,1e-6)

    j = captom/captod - 1.0
    j1 = captom/captod + 1.0
    AdjCostk = (-0.5)*kappa*j*j1

    return AdjCostk


################################################################################
#      Derivative of capital adjustment cost w.r.t tomorrows's cap stock       #
################################################################################

def AdjCost_ktom(ktod,ktom):

    captod = np.maximum(ktod,1e-6)
    captom = np.maximum(ktom,1e-6)

    j = captom/captod - 1.0
    AdjCostktom = kappa * j


    return AdjCostktom


################################################################################
#                  Residual of aggregate resource constraint                   #
################################################################################
    
# This function is used to compute an initial guess for the ARC multiplier
# It computes the residual of the aggregate resource constraint given a
# guess for lambda and a grid point

def ARC_zero(lam_gues,gridPt):
    
    res = 0.0
    
    for i1 in range(nCountries):
        res += np.exp(gridPt[nCountries+i1])*A_tfp*gridPt[i1]**zeta - (-delta*kappa/2.0)**2 - (lam_gues/pareto[i1])**(-gamma[i1])
    
    return res



################################################################################
#                               Grid construction                              #
################################################################################

# Number of dimensions (capital stock and tfp for each country)
gridDim = nCountries*2
# Number of outputs (capital policy & multiplier for each country + ARC multiplier)
gridOut = nPols
# Grid level (we start with a sparse grid of level 3)
gridDepth = 2
# 1=linear, 2=quadratic, 3=cubic
gridOrder = 1
# Type of base functions
gridRule = "localp"

# Set the grid domain to [kmin,kmax]^n x [amin,amax]^n
gridDomain = np.zeros((gridDim,2))

gridDomain[0:nCountries,0] = kMin
gridDomain[0:nCountries,1] = kMax
gridDomain[nCountries:,0] = aMin
gridDomain[nCountries:,1] = aMax

# Generate the grid structure
grid0 = Tasmanian.makeLocalPolynomialGrid(gridDim,gridOut,gridDepth,gridOrder,gridRule)
# Transform the domain
grid0.setDomainTransform(gridDomain)
# Get the points that require function values
aPoints = grid0.getPoints()
# Get the number of points that require function values
aNum = grid0.getNumPoints()



################################################################################
#                        Adaptivity parameters                                 #
################################################################################

# Surplus threshold
surplThreshold = 1e-3
# Number of maximum refinements
maxRef = 1
# Maximum Level of ASG
maxRefLevel = gridDepth + maxRef
# Outputs that are considered in the refinement process (-1 implies that all outputs are considered)
dimRef = -1
# Type of grid refinements
typeRefinement = 'classic'
# Scale correction in the refinement process:
# We only let the capital policies of each country determine the addition of grid points
scaleCorr = np.zeros(nPols)
scaleCorr[0:nCountries] = 1


################################################################################
#                             Initialization                                   #
################################################################################

# Our time iteration algorithm requires the initialization of policy functions,
# as these are necessary to interpolate for next period's policies. We make an
# educated guess here, assuming that capital choices are equal to the respective
# non-depreciated capital stock. This implies for the non-smooth model that the 
# irreversibility constraint is binding everywhere.

polGuess = np.zeros((aNum,nPols))

# Guesses for the capital policies and investment constraint multipliers:

for i0 in range(nCountries):
    polGuess[:,i0] = aPoints[:,i0]*(1.0-delta)

    if typeIRBC=='non-smooth':
        polGuess[:,nCountries+1+i0] = -delta*aPoints[:,i0]

# Guess for the aggregate ressource constraint multiplier:
#
# We use a nonlinear equation solver to find the ARC multipliers that are consistent
# with the guesses for the capital policies and investment constraint multipliers.

for i0 in range(aNum):
    root = optimize.root(ARC_zero, 0.1, method='lm', args=(aPoints[i0,:]))
    polGuess[i0,nCountries] = root.x
    # Print the status in case the solver did not find the root
    if root.success!= 1:
        print(root.message)


# Load function values into grid structure
grid0.loadNeededPoints(polGuess)



def ExpectFOC(ktemp, state, grid):

    # 1) Determine next period's tfp states

    newstate = np.zeros((numNodes,nCountries))

    for itfp in range(nCountries):
        newstate[:,itfp] = rhoZ*state[nCountries+itfp] + (IntNodes[:,itfp] + IntNodes[:,nShocks-1])
        newstate[:,itfp] = np.where(newstate[:,itfp] > aMin, newstate[:,itfp], aMin)
        newstate[:,itfp] = np.where(newstate[:,itfp] < aMax, newstate[:,itfp], aMax)

    # 2) Determine next period's state variables

    evalPt = np.zeros((numNodes,nCountries*2))

    evalPt[:,0:nCountries] = ktemp
    evalPt[:,nCountries:] = newstate


    # 3) Determine relevant variables within the expectations operator

    capPrPr = grid.evaluateBatch(evalPt)[:,0:nCountries]
    lambPr = grid.evaluateBatch(evalPt)[:,nCountries]

    if typeIRBC=='non-smooth':
        gzAlphaPr = grid.evaluateBatch(evalPt)[:,nCountries+1:]
        gzAplusPr = np.maximum(0.0,gzAlphaPr)

    # Compute tomorrow's marginal productivity of capital
    MPKtom = np.zeros((numNodes,nCountries))
    for impk in range(nCountries):
        MPKtom[:,impk] = 1.0 - delta + Fk(ktemp[impk],newstate[:,impk]) - AdjCost_k(ktemp[impk],capPrPr[:,impk])

    #Compute Density
    if typeInt=='GH-quadrature':
        density = np.pi**(-(nCountries+1) * 0.5)
    else:
        density = 1.0

    #Specify Integrand
    ExpectFOC = np.zeros((numNodes,nCountries))

    if typeIRBC=='non-smooth':

        for iexp in range(nCountries):
            ExpectFOC[:,iexp] = (MPKtom[:,iexp]*lambPr - (1.0-delta)*gzAplusPr[:,iexp]) * density

    else:

        for iexp in range(nCountries):
            ExpectFOC[:,iexp] = MPKtom[:,iexp]*lambPr * density


    return ExpectFOC


def sysOfEqs(x,state,grid):

    # State variables
    capStates = state[0:nCountries]
    tfpStates = state[nCountries:]

    # Policy values
    capPolicies = x[0:nCountries]
    lamb = x[nCountries]

    if typeIRBC=='non-smooth':

        gzAlphas = x[nCountries+1:]

        # Garcia-Zengwill transformation of the occasionally binding constraints
        gzAlphaPlus = np.maximum(0.0,gzAlphas)
        gzAlphaMinus = np.maximum(0.0,-gzAlphas)

    # Computation of integrands
    Integrands = ExpectFOC(capPolicies, state, grid)

    IntResult = np.empty(nCountries)

    for iint in range(nCountries):
        IntResult[iint] = np.dot(IntWeights,Integrands[:,iint])

    res = np.zeros(nPols)

    # Computation of residuals of the equilibrium system of equations

    if typeIRBC=='non-smooth':

        # Euler equations & GZ alphas
        for ires in range(nCountries):
            res[ires] = (betta*IntResult[ires] + gzAlphaPlus[ires])\
                            /(1.0 + AdjCost_ktom(capStates[ires],capPolicies[ires])) - lamb
            res[nCountries+1+ires] = capPolicies[ires] - capStates[ires]*(1.0-delta) - gzAlphaMinus[ires]

    else:

        # Euler equations
        for ires in range(nCountries):
            res[ires] = betta*IntResult[ires]/(1.0 + AdjCost_ktom(capStates[ires],capPolicies[ires])) - lamb


    # Aggregate resource constraint
    for ires2 in range(nCountries):
        res[nCountries] += F(capStates[ires2],tfpStates[ires2]) + (1.0-delta)*capStates[ires2] - capPolicies[ires2]\
                            - AdjCost(capStates[ires2],capPolicies[ires2]) - (lamb/pareto[ires2])**(-gamma[ires2])



    return res


################################################################################
#                           Time iteration step                                #
################################################################################

def ti_step(grid,pol_guess,gridZero):

    # Get the points that require function values
    aPoints1 = grid.getNeededPoints()
    # Get the number of points that require function values
    aNumAdd = grid.getNumNeeded()

    # Array for intermediate update step
    polInt = np.zeros((aNumAdd,nPols))

    # Time Iteration step
    for ii1 in range(aNumAdd):

        state = aPoints1[ii1]
        pol = pol_guess[ii1,:]
        root = optimize.root(sysOfEqs, pol, args=(state,gridZero), method='hybr')
        polInt[ii1,:] = root.x

    # Add the new function values to grid1
    grid.loadNeededPoints(polInt)


    return grid


################################################################################
#                             Grid refinement                                  #
################################################################################

def refine(grid):

    # Get the points that require function values
    aNumLoad = grid.getNumLoaded()
    # Scaling to only allow for those policies that are supposed to
    # determine the refinement process (in this case only the capital policies)
    scaleCorrMat = np.zeros((aNumLoad,nPols))
    scaleCorrMat[:,0:nPols+1] = scaleCorr

    # Refine the grid based on the surplus coefficients
    grid.setSurplusRefinement(surplThreshold, dimRef, typeRefinement, [], scaleCorrMat)

    if (grid.getNumNeeded()>0):

	    # Get the new points and the number of points
	    nwpts = grid.getNeededPoints()
	    aNumNew = grid.getNumNeeded()

	    # We assign (for now) function values through interpolation#
	    pol_guess = np.zeros((aNumNew,nPols))
	    pol_guess = grid.evaluateBatch(nwpts)

    else:

	    pol_guess = []


    return grid, pol_guess


################################################################################
#                        New grid construction                                 #
################################################################################

def fresh_grid():

    # Generate the grid structure
    grid = Tasmanian.makeLocalPolynomialGrid(gridDim,gridOut,gridDepth,gridOrder,gridRule)
    # Transform the domain
    grid.setDomainTransform(gridDomain)

    return grid



################################################################################
#                Checking convergence and updating policies                    #
################################################################################

def policy_update(gridOld,gridNew):

    # Get the points and the number of points from grid1
    aPoints2 = gridNew.getPoints()
    aNumTot = gridNew.getNumPoints()

    # Evaluate the grid points on both grid structures
    polGuessTr1 = gridNew.evaluateBatch(aPoints2)
    polGuessTr0 = gridOld.evaluateBatch(aPoints2)

    # 1) Compute the Sup-Norm

    metricAux = np.zeros(nPols)

    for imet in range(nPols):
        metricAux[imet] = np.amax(np.abs(polGuessTr0[:,imet]-polGuessTr1[:,imet]))

    metricSup = np.amax(metricAux)

    # 2) Compute the L2-Norm

    metricL2 = 0.0

    for imetL2 in range(nPols):
        metricL2 += np.sum((np.abs(polGuessTr0[:,imetL2]-polGuessTr1[:,imetL2]))**2)

    metricL2 = (metricL2/(aNumTot*nPols))**0.5

    metric = np.minimum(metricL2,metricSup)

    # Now update pol_guess and grid

    polGuess = np.zeros((aNumTot,nPols))

    for iupd in range(nPols):
        polGuess[:,iupd] = 0.5*polGuessTr0[:,iupd] + 0.5*polGuessTr1[:,iupd]

    gridOld = Tasmanian.copyGrid(gridNew)


    return metric, polGuess, gridOld



################################################################################
#                               Grid storage                                   #
################################################################################

def save_grid(grid,iter):

    if typeIRBC=='non-smooth':
        grid.write(data_location_nonsmooth + "grid_iter_" + str(iter+1) + ".txt")
    else:
        grid.write(data_location_smooth + "grid_iter_" + str(iter+1) + ".txt")


    return      
                                                                                                                            
                                                                                                                            
                                                                                                                            
# TeX Support for plots
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
                                                                                                                            
                                                                                                                            
# Parser settings for terminal calls
parser = argparse.ArgumentParser(description='Run the IRBC model.')
parser.add_argument('--final_grid', dest='load_flag', action='store_true', help='Postprocessing only')

# Parse with empty list or specific arguments
args = parser.parse_args([])  # For no arguments
# args = parser.parse_args(['--final_grid'])  # To enable the flag
                                                                                                                            
                                                                                                                            
#args = parser.parse_args()
load_flag = args.load_flag
                                                                                                                            
                                                                                                                            
# Replace with just the program name
sys.argv = [sys.argv[0]]


# Your parser code
parser = argparse.ArgumentParser(description='Run the IRBC model.')
parser.add_argument('--final_grid', dest='load_flag', action='store_true', help='Postprocessing only')

# Parse arguments
args = parser.parse_args()

# Now wrap your main code in a try-except to get better error information
try:
    # Your main code block here
    if args.load_flag:
        print('Postprocessing only.')
        # Construct the grid structure
        gridFinal = Tasmanian.TasmanianSparseGrid()
        # Read the properties from grid_final.txt
        gridFinal.read(data_location + "grid_final.txt")
        # Set as interpolation grid
        grid1 = Tasmanian.copyGrid(gridFinal)

    else:
    
        print('Start time iteration from iter = ', numstart)
    
        # If numstart==0 => start from scratch; numstart>0 => Restart from given iteration
    
        if (numstart>0):
    
            # Construct a new grid structure
            gridRestart = Tasmanian.TasmanianSparseGrid()
            # Read properties from file for restart
            gridRestart.read(data_location + "grid_iter_" + str(numstart) + ".txt")
            # Set as interpolation grid
            grid0 = Tasmanian.copyGrid(gridRestart)

        for iter0 in range(numstart,maxiter+1):
    
            polGuess1 = copy.copy(polGuess)
    
            grid1 = fresh_grid()
    
            # Index of current grid level to control the number of refinements
            ilev = gridDepth
    
            while ((grid1.getNumNeeded() > 0) and (ilev<=maxRefLevel)):
    
                grid1 = ti_step(grid1,polGuess1,grid0)
    
                # We start the refinement process after a given number of iterations
                if (iter0>iterRefStart):
                    grid1,polGuess1 = refine(grid1)
                    #grid1 = refine(grid1)
    
                # Track the grid level
                ilev += 1
    
            ## Calculate (approximate) errors on tomorrow's policy grid
            metric, polGuess, grid0 = policy_update(grid0,grid1)
    
            print("Iteration: %2d, Grid pts: %2d, Level: %2d, Metric: %.4E" % (iter0, grid0.getNumPoints(),ilev,metric))
    
            if (np.mod(iter0+1,savefreq)==0):
                save_grid(grid0,iter0)
    
            if (metric<tol_ti):
                break
    
        if typeIRBC=='non-smooth':
            grid1.write(data_location_nonsmooth + "grid_final.txt")
        else:
            grid1.write(data_location_smooth + "grid_final.txt")
    
        #error_sim = post.errors_sim(grid1)
        #errors_ss = post.errors_ss(grid1)


except Exception as e:
    print(f"Error occurred: {e}")
    import traceback
    traceback.print_exc()                                                                                                                        






















