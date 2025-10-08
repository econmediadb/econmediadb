# Literature on Famine

In order to analyse the adjusment mechanism to price disequilibria, three families of dynamic models have been used in the literature : error-correction models, dynamic stochastic general equilibrium models, and agent-based models.

## 1. Models for price adjustment during crisis

### 1.1. Error correction model and adjustments to disequilibria ( Ó Gráda, 2015 )

Ó Gráda (2015) uses the error corection model approach to test whether the reaction to emerging disequilibria was slower during a crisis than in normal times. He estimates the following simple representation of the error correction model (ECM) :

$$
\Delta \text{P}_{i,t} = a + b \Delta \text{P}_{A,t} + c \text{FAM1} + d \text{P}_{i,t-1} + e \text{P}_{A, t-1} + f \text{FAM2} + g \text{FAM3} + \text{u}'_{it}
$$
where 
$$
\text{FAM1} = \text{FAMDUM}.\Delta \text{P}_{A,t}  \\
\text{FAM2} = \text{FAMDUM}.\text{P}_{i,t-1}  \\
\text{FAM3} = \text{FAMDUM}.\text{P}_{A',t-1}  
$$

Here $`\text{P}`$ is the natural log of price, $`\text{A}`$ is Region A, and $i$ is any other region. Agents adjust $` \text{P}_{i,t} `$ from $` \text{P}_{i,t-1} `$, in response to changes in $` \text{P}_{A} `$ (with b measuring the short-run effect).

Changes to $` \text{P}_{i} `$ are caused by by shocks to $` \text{P}_{A} `$ with a long-run relation $` \text{P}_{i} = (e/d) P_A `$ (mistake? should this not be -(e/d) ?)

Main findings :

1. The author finds that the $b$ coefficients are all positive and the $d$ coefficients are all negative.
2. The spread of coefficient values is consistent with distance and communications - the closer the markets to each other , the bigger the coefficients - or the stronger the co-movements and the bigger the adjustments to disequilibria
3. The $c$s are mostly positive. There are stronger co-movements during the famine months. Most of the $f$s are negative indicating faster adjustment in crisis months. 
4. Reaction to wheat prices in 1709-10 was somewhat stronger than in 1693-94. 


### 1.2. Dynamic Stochastic General Equilibrium (DSGE) models

DSGE models build on the assumption of a representative agent operationg under rational expectations in a general equilibrium.

Over the past three decades economists have modified the basic DSGE model in order analyse crisis dynamics and price adjustment, mainly by introducing frictions and non-linearities.

Bernanke, Gertler, and Gilchrist (1999) use the financial aggregator which amplifies initial shocks, making a small economic downturn propagate into a credit crunch and a large recession. The external finance premium creates a wedge between the cost of internal and external funds, which widens during a crisis and affects firm investment and demand, slowing down price adjustment.

Gertler and Karadi (2011) introduce intermediary frictions and focus on a financial intermediary/banking sector subject to moral hazard or capital constraints. A financial shock causes intermediaries' net worth to fall, which in turn reduces their capacity to lend and amplifies the transmission of shocks to the real economy.

Since the financial crisis of 2008, DSGE models have been relying on occasionally binding constraints (or Zero Lower Bound) by incorporating non-linearities like a minimum regulatory capital requirement for banks or a collateral constraint for households (e.g., loan-to-value ratio). When the constraint binds (during a crisis), the dynamics change abruptly, often leading to a sharper price or output response (see for instance Gust et al., 2017). 

Another approach to modify the price adjustment mechanism has been to replace the standard Calvo pricing or the Rotemberg pricing by alternatives. 

For instance within the state-dependent price setting firms adjust prices based on how far their price is from the optimal level, which becomes more costly during a crisis. This introduces non-linearity into the New Keynesian Phillips Curve. In this setup firms respond more quickly to large disequilibrium, which can be relevant during a crisis.

Another approach is to introduce inflation-based adjustment costs. Here we introduce costs that depend not just on the level of price change, but also on the first difference of inflation ( $` \pi_t - \pi_{t-1} `$ ​). This generates more inflation persistence and helps the model fit empirical data, especially during periods of high volatility. In other words, costs arise from changes in the inflation rate, which better captures inertial or volatile price-setting in crisis.

Finally, by introducing Markov-Switching into a DSGE model, one allows key parameters (like expectation rules, monetary policy rule coefficients, or price-stickiness) to switch between regimes (e.g., "normal" vs. "crisis"). For price adjustment, this can model a shift from rational to adaptive expectations (simple learning) during the crisis regime, which slows down price adjustment. The transition probability between regimes is governed by a Markov process, capturing shifts in behavior or policy.


### 1.3. Heterogeneous Agent Models (HAM)

Kaplan et al. (2018) develops a quantitative HANK model to show that monetary policy's transmission mechanism works mostly through indirect general equilibrium effects on household income, not the direct intertemporal substitution channel of standard models. It highlights the importance of heterogeneous marginal propensities to consume (MPCs) and "hand-to-mouth" households.

Auclert et al. (2025) demonstrate that the size of the fiscal multiplier is significantly larger than in Representative Agent New Keynesian models, primarily because government spending generates income for constrained, high-MPC households.

Bilbiie (2020) provides an analytically tractable (simplified) HANK model. It clearly illustrates the mechanism of the "New Keynesian Cross" (the interaction between household heterogeneity and nominal rigidity) and shows how HANK models can address several puzzles of the RANK literature, such as the forward guidance puzzle, and generate amplification.



### 1.4. Agent-Based Models (ABM)

In the _market microstructure mechanism_, the Limit Order Book (LOB) Dynamics is a mechanism used in crisis ABMs. Agents (liquidity demanders, suppliers, and market makers) submit limit orders (to buy/sell at a specific price) and market orders (to trade immediately at the best available price). The transaction price is determined endogenously where supply and demand meet.

In this framework, a crisis is modeled as a shock that reduces market maker capacity (e.g., due to balance sheet constraints or increased risk) and increases liquidity demanders' need for immediacy (e.g., forced selling due to margin calls or redemptions). This micro-level imbalance — a lack of limit orders to absorb selling pressure — leads to cascades of falling prices and a sharp increase in the bid-ask spread (a measure of illiquidity), which is the emergent price adjustment during a crisis.

Price dynamics are influenced by the difference in the timing and urgency of trades between different agent types. During a crisis, liquidity demanders (forced sellers) exhibit greater immediacy and push prices down more aggressively than the slow-to-react liquidity suppliers or constrained market makers. 

In _macroeconomic ABMs_ there are several mechanims that are used.

The asymmetric price adjustment mechanism captures the observation that during the 2008 crisis, financially constrained firms often raised prices while healthy firms cut them. Firms with weak balance sheets (limited internal liquidity, high leverage) are modeled to find it optimal to raise prices to boost current cash flows, even at the cost of losing future market share. This is an attempt to avoid costly external financing or maintain liquidity. Conversely, financially stronger firms may cut prices to gain market share. This heterogeneity in response to a negative demand/financial shock results in an overall attenuation of deflationary pressure compared to standard models, where prices would simply fall.

The adaptive heuristics and social interaction assumtion, uses simplified heuristics (rules of thumb) instead of full optimization, and they learn or imitate the pricing strategies of other successful agents. During a crisis, this can introduce price stickiness or volatility. Firms are often modeled to choose one of a few discrete pricing strategies (e.g., lower, maintain, or raise price) based on their utility function, which includes both private (e.g., profit margin) and social features (e.g., observing neighbors' price changes). The fear of making a mistake or menu costs can lead to stickiness, where firms only adjust prices when the deviation from their target price (price misalignment) is sufficiently large, or when the economic outlook is extremely uncertain (crisis). 

## 2. Factors used for current famine detection

**Agricultural food production** is generally estimated by the formula seen below :
$$
\text{Production} = \text{Area Cropped} \times \text{Yield}
$$
which means that we have to quentify both changes in the area planted as well as crop yield.

Current methods of famine detection use the following variables (Brown, 2008) :
1. **socio-economic data** : employment demand, population fluxes, school attendance, food prices, terms of trade, food prices (for food security monitoring, decision support system)
2. **rainfall, precipitation** : 
   - verbal descriptions in historical chronicles (i.e. wine chronicles since winegrowing goes as far back as the year 1200); 
   - identify above-average rainfall; 
   - the standardized precipitation index (SPI) is based on the long-run precipitation record for a thirty year period. The long-term record isfitted to a probability distribution, which is then transformed into a normal distributionso that the mean SPI for the location and desired period is zero  
3. **climate** : reliance on agriculture as a primary source of both income and food often leads to vulnerability to seasonal and inter-annual climate variability that affects agricultural yields
   - [HISTALP](https://www.zamg.ac.at/histalp/) : Historical Instrumental Climatological Surface Time Series Of The Greater Alpine Region
   - [Euro-Climhist](https://www.euroclimhist.unibe.ch/index_eng.html) : Euro-Climhist makes weather and climate history data accessible with a user-friendly search, daily weather data as well as extreme events and long-term climate trends.
   - [ACRE](https://www.met-acre.org/) : Atmospheric Circulation Reconstructions over the Earth
4. **pests** : birds, insects, .... may impact agricultural production 
5. **vegetation data** :
6. **markets and trade** : 
   - farmers typically sell a portion of their crop in the market after harvest, save a portion for consumption, and purchase food from market as their own supplies diminish later in the year; this interaction tends to amplify the response of market prices to the production of low-cost, locally grown grains such as millet, because higher prices will yield larger rewards for those who have excess grain to sell, and cost more for those who have food deficits for large portions of the year
   - higher prices can cause food insecurity among the most vulnerable in a population even in times with adequate or even abundant food supplies (Sen, 1981) 
   - countries that rely on imported food from outside the region are vulnerable to regional scarcity, global pricing and exchange rate volatility
7. **crop production** :
8. **livestock** : 
   - sale of animals in the market is related far more to scarcity of fodder than to actual numbers on the ground
9. **health & sanitation, nutrition** : 
   - during times of stress, contaminated drinking water, poor environmental hygiene and poor health infrastructure lead to poor assimilation of the food consumed; 
   - a person cannot be said to be food secure without environmental hygiene, primary health care and clean drinking water security; 
   - increasing poverty tends to be associated with lower dietary diversity
   - lack of quantity (energy) and quality (micronutrients) in the diet, which often leads to a lack of appetite and concurrent weight loss
   - monitoring of food consumption patterns, particularly for mothers and children, is essential for understanding the underlying food security issues in a region (check historical public records)
   - eco-climatically coupled diseases (i.e. cholera, ...) that affect directly both the ability of an affected person to absorb available nutrients
   - measures to control the spread of cholera, such as a ban on the sale of meat, fish and vegetables in local markets to prevent the spread of the disease, can negatively affect the purchasing power of household
   - water borne diseases in areas experiencing flooding conditions
10. **water & sanitation** : 
   - shallow, hand dug wells that can dry up during times of severe drought
   - lack of clean portable water and poor sanitation can lead to frequent illness and large outbreaks of water-borne diseases such a Cholera
   - improvements in safe water supply, and in particular hygiene (including use of soap for hand-washing) could reduce the incidence of diarrhea and the number of deaths due to diarrhea by more than half
11. **population data, census** :
12. **drought** :
13. **infrastructure** :
14. **conflict/security** : populations in conflict zones are particularly vulnerable to food security due to
   - the restriction in movements of people and goods, 
   - increased likelihood of raiding and theft of basic food and livestock, and 
   - the inability of farming families to sow, tend and harvest their fields over the course of a season



## 3. Decisions and decision-makers

- community
- civil society
- government
- private sector
- international organisations
- donor

An important part of contingency planning process is scenario development. Scenarios are used in the planning process to identify possible response requirements for hazards of varying severity as an integrated part of food security early warning. The planning process itself can be an invaluable tool for building consensus between government, donors, and humanitarian organizations and for developing the relationships and understanding needed for effective emergency response.
Contingencies considered in the planning process :
- hurricanes/cyclones
- floods
- earthquakes
- droughts
- famine
- internal conflict
- war
- refugees
- economic collapse
- logistical bottlenecks
- internal displaced persons
- border closure
- epidemics
- volcanic eruptions
- tsunami
- landslides
- crop failure
- food aid pipeline breaks
- peace
- prepositioning

## Sources

### Famine

- Brown, Molly E. Famine early warning systems and remote sensing data. Berlin, Heidelberg: Springer Berlin Heidelberg, 2008.
- Boudreau, Tanya. The food economy approach: a framework for understanding rural livelihoods. London: Overseas Development Institute, 1998.
- Drèze, Jean, and Amartya Sen. Hunger and public action. Clarendon Press, 1990.
- Ó Gráda, Cormac. Eating people is wrong, and other essays on famine, its past, and its future. Princeton University Press, 2015.
- ó Gráda, Cormac. "Famine: a short history." (2021): 1-344.
- Sen, Amartya. "An essay on entitlement and deprivation." Poverty and Famines (1981).
- Verdin, James, et al. "Climate science and famine early warning." Philosophical Transactions of the Royal Society B: Biological Sciences 360.1463 (2005): 2155-2168.

### Economic Models

- Auclert, Adrien, Matthew Rognlie, and Ludwig Straub. "Fiscal and monetary policy with heterogeneous agents." Annual Review of Economics 17 (2025).
- Bilbiie, Florin O. "The new Keynesian cross." Journal of Monetary Economics 114 (2020): 90-108.
- Gust, Christopher, et al. "The empirical implications of the interest-rate lower bound." American Economic Review 107.7 (2017): 1971-2006.
- Kaplan, Greg, Benjamin Moll, and Giovanni L. Violante. "Monetary policy according to HANK." American Economic Review 108.3 (2018): 697-743.

