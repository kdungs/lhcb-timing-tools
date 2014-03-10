# Useful functions for analysing studies.
# Helps by calculating means as ufloats.
#
# Author:  Kevin Dungs <kevin.dungs@cern.ch>
# Version: 2.0
# Date:    2014-03-10


def mean_and_error(xs):
    """
        Calculate mean and SEM of a numpy array xs.

        Returns a ufloat.
    """
    from scipy.stats import sem
    from uncertainties import ufloat
    return ufloat(xs.mean(), sem(xs))


def means_and_errors(timings):
    import numpy as np
    return {
        key: mean_and_error(np.array([t[key] for t in timings]))
        for key in timings[0].keys()
    }


def total(timing):
    return sum(timing.values())
