
# Autocorrelation and effective samples


The `emcee` [article about convergence][1] defines the autocorrelation time as:

> Tf is the integrated autocorrelation time for the chain. In other words, N/Tf is the effective number of samples and Tf is the number of steps that are needed before the chain "forgets" where it started (...) if you can estimate Tf, then you can estimate the number of samples that you need to generate to reduce the relative error on your target integral to (say) a few percent.

The author arrives at the conclusion that when N>=50*Tf (e.e: N_eff>=50) then the Tf value is properly estimated:

> with emcee (..) we can use the parallel chains to reduce the variance and we've found that chains longer than about 50*Tf are often sufficient (to estimate the integrated autocorrelation time)

According to [Convergence Diagnostics For Markov chain Monte Carlo, Ford (2015)][3] page 20, we should look for:

> the smallest lag to give an $\rho lag \approx 0$

and this is:

> One of several methods for estimating how many iterations of Markov chain are needed for effectively independent samples



## Definitions


* Covariance:

```
$c(x, y) = \frac{1}{N}\sum_{i=1}^N (x_i-\hat{x})(y_i-\hat{y})$
```

* Auto-covariance of $\theta$ parameter with its $k$ lag:

```
$c(k) = \frac{1}{N-k}\sum_{i=1}^{N-k} (\theta_i-\hat{\theta})(\theta_{i+k}-\hat{\theta})$
```
    
* Normalized autocorrelation function:

```
$\rho(k) = \frac{c(k)}{c(0)} = \frac{\sum_{i=1}^{N-k} (\theta_i-\hat{\theta})(\theta_{i+k}-\hat{\theta})}{\sum_{i=1}^{N}(\theta_i-\hat{\theta})^2}$
```

* Integrated autocorrelation time:

```
$\tau = \sum_{k=-\infty}^{\infty} \rho(k)$
```

or for some $M<<N$

```
$\hat{\tau}(M) = 1 + 2 \sum_{k=1}^{M} \rho(k)$
```





# About thinning

Questions/doubts:

1. Should I thin my chains?
   1. Should I thin on a per-chain basis using the per-chain Tf?
2. To obtain the ESS should I multiply N/Tf by the number of chains? This usually results in a **very** large ESS, even with chains that look **very** poorly mixed.

Answers (or comments):

1. Apparently not, according to Kruschke [Thinning to reduce autocorrelation: Rarely useful!][2]. Nonetheless, that same article states that:

> "Unless there is severe autocorrelation, e.g., high correlation with, say [lag]=30, we don't believe that thinning is worthwhile. (p.146)"

The value `lag=30` is a very common (even low) value in the `ptemcee` chains, so perhaps I should?



________________________________________________
[1]: https://emcee.readthedocs.io/en/latest/tutorials/autocorr/
[2]: http://doingbayesiandataanalysis.blogspot.com/2011/11/thinning-to-reduce-autocorrelation.html
[3]: https://astrostatistics.psu.edu/RLectures/diagnosticsMCMC.pdf
