
# Stats notes

## Loss functions (mean, median, mode)

Definition of mean, median, and mode as the minimization of loss functions.

### [Modes, Medians and Means: A Unifying Perspective][1]

> Any traditional introductory statistics course will teach students the definitions of modes, medians and means. But, because introductory courses can't assume that students have much mathematical maturity, the close relationship between these three summary statistics can't be made clear. This post tries to remedy that situation by making it clear that all three concepts arise as specific parameterizations of a more general problem.

### [MAP or mean?!][2]

The MAP is expressed as a proper Bayes estimator.

> A frequent matter of debate in Bayesian inversion is the question, which of the two principle point-estimators, the maximum-a-posteriori (MAP) or the conditional mean (CM) estimate is to be preferred.

### [5 Regression Loss Functions All Machine Learners Should Know][3]

> All the algorithms in machine learning rely on minimizing or maximizing a function, which we call “objective function”. The group of functions that are minimized are called “loss functions”. A loss function is a measure of how good a prediction model does in terms of being able to predict the expected outcome. A most commonly used method of finding the minimum point of function is “gradient descent”. Think of loss function like undulating mountain and gradient descent is like sliding down the mountain to reach the bottommost point.


## Bootstrap

The statistic of interest for the original data (e.g: mean, MLE, applied on your **actual data**) is not necessarily equal to the mean of the bootstrap distribution (or *sampling distribution of the statistic*) for the statistic; as seen in [this example][5].

This is described more properly in this [SE answer][4]:

> For statistics that are not linear functions of the data (...) it would be wrong simply to substitute the bootstrap mean for the statistic's value on the data: that is not how bootstrapping works. Instead, by comparing the bootstrap mean to the data statistic we obtain information about the bias of the statistic. This can be used to adjust the original statistic to remove the bias. As such, the bias-corrected estimate thereby becomes an algebraic combination of the original statistic and the bootstrap mean. For more information, look up "BCa" (bias-corrected and accelerated bootstrap) and "ABC".

Th bias-corrected and accelerated bootstrap interval (BCa interval) is explained in detail in [this example][6]:

> The main advantage to the BCa interval is that it corrects for bias and skewness in the distribution of bootstrap estimates. The BCa interval requires that you estimate two parameters. The bias-correction parameter, z0, is related to the proportion of bootstrap estimates that are less than the observed statistic. The acceleration parameter, a, is proportional to the skewness of the bootstrap distribution. You can use the jackknife method to estimate the acceleration parameter.
>
> The bias correction factor is related to the proportion of bootstrap estimates that are less than the observed statistic. The acceleration parameter is proportional to the skewness of the bootstrap distribution.

A Python implementation can be found in the `scikits-bootstrap` [package][7]. An example of its use can be found in [the article mentioned above][6] (it also mentions the Approximate Bootstrap Confidence or `ABC` method).

All these methods are described in `An Introduction to the Bootstrap`, Efron & Tibshirani (1994), Chapter 4.


## MCMC

These two *Towards Data Science* articles introduce the concept at different levels:

* A (very) gentle introduction to the concept of MCMC: [Markov Chain Monte Carlo: Lifting your understanding of MCMC to an intermediate level][8]. It comments separately the concepts of Monte Carlo, Markov Chains, and acceptance/rejection sampling.

* A more detailed introduction is given in [A Zero-Math Introduction to Markov Chain Monte Carlo Methods][9]
> MCMC methods are used to approximate the posterior distribution of a parameter of interest by random sampling in a probabilistic space.
About Markov Chains it says:
> Markov chains, which seem like an unreasonable way to model a random variable over a few periods, can be used to compute the long-run tendency of that variable if we understand the probabilities that govern its behavior.

This CrossValidated [answer][10] gives a somewhat simple explanation of a Markov Chain, that can be summarized as:

> We want to generate random draws from a target distribution. We then identify a way to construct a 'nice' Markov chain such that its equilibrium probability distribution is our target distribution.
>
>If we can construct such a chain then we arbitrarily start from some point and iterate the Markov chain many times (like how we forecast the weather n times). Eventually, the draws we generate would appear as if they are coming from our target distribution.
>
> There are several ways to construct 'nice' Markov chains (e.g., Gibbs sampler, Metropolis-Hastings algorithm).

______________________________________________________________
[1]: http://www.johnmyleswhite.com/notebook/2013/03/22/modes-medians-and-means-an-unifying-perspective/
[2]: https://xianblog.wordpress.com/2014/03/05/map-or-mean/
[3]: https://heartbeat.fritz.ai/5-regression-loss-functions-all-machine-learners-should-know-4fb140e9d4b0
[4]: https://stats.stackexchange.com/a/133405/10416
[5]: https://blogs.sas.com/content/iml/2017/07/10/bootstrap-sasiml.html
[6]: https://blogs.sas.com/content/iml/2017/07/12/bootstrap-bca-interval.html
[7]: https://github.com/cgevans/scikits-bootstrap
[8]: https://towardsdatascience.com/markov-chain-monte-carlo-291d8a5975ae
[9]: https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50
[10]: https://stats.stackexchange.com/a/207/10416
