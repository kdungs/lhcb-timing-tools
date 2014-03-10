# Quickly load whole studies.
#
# Author:  Kevin Dungs <kevin.dungs@cern.ch>
# Version: 2.0
# Date:    2014-03-10


def load_study(path, runs=10, prefix='', relevant=None):
    """ Load a study from {path} with {runs} runs.
        Additional dictionary of {relevant} algorithms can be used and is
        passed to the extractor.
    """
    from os.path import join
    from TimingTools import (
        analysor,
        extractor
    )
    return extractor.extract_multiple(
        [join(path, '{}{}.log'.format(prefix, i)) for i in range(1, runs+1)],
        relevant
    )


def load_means(path, runs=10, prefix='', relevant=None):
    """ Load the means for a study from {path} with {runs} runs.
        Additional dictionary of {relevant} algorithms can be used and is
        passed to the extractor.
    """
    from TimingTools import (
        analysor
    )
    return analysor.means_and_errors(load_study(path, runs, prefix, relevant))
