"""
File:
    tcopy.py

Description:
    Creates a deep copy of a tplot_variable, with a new name.

Parameters:
    names_in: str/list of str
        List of pytplot names.
    names_out: str/list of str
        List of pytplot names.
        If it is not provided, then suffix '-copy' is used.
    suffix:
        A suffix to apply. Default is '-copy'.

Notes:
    Allowed wildcards are ? for a single character, * from multiple characters.
"""

import pytplot
import pyspedas
import copy


def tcopy_one(name_in, name_out):
    # Copies one pytplot variable
    tvar_old = pytplot.data_quants[name_in]
    tvar_new = copy.deepcopy(tvar_old)
    tvar_new.name = name_out
    pytplot.data_quants.update({name_out: tvar_new})
    print(name_in + ' copied to ' + name_out)


def tcopy(names_in, names_out=None, suffix=None):

    names_in = pyspedas.tnames(names_in)
    if len(names_in) < 1:
        print('tcopy error: No pytplot variables found.')
        return

    if suffix is None:
        suffix = '-copy'

    if names_out is None:
        names_out = [s + suffix for s in names_in]

    if isinstance(names_out, str):
        names_out = [names_out]

    if len(names_in) != len(names_out):
        print('tcopy error: List with the names_in does not match list\
              with the names out.')
        return

    for i in range(len(names_in)):
        n = names_in[i]
        o = names_out[i]
        if len(pyspedas.tnames(n)) == 1:
            tcopy_one(n, o)
        else:
            print('tplot name not found: ' + n)
