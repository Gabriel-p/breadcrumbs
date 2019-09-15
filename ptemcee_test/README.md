
I analyzed the cluster HAF14 with different inputs for the `ptemcee` sampler, to test what parameter values gave the best performance.

The numbers in the dictionaries in the `ptemcee_test` script correspond to the following input files:

input_01: (1, 10, 19), input_02: (2, 11, 20), input_03: (3, 12, 21)
input_04: (4, 13, 22), input_05: (5, 14, 23), input_06: (6, 15, 24)
input_07: (7, 16, 25), input_08: (8, 17, 26), input_09: (9, 18, 27)

# 1st analysis

Used a fixed number of steps set to 4000, and these input parameters:

Ntemps | Nchains | Tmax
-----------------------
  10   |   20    |  20
  20   |   30    |  50
  50   |   40    |  inf

The analysis points to the best four performers being:

(ntemps, nchains, Tmax)
-----------------------
(10, 20, 20), input_01,1 (1)  <-- min=69
(20, 20, 20), input_01,2 (10) <-- min=142
(20, 20, 50), input_02,2 (11) <-- min=153
(50, 20, 20), input_01,3 (19) <-- min=340

Conclusions:

* Around 20 temps seems to be a good compromise between runtime and performance
* More than 20 chains actually affects the performance rather than helping
* Using `Tmax=inf` is *very* detrimental to the performance


# 2nd analysis

The second run uses a fixed number of hours set to 6, 20000 steps, and these
`ptemcee` parameters:

Ntemps | Nchains | Tmax
-----------------------
  10   |   12    |  10
  20   |   20    |  20
  30   |   30    |  30

The analysis points to the best four performers being:

(ntemps, nchains, Tmax)
-----------------------
(20, 20, 20), input_05,2 (14)
(20, 20, 30), input_06,2 (15) <-- This one has a values of Tau and ESS even
better than the above, but the chains are a bit stuck.
(30, 20, 10), input_04,3 (22)
(30, 12, 30), input_03,3 (21)

Conclusions:

* Between 10 and 30 temps seems to be a reasonable number
* More than 20 chains **definitely** affect the performance. Fewer chains gives mixed results
* A value between 10 and 30 for `Tmax` seems to be reasonable.