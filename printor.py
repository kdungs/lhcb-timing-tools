#
#
#

def latex(study, significant_digits=None):
    for k, v in study.items():
        if significant_digits:
            print(('{} & {:' + str(significant_digits) + 'L}').format(
                k.ljust(30), v
            ))
        else:
            print('{} & {:L}'.format(k.ljust(30), v))