
# Mass

<!-- MarkdownTOC levels="1,2,3" autolink="true" style="ordered" -->

1. [Spitzer \(1969\)](#spitzer-1969)
1. [Spitzer \(1987\)](#spitzer-1987)
1. [Gerhard \(2000\)](#gerhard-2000)
1. [McCrady et al. \(2003\)](#mccrady-et-al-2003)
1. [Fleck \(2006\)](#fleck-2006)
1. [Sterrenstelsels & Kosmos \(2009\)](#sterrenstelsels--kosmos-2009)
1. [References:](#references)

<!-- /MarkdownTOC -->


## Spitzer (1969)

This article is apparently the origin of the relation:

    <v^2> = 0.4 * G*M / R                  (Eq 1)

(there's a 2nd term that is dismissed?) or

    M = 5/2 * <v^2>*R/G

where `<v^2>` is the *mean-square velocity for stars (of mass 2)* and `R` is the **half-mass radius**.



## Spitzer (1987)

If the system is isolated, with no external fields present... (the Virial Theorem gives):

    2T = -W ~ 0.4 (G*M^2) / r_h            (Eq 1-10)

where `T` is the total kinetic energy `M<v_m^2>/2`, `W` is the total gravitational energy, and `r_h` is the radius **half-mass radius**.

From the above we obtain:

    M = 5/2 * <v_m^2>*r_h/G

in concordance with Spitzer (1969). Following:

> *`r_hp`, the radius containing half the mass **in projection**, is generally about `3*r_h/4` for models with an isotropic velocity distribution*

we can derive:

    M = 5/2 * 4/3 * <v_m^2>*r_hp/G = 10/3 * <v_m^2>*r_hp/G



## Gerhard (2000)

> *in equilibrium, the radius of a stellar system is proportional to `G*M/V^2`, where M is the total mass and V the **RMS three-dimensional velocity** of the stars.*

    R = eta * G*M/V^2

> *if the relation is expressed in terms of the **half-mass radius** `r_h`, this dependence is weak and the constant is approximately 0.4*

    r_h = 0.4 * G*M/V^2

or

    M = 5/2 * r_h * V^2/G

> *assume that the cluster is spherical, `V^2=3*s^2`, where `s` is the one-dimensional **RMS velocity dispersion along the line-of-sight***

    M = 5/2 * r_h * 3*s^2/G = 7.5 * r_h*s^2/G



## McCrady et al. (2003)

> *Assuming that the light profile traces the mass distribution, the **half-light radius is used as a proxy for the half-mass radius**.*

> *the **half-light radius** is related to the observed **half-light radius in projection** (`r_hp`) by `r_hp~3/4 r_h` (Spitzer 1987), and the three-dimensional rms velocity `V` is related to the measured **one-dimensional line-of-sight velocity dispersion** `s_r` by `V^2=3*s_r^2`*

    M = 10 * r_hp*s_r^2/G

In this equation **both** quantities `r_hp, s_r` are assumed to be projected.



## Fleck (2006)




## Sterrenstelsels & Kosmos (2009) 

If only gravitational forces between particles with mass are at work, in an **equilibrium system** (such that the moment of inertia I=M*r^2 is constant in time) it can be proven that:

2T + U = 0

where T is the kinetic energy and U the gravitational potential energy.

The potential energy of a *uniform-density* sphere of mass M and radius R (for a spherical shell, the 3/5 factor becomes 1/2[1]) is:

U = -3/5 * G*M^2/R

where G is the *gravitational constant*. The kinetic energy of a cluster composed of N stars with average mass m and mean square velocity <v^2> is:

T = M<v^2>/2

The first equation the gives the **dynamical mass** (for a dynamically-relaxed cluster) as:

M = 5/3 * <v^2>*R/G

where R is the **3D radius** (i.e., not projected). To estimate <v^2> we observe that:

<v^2> = <v_x^2> + <v_y^2> + <v_z^2>

if motions are random then:

<v_x^2> = <v_y^2> = <v_z^2>

and:

<v^2> = 3 * <v_x^2>

resulting in:

M = 5 * <v_x^2>*R/G

where <v_x^2> is the *radial velocity* (why?).



The root mean square velocity (v_RMS) is:

v_RMS = sqrt(<v^2>)



* [Velocity dispersion](https://en.wikipedia.org/wiki/Velocity_dispersion) ($\sigma$): statistical dispersion of velocity about the mean velocity for a group of objects. The dispersion of the **radial velocities** can be used to estimate the group's mass from the *Virial Theorem*.





## References:

* [Spitzer (1969)](https://ui.adsabs.harvard.edu/abs/1969ApJ...158L.139S/abstract)
* [Spitzer (1987)](https://www.jstor.org/stable/j.ctt7ztvx4)
* [McCrady et al. (2003)](https://iopscience.iop.org/article/10.1086/377631)
* [Fleck (2006)](https://doi.org/10.1111/j.1365-2966.2006.10390.x)
* [Sterrenstelsels & Kosmos (2009)](https://www.astro.rug.nl/~weygaert/tim1publication/sk2009/StarClusters.pdf), PDF stored in folder

[1]: [Gravitational potential energy of any spherical distribution](https://physics.stackexchange.com/q/341065/8514)