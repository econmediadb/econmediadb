import numpy as np
from random import uniform
import Tasmanian

def example_11():
    print("\n---------------------------------------------------------------------------------------------------\n")
    print("Example 11: Using unstructured data\n")

    iNumInputs = 2  # using two inputs for testing

    # test the error on a uniform dense grid with 10K points
    iTestGridSize = 100
    dx = np.linspace(-1.0, 1.0, iTestGridSize)  # sample on a uniform grid
    aMeshX, aMeshY = np.meshgrid(dx, dx)
    aTestPoints = np.column_stack([aMeshX.reshape((iTestGridSize**2, 1)),
                                   aMeshY.reshape((iTestGridSize**2, 1))])

    def get_error(grid, model, aTestPoints):
        aGridResult = grid.evaluateBatch(aTestPoints)
        aModelResult = np.empty((aTestPoints.shape[0], 1), np.float64)
        for i in range(aTestPoints.shape[0]):
            aModelResult[i, :] = model(aTestPoints[i, :])
        return np.max(np.abs(aModelResult[:, 0] - aGridResult[:, 0]))

    def model(aX):
        return np.ones((1,)) * np.exp(-aX[0]**2 - aX[1]**2)

    grid = Tasmanian.makeGlobalGrid(iNumInputs, 1, 4, "level", "clenshaw-curtis")

    # generate random data
    iNumData = 2000
    inputs = np.zeros((iNumData, iNumInputs))
    outputs = np.zeros((iNumData, 1))

    for i in range(iNumData):
        inputs[i, 0] = uniform(-1.0, 1.0)
        inputs[i, 1] = uniform(-1.0, 1.0)
        outputs[i, :] = model(inputs[i, :])

    # Remove the acceleration check. The code will always attempt to run.
    Tasmanian.loadUnstructuredDataL2(inputs, outputs, 1.E-4, grid)

    print("Using construction from unstructured (random) data")
    print("    approximatino error = {0:1.6E}".format(get_error(grid, model, aTestPoints)))
    print("  note: compared to the C++ code, this example does not fix the random seed")
    print("        the error will be slightly different every time you run the example")
    print("")

if (__name__ == "__main__"):
    example_11()