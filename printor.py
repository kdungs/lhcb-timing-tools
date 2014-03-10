# Prints a readymade LaTeX table of a timing study for use in publications.
#
# Author:  Kevin Dungs <kevin.dungs@cern.ch>
# Version: 2.0
# Date:    2014-03-10


def latex(study, significant_digits=None):
    from TimingTools import analysor
    formatstring = '{:L}'
    if significant_digits:
        formatstring = '{:.' + str(significant_digits) + 'L}'
    for k, v in study.items():
        print(('{}  &  ' + formatstring).format(k.ljust(30), v))
    print(('{}  &  ' + formatstring).format('Total'.ljust(30), analysor.total(study)))
