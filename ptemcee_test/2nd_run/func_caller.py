
import time
import gc  # Garbage collector.
#
from .inp import names_paths
from .inp import get_manual_strct
from .inp import get_data
# from .structure import trim_frame  # DEPRECATED
from .structure import histo_2d
from .structure import xy_density
from .structure import center
from .structure import radial_dens_prof
from .structure import field_density
from .structure import radius
from .structure import cluster_area
from .structure import contamination_index
from .structure import king_profile
from .errors import err_accpt_rejct
from .structure import stars_in_out_cl_reg
from .structure import field_regions
from .errors import err_range_avrg
#
from .data_analysis import compl_err_funcs
from .data_analysis import luminosity
from .data_analysis import ad_field_vs_clust
from .data_analysis import members_number
#
from .decont_algors import decont_algors
from .decont_algors import members_N_compare
from .decont_algors import cl_region_clean
#
from .data_analysis import plx_analysis
from .data_analysis import pms_analysis
#
from .out import inparams_out
from .out import cluster_members_file
from .best_fit import best_fit_synth_cl
from .out import mcmc_samples
from .out import synth_cl_file
from .out import massFunction  # TODO
from .out import create_out_data_file
# DEPRECATED 31/12/18
# from .errors import error_round
#
from .out import add_data_output
from .out import make_A1_plot
from .out import make_A2_plot
from .out import photComb
from .out import make_B1_plot
from .out import make_B2_plot
from .out import make_C1_plot
from .out import make_C2_plot
from .out import make_C3_plot
from .out import make_D1_plot
from .out import make_D2_plot
# DEPRECATED 22/11/18
# from .out import top_tiers
# DEPRECATED 28/07/19
# from .out import done_move


def main(cl_file, pd):
    '''
    Call each function sequentially. Four dictionaries are passed around:

    pd : contains all the input parameters stored in 'params_input.dat'.

    npd : names and paths for the cluster and all the files generated.
    Generated by 'names_paths' and never modified.

    cld : read cluster data. Generated by 'get_data'
    DEPRECATED: and modified by 'trim_frame', if the frame is manually trimmed.

    clp : contains all the information about the cluster gathered by the
    functions applied. Modified constantly throughout the code.

    '''

    # Start timing this loop.
    start = time.time()

    d1, d2 = cl_file[-3][-2:], cl_file[-1][-6:-4]
    d = {
        '1': ('10', 12, '10'), '2': ('10', 12, '20'), '3': ('10', 12, '30'),
        '4': ('10', 20, '10'), '5': ('10', 20, '20'), '6': ('10', 30, '30'),
        '7': ('10', 30, '10'), '8': ('10', 30, '20'), '9': ('10', 30, '30'),
        #
        '10': ('20', 12, '10'), '11': ('20', 12, '20'),
        '12': ('20', 12, '30'), '13': ('20', 20, '10'),
        '14': ('20', 20, '20'), '15': ('20', 20, '30'),
        '16': ('20', 30, '10'), '17': ('20', 30, '20'),
        '18': ('20', 30, '30'),
        #
        '19': ('30', 12, '10'), '20': ('30', 12, '20'),
        '21': ('30', 12, '30'), '22': ('30', 20, '10'),
        '23': ('30', 20, '20'), '24': ('30', 20, '30'),
        '25': ('30', 30, '10'), '26': ('30', 30, '20'),
        '27': ('30', 30, '30')}
    idx = str(int(float(d1) + 9 * (float(d2) - 1.)))
    pd['ntemps'], pd['nwalkers_ptm'], pd['tmax_ptm'] = d[idx]

    # File names (n) and paths (p) dictionary (d).
    npd = names_paths.main(cl_file, **pd)

    # Save params_input.dat file used.
    inparams_out.main(npd, **pd)

    # Get manual structural data and add to dictionary.
    pd = get_manual_strct.main(pd, **npd)

    # Cluster's data from file, as dictionary. Obtain both incomplete (ie: all
    # stars in data file) and complete (only those with full photometric data)
    # dictionaries.
    # Initiates cluster's parameters dictionary 'clp'.
    cld_i, cld_c, clp = get_data.main(npd, **pd)

    # DEPRECATED (at least for now, 08/05/18)
    # If Manual mode is set, display frame and ask if it should be trimmed.
    # cld = trim_frame.main(cld, **pd)

    # Obtain 2D coordinates histogram for the observed frame.
    clp = histo_2d.main(clp, **cld_i)

    # Gaussian filtered 2D x,y histograms.
    clp = xy_density.main(clp, cld_i, **pd)

    make_A1_plot.main(npd, cld_i, pd, **clp)

    # Cluster's center coordinates and errors.
    clp = center.main(cld_i, clp, **pd)

    # Density profile
    clp = radial_dens_prof.main(clp)

    # Field density value in stars/<area unit>.
    clp = field_density.main(clp, **pd)

    # Cluster radius
    clp = radius.main(cld_i, clp, **pd)

    # Cluster's area and total number of stars within the cluster region.
    clp = cluster_area.main(clp, **cld_i)

    # Contamination index.
    clp = contamination_index.main(clp, **cld_i)

    # King profiles based on the density profiles.
    clp = king_profile.main(clp, **pd)

    # ^ All the functions above use the *photo incomplete* dataset 'cld_i'

    # These three functions are applied for both datasets since we need the
    # 'cl_region' and 'field_regions' parameters with *photo incomplete* data
    # to be used by the DA, and the parameters obtained with the
    # *photo complete* dataset for the rest of the functions.
    print("Processing complete dataset:")
    # Accept and reject stars based on their errors.
    clp = err_accpt_rejct.main('comp', cld_c, clp, **pd)

    # Stars in and out of cluster's radius.
    clp = stars_in_out_cl_reg.main('comp', clp)

    # Field regions around the cluster's center.
    clp = field_regions.main('comp', clp, **pd)

    # Only process incomplete data if the the input data is not equal. Else
    # just use the complete dataset.
    if clp['flag_data_eq']:
        clp['cl_region_i'], clp['flag_no_fl_regs_i'], clp['field_regions_i'], \
            clp['cl_region_rjct_i'], clp['field_regions_rjct_i'] =\
            clp['cl_region_c'], clp['flag_no_fl_regs_c'],\
            clp['field_regions_c'], clp['cl_region_rjct_c'],\
            clp['field_regions_rjct_c']
    else:
        print("Processing incomplete dataset:")
        clp = err_accpt_rejct.main('incomp', cld_i, clp, **pd)
        clp = stars_in_out_cl_reg.main('incomp', clp)
        clp = field_regions.main('incomp', clp, **pd)

    # This is what these three functions generate. The 'x' separates incomplete
    # (i) and complete (c) data.
    #
    # err_accpt_rejct -------> acpt_stars_x
    #       |        '-------> rjct_stars_x
    #       |
    #       v
    # stars_in_out_cl_reg ---> acpt_stars_x --> cl_region_x
    #       |            |                 '--> stars_out_x
    #       |            |
    #       |            '---> rjct_stars_x --> cl_region_rjct_x
    #       |                              '--> stars_out_rjct_x
    #       v
    # field_regions --> stars_out_x ----------> field_regions_x
    #              '--> stars_out_rjct_x -----> field_regions_rjct_x

    # Uses the incomplete 'cl_region' and 'field_regions' data.
    make_A2_plot.main(npd, cld_i, pd, **clp)

    # v The functions below use the *photom complete* dataset with the
    # exception of the 'compl_err_funcs()' function and the Bayesian DA. The
    # DA uses the *photo incomplete* dataset to assign MPs. After this, only
    # those stars in the *photo complete* dataset are kept and passed forward
    # to the fundamental parameters estimation process.

    # Obtain exponential fit for the errors.
    clp = err_range_avrg.main(clp)

    # Combined error rejection & completeness function.
    clp = compl_err_funcs.main(clp, cld_i, cld_c)

    # Helper function for plotting.
    clp = photComb.main(pd, clp)

    make_B1_plot.main(npd, cld_c, pd, **clp)

    # Luminosity function and completeness level for each magnitude bin.
    clp = luminosity.main(clp, **cld_c)

    # DEPRECATED 31/10/18
    # # Physical cluster probability based on p_values distribution.
    # clp = kde_pvalue.main(clp, **pd)

    clp = ad_field_vs_clust.main(clp, cld_c, **pd)

    # Approximate number of cluster's members.
    clp = members_number.main(clp)

    # # Helper function for plotting.
    # clp = photComb.main(pd, clp)

    make_B2_plot.main(npd, cld_c, pd, **clp)

    # Apply decontamination algorithm.
    clp = decont_algors.main(clp, npd, **pd)

    # Obtain members parameter.
    clp = members_N_compare.main(clp)

    # Remove stars from the observed cluster according to a selected method.
    clp = cl_region_clean.main(clp, **pd)

    # Create data file with membership probabilities.
    cluster_members_file.main(clp, npd, **pd)

    make_C1_plot.main(npd, cld_c, pd, **clp)

    # Analyze parallax data if available.
    clp = plx_analysis.main(clp, **pd)

    # Analyze PMs data if available.
    clp = pms_analysis.main(clp, cld_i, **pd)

    make_C2_plot.main(npd, pd, **clp)
    make_C3_plot.main(npd, pd, cld_i, **clp)

    # Obtain best fitting parameters for cluster.
    clp = best_fit_synth_cl.main(clp, pd)

    # Save MCMC samples to file (if MCMC sampler was used)
    mcmc_samples.main(clp, pd, **npd)

    # Create output synthetic cluster file if one was found
    clp = synth_cl_file.main(clp, npd, **pd)

    # TODO #96
    # clp = massFunction.main(clp)

    # Create template output data file in /output dir.
    create_out_data_file.main(npd)

    # DEPRECATED 31/12/18
    # # Round fundamental parameters fitted and their errors
    # clp = error_round.fundParams(clp)

    # Add cluster data and flags to output file
    add_data_output.main(npd, pd, **clp)

    # Plot result of best match algorithm.
    make_D1_plot.main(npd, pd, **clp)

    # Plot final best match found.
    make_D2_plot.main(npd, cld_c, pd, **clp)

    # DEPRECATED 22/11/18
    # # Plot top tiers models and save to file.
    # top_tiers.main(npd, cld_c, pd, **clp)

    # DEPRECATED 28/07/19
    # # Move file to 'done' dir (if flag is set).
    # done_move.main(pd, **npd)

    elapsed = time.time() - start
    m, s = divmod(elapsed, 60)
    if m > 60:
        h, m = divmod(m, 60)
        t = "{:.0f}h {:.0f}m {:.0f}s".format(h, m, s)
    else:
        t = "{:.0f}m {:.0f}s".format(m, s)
    print("End of analysis for {} in {}\n".format(npd['clust_name'], t))

    # Force the Garbage Collector to release unreferenced memory.
    gc.collect()
