
# Autocorrelation and effective samples


The `emcee` [article about convergence][1] defines the autocorrelation time as:

> Tf is the integrated autocorrelation time for the chain. In other words, N/Tf is the effective number of samples and Tf is the number of steps that are needed before the chain "forgets" where it started (...) if you can estimate Tf, then you can estimate the number of samples that you need to generate to reduce the relative error on your target integral to (say) a few percent.

The author arrives at the conclusion that when N>=50*Tf (e.e: N_eff>=50) then the Tf value is properly estimated:

> with emcee (..) we can use the parallel chains to reduce the variance and we've found that chains longer than about 50*Tf are often sufficient (to estimate the integrated autocorrelation time)

Questions/doubts:

1. Should I thin my chains?
   1. Should I thin on a per-chain basis using the per-chain Tf?
2. To obtain the ESS should I multiply N/Tf by the number of chains? This usually results in a **very** large ESS, even with chains that look **very** poorly mixed.
3. 






________________________________________________
[1]: https://emcee.readthedocs.io/en/latest/tutorials/autocorr/