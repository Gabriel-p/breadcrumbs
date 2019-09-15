
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    """
    for num in ('2'):
        d, results = analysis_res(num)

        good_res, avrg_res, bad_res = split_res(d, results)

        if num == '1':
            # x: time, y: tau, m=ntemps, s/fc=nchains, c=Tmax
            mrk = {'10': 'o', '20': 's', '50': '^'}
            clr = {'20': 'b', '50': 'g', 'inf': 'r'}
            fcr = {20: 'c', 30: 'k', 40: 'w'}
            title = "Ntemps: o=10, s=20, ^=50 | Nchains: c=12, k=20, w=30 |" +\
                " Tmax: B=20, G=50, R=inf"
        elif num == '2':
            # x: time, y: tau, m=ntemps, s/fc=nchains, c=Tmax
            mrk = {'10': 'o', '20': 's', '30': '^'}
            clr = {'10': 'b', '20': 'g', '30': 'r'}
            fcr = {12: 'c', 20: 'k', 30: 'w'}
            title = "Ntemps: o=10, s=20, ^=30| Nchains: c=12, k=20, w=30 |" +\
                " Tmax: B=10, G=20, R=30"

        plot1(good_res, avrg_res, bad_res, num, mrk, clr, fcr, title)
        plot2(good_res, avrg_res, bad_res, num, mrk, clr, fcr, title)


def analysis_res(num):
    """
    """

    if num == '1':
        # Input ptemcee parameters for each run: ntemps, nchains, Tmax
        d = {
            '1': ('10', 20, '20'), '2': ('10', 20, '50'),
            '3': ('10', 20, 'inf'), '4': ('10', 30, '20'),
            '5': ('10', 30, '50'), '6': ('10', 30, 'inf'),
            '7': ('10', 40, '20'), '8': ('10', 40, '50'),
            '9': ('10', 40, 'inf'),
            #
            '10': ('20', 20, '20'), '11': ('20', 20, '50'),
            '12': ('20', 20, 'inf'), '13': ('20', 30, '20'),
            '14': ('20', 30, '50'), '15': ('20', 30, 'inf'),
            '16': ('20', 40, '20'), '17': ('20', 40, '50'),
            '18': ('20', 40, 'inf'),
            '19': ('50', 20, '20'), '20': ('50', 20, '50'),
            '21': ('50', 20, 'inf'), '22': ('50', 30, '20'),
            '23': ('50', 30, '50'), '24': ('50', 30, 'inf'),
            '25': ('50', 40, '20'), '26': ('50', 40, '50'),
            '27': ('50', 40, 'inf')}

        # Summarized result
        # MAF, Tau, Lmin, time, my impression (0: bad, 1: avrg, 2: good)
        results = {
            '1': (.009, 14, -812.6, 69, 2), '10': (.019, 11, -806.9, 142, 2),
            '19': (.033, 4.5, -790, 340, 2), '2': (.021, 45, -777.5, 70, 1),
            '11': (.015, 19, -765.7, 153, 2), '20': (.015, 29, -797.1, 235, 2),
            '3': (.018, 75, -816.9, 57, 0), '12': (.022, 40, -758.9, 88, 0),
            '21': (.019, 65, -798.9, 96, 0), '4': (.013, 50, -776.8, 70, 1),
            '13': (.016, 31, -796.4, 231, 2), '22': (.03, 9, -786.1, 524, 2),
            '5': (.019, 37, -794.3, 71, 1), '14': (.052, 35, -767.6, 225, 1),
            '23': (.021, 34, -793.3, 521, 2), '6': (.034, 45, -771.6, 87, 0),
            '15': (.021, 45, -786.7, 132, 0), '24': (.018, 71, -767.2, 141, 0),
            '7': (.018, 50, -778.4, 152, 1), '16': (.021, 35, -775.3, 261, 2),
            '25': (.033, 17.5, -808.6, 423, 2), '8': (.015, 40, -783, 149, 1),
            '17': (.011, 40, -777.3, 298, 2), '26': (.025, 16, -780.3, 426, 2),
            '9': (.02, 49, -793.2, 114, 0), '18': (.021, 61, -793.5, 174, 0),
            '27': (.019, 75, -801.7, 182, 0)
        }
    elif num == '2':
        d = {
            '1': ('10', 12, '10'), '2': ('10', 12, '20'),
            '3': ('10', 12, '30'), '4': ('10', 20, '10'),
            '5': ('10', 20, '20'), '6': ('10', 30, '30'),
            '7': ('10', 30, '10'), '8': ('10', 30, '20'),
            '9': ('10', 30, '30'),
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

        # Summarized result
        # MAF, Tau, steps, time, my impression (0: bad, 1: avrg, 2: good)
        results = {
            '1': (.019, 31, 2e4, 174, 2), '10': (.027, 50, 2e4, 360, 1),
            '19': (.029, 29, 12750, 360, 1), '2': (.051, 66, 2e4, 164, 0),
            '11': (.039, 52, 2e4, 357, 1), '20': (.036, 51, 12650, 360, 1),
            '3': (.057, 26, 2e4, 174, 1), '12': (.083, 25, 2e4, 359, 1),
            '21': (.036, 16, 12450, 360, 2), '4': (.048, 75, 2e4, 284, 0),
            '13': (.033, 21, 11900, 360, 2), '22': (.021, 14, 10850, 360, 2),
            '5': (.031, 47, 2e4, 255, 1), '14': (.054, 12, 11950, 360, 2),
            '23': (.064, 19, 8550, 360, 1), '6': (.055, 70, 16900, 360, 0),
            '15': (.118, 11, 11600, 360, 1), '24': (.025, 18, 10600, 360, 2),
            '7': (.202, 59, 16700, 360, 0), '16': (.03, 55, 7900, 360, 1),
            '25': (.01, 17.5, 6250, 360, 2), '8': (.037, 52, 16300, 360, 1),
            '17': (.02, 69, 8050, 360, 1), '26': (.019, 17.5, 6350, 360, 2),
            '9': (.175, 60, 2e4, 251, 1), '18': (.101, 80, 14300, 360, 1),
            '27': (.014, 37, 7600, 360, 2)
        }

    return d, results


def split_res(d, results):
    """
    """
    bad_res, avrg_res, good_res = [], [], []
    for key, val in results.items():
        if val[4] == 0:
            bad_res.append((*d[key], *val[:4]))
        elif val[4] == 1:
            avrg_res.append((*d[key], *val[:4]))
        elif val[4] == 2:
            # temp = d[key][2]) if d[key][2] != 'inf' else 100.
            good_res.append((*d[key], *val[:4]))

    return good_res, avrg_res, bad_res


def plot1(good_res, avrg_res, bad_res, run, mrk, clr, fcr, title):
    """
    """

    fig = fig = plt.figure(figsize=(30, 10))
    plt.suptitle(title, y=1.05)

    plt.subplot(131)
    plt.title("Good")
    for cl in good_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            # Nsteps / Tau, Tau
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)
    if run == '1':
        plt.xlabel("Minutes")
        plt.xlim(30, 600)
    if run == '2':
        plt.xlabel("Nsteps / Tau")
        plt.xlim(100, 1200)
    plt.ylim(0, 90)
    plt.ylabel("Tau")

    plt.subplot(132)
    plt.title("Average")
    for cl in avrg_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            # Nsteps / Tau, Tau
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)
    if run == '1':
        plt.xlabel("Minutes")
        plt.xlim(30, 600)
    if run == '2':
        plt.xlabel("Nsteps / Tau")
        plt.xlim(100, 1200)
    plt.ylim(0, 90)
    plt.ylabel("Tau")

    plt.subplot(133)
    plt.title("Bad")
    for cl in bad_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            # Nsteps / Tau, Tau
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)
    if run == '1':
        plt.xlabel("Minutes")
        plt.xlim(30, 600)
    if run == '2':
        plt.xlabel("Nsteps / Tau")
        plt.xlim(100, 1200)
    plt.ylim(0, 90)
    plt.ylabel("Tau")

    fig.tight_layout()
    plt.savefig("split_res_{}.png".format(run), dpi=150, bbox_inches='tight')


def plot2(good_res, avrg_res, bad_res, run, mrk, clr, fcr, title):
    """
    """

    fig = fig = plt.figure(figsize=(10, 10))
    plt.title(title)

    for cl in good_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            # Nsteps / Tau, Tau
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)
    for cl in avrg_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)
    for cl in bad_res:
        m, s, c, fc = mrk[cl[0]], cl[1], clr[cl[2]], fcr[cl[1]]
        if run == '1':
            x, y = cl[6], cl[4]
        if run == '2':
            x, y = cl[5] / cl[4], cl[4]
        plt.scatter(x, y, marker=m, s=s**2, edgecolors=c, lw=2, facecolor=fc)

    if run == '1':
        plt.xlabel("Minutes")
    if run == '2':
        plt.xlabel("Nsteps / Tau")
    plt.ylabel("Tau")

    fig.tight_layout()
    plt.savefig("all_res_{}.png".format(run), dpi=150, bbox_inches='tight')

    # # x: time, y: tau, m=ntemps, s=Tmax, c=Lkl
    # xl, yl, ml, sl, co = [[] for _ in range(5)]
    # for cl in good_res:
    #     x, y, m, s, c = cl[6], cl[4], mrk[cl[0]], cl[2], -cl[5]
    #     s = float(s) if s != 'inf' else 100
    #     # plt.scatter(x, y, marker=m, s=s, c=c)
    #     xl.append(x)
    #     yl.append(y)
    #     ml.append(m)
    #     sl.append(s)
    #     co.append(c)
    # plt.scatter(xl, yl, s=sl, c=co)
    # plt.colorbar()
    # plt.xlabel("Minutes")
    # plt.ylabel("Tau")
    # plt.show()


if __name__ == '__main__':
    main()
