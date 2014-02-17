#
#
#


def load_study(path, runs=10):
    """
    """
    from os.path import join
    import analysor
    import extractor
    return analysor.means_and_errors(extractor.extract_multiple(
        [join(path, '{}.log'.format(i)) for i in range(1, runs+1)]
    ))