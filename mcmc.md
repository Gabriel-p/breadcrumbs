# MCMC

These *Towards Data Science* articles introduce the concept at different levels:

* A (very) gentle introduction to the concept of MCMC: [Markov Chain Monte Carlo: Lifting your understanding of MCMC to an intermediate level][1]. It comments separately the concepts of Monte Carlo, Markov Chains, and acceptance/rejection sampling.

* A more detailed introduction is given in [A Zero-Math Introduction to Markov Chain Monte Carlo Methods][2]
> MCMC methods are used to approximate the posterior distribution of a parameter of interest by random sampling in a probabilistic space.
About Markov Chains it says:
> Markov chains, which seem like an unreasonable way to model a random variable over a few periods, can be used to compute the long-run tendency of that variable if we understand the probabilities that govern its behavior.

* The article [MCMC Intuition for Everyone][3] comments a bit more on Markov Chains, and makes the point:
> Why is a Markov Chain important? It is important because of its Stationary Distribution.
> The stationary state distribution is important because it lets you define the probability for every state of a system at a random time.

This CrossValidated [answer][4] gives a somewhat simple explanation of a Markov Chain, that can be summarized as:

> We want to generate random draws from a target distribution. We then identify a way to construct a 'nice' Markov chain such that its equilibrium probability distribution is our target distribution.
>
>If we can construct such a chain then we arbitrarily start from some point and iterate the Markov chain many times (like how we forecast the weather n times). Eventually, the draws we generate would appear as if they are coming from our target distribution.
>
> There are several ways to construct 'nice' Markov chains (e.g., Gibbs sampler, Metropolis-Hastings algorithm).



___________________________________________________________________________
[1]: https://towardsdatascience.com/markov-chain-monte-carlo-291d8a5975ae
[2]: https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50
[3]: https://towardsdatascience.com/mcmc-intuition-for-everyone-5ae79fff22b1
[4]: https://stats.stackexchange.com/a/207/10416

