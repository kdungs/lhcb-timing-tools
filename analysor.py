#
#
#


def mean_and_error(xs):
    from scipy.stats import sem
    from uncertainties import ufloat
    """
        Calculate mean and SEM of a numpy array xs.

        Returns a ufloat.
    """
    return ufloat(xs.mean(), sem(xs))


def means_and_errors(timings):
    import numpy as np
    return {
        key: mean_and_error(np.array([t[key] for t in timings]))
        for key in timings[0].keys()
    }