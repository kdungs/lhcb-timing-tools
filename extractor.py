# Helpers for extracting information from logfiles generated from Gaudi output.
#
# Author:  Kevin Dungs <kevin.dungs@cern.ch>
# Version: 2.0
# Date:    2014-03-10


def timings_from_file(filename):
    """
        Extract timing information from a file.
    """
    import re
    with open(filename) as f:
        data = f.read()
        return dict(re.findall(
            '^TimingAuditor\.TIMER\s+INFO\s+(\w+)\s+\|\s+([\d\.]+).*$',
            data,
            flags=re.MULTILINE
        ))


def extract_relevant(timings, relevant=None):
    """
        Extract relevant information from a timing dictionary that has been
        obtained from timings_from_file().
    """
    if not relevant:
        relevant = {  # Relevant information, list elements are summed over.
            'VELO tracking': ['FstVPDecoding', 'FstPixel'],
            'PV finding': ['HltPVsPV3D'],
            'VELO-UT tracking': ['CreateUTLiteClusters', 'PrVeloUT'],
            'Forward tracking': ['FTRawBankDecoder', 'FstForward'],
        }
    return {k: sum(float(timings[t]) for t in v) for k, v in relevant.items()}


def extract_multiple(filenames, relevant=None):
    """
        For a list of filenames, extracts the relevant information from them and
        returns a list of dictionaries containing the timings.
    """
    return [extract_relevant(timings_from_file(f), relevant) for f in filenames]
