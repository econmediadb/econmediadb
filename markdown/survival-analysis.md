# Survival Analysis

## Overview

1. Event-history data
2. Kaplan-Meier Estimator
3. Nelson-Aalen Estimator
4. Cox Proportional Hazard Models



## 1. Event-history data

We consider the case in which the data consists of observations on $N$ people each of whom passes through a sequence of discrete-states. Each person is first observed on entry to some initial state and his subsequent transitions are determined by a matrix of transition intensities of the form 

$\theta_{kl}(t,s)ds = P( A )$, $k, l = 1,2,\ldots, K. k \neq l$

where $A$ is the departure from $k$ to $l$ in $s, s+ ds$ given that it was entered at $t$ and has remained for $s$ and given the history of the process to $t+s$



## 2. Kaplan-Meier Estimator (non-parametric)

We consider the case of the estimation of a survivor function from a set of possibly right censored exit times. These times are to be thought of as independent realisations of a random variable $T$ with survivor function $\bar{F}(t)$.

Suppose we have $N$ uncensored times and let there be $M \leq N$ distinct exit times arranged in order of magnitude as $t_{(1)}, t_{(2)}, \ldots, t_{(M)}$. Thus we are allowing multiple exits at the same time. Let $n_j$ be the number of people leaving at $t_{(j)}$, where $n_1 + n_2 + \ldots + n_M = N$.

Now defining $\bar{F}(t) = P(T \geq t), t \geq 0$, we would naturally estimate a probability by a relative frequency and so estimate $\bar{F}(t)$ by the proportion of the $N$ people observed to leave at or after $t$, which is

$$\begin{aligned}
\hat{\bar{F}}(t)    &= 1 - \frac{ \text{number leaving before} \ \ t }{N} \\
                    &= 1-\frac{(n_1 + n_2 + \ldots + n_k)}{N}
\end{aligned}$$


where $k$ is the largest $j$ such that $t_{(j)} < t$.

For a homogeneous right censored data the survivor function at $t$ can be estimated by

$\hat{\bar{F}}(t) = \prod_{t_{(j)<t} } ( 1 - \hat{\theta}_j ), \hspace{1cm} t \leq 0$

for $\hat{\theta} = n_j/r_j $, where $n_j$ is the number of people observed to leave at $t_{(j)}$ and $r_j$ is the number of people in the risk set the instant before $t_{(j)}$. The subscript $j$ runs over the $M$ distinct times at which exits are observed.



## 3. Nelson-Aalen Estimator

The Nelson–Aalen estimator is a nonparametric estimator which may be used to estimate the cumulative hazard rate function from censored survival data.

Consider ﬁrst the survival data situation, where we want to study the time to death (or some other event) for a homogeneous population with hazard rate function $\alpha(t)$ and cumulative hazard rate function $A(t) = \int_0^t \alpha(s) ds$.

Assume that we have a sample of $n$ individuals from this population.

Our observation of the survival times for these individuals will typically be subject to right censoring, meaning that for some individuals we only know that their true survival times exceed certain censoring times.

We denote by $t_1 < t_2 < ldots $ the times when deaths are observed and let $d_j$ be the number of individuals who die at $t_j$.

The Nelson–Aalen estimator for the cumulative hazard rate function then takes the form

$$
 \hat{A}(t) = \sum_{t_j \leq t} \frac{d_j}{r_j}
$$

where $r_j$ is the number of individuals at risk just prior to time $t_j$ .



## 4. Cox Proportional Hazard Models

The Cox proportional hazards model is a frequently used approach that allows the investigator to study relationships between the time to event outcome $Y$ and a set of explanatory variables $X_1, X_2, \ldots, X_p$.

see [Julia code](../jupyterlab/survival-analysis.ipynb#Cox-proportional-hazards-regression-model)


## References

- Ibrahim, Joseph G., Ming-Hui Chen, Debajyoti Sinha, J. G. Ibrahim, and M. H. Chen. Bayesian survival analysis. Vol. 2. New York: Springer, 2001.
- Lancaster, Tony. The econometric analysis of transition data. No. 17. Cambridge university press, 1990.
- [Nelson–Aalen Estimator](http://www.medicine.mcgill.ca/epidemiology/hanley/c609/Material/NelsonAalenEstimator.pdf)
- [Nikulin, Mikhail., and Hong-Dar Isaac. Wu. The Cox Model and Its Applications. Berlin, Heidelberg: Springer Berlin Heidelberg, 2016. Web.](https://www.a-z.lu/discovery/fulldisplay?docid=alma9920996849707251&context=L&vid=352LUX_BNL:BIBNET_UNION&search_scope=DN_and_CI_UCV&tab=DiscoveryNetwork_UCV&lang=fr)
- [Getting started with the Julia library Survival.jl](https://juliastats.org/Survival.jl/latest/getting_started/)