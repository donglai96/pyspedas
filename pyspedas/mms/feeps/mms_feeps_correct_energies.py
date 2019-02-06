'''
 PURPOSE:
       This function modifies the energy table in FEEPS spectra (intensity, count_rate, counts) variables
       using the function: mms_feeps_energy_table (which is s/c, sensor head and sensor ID dependent)

 NOTES:
     BAD EYES are replaced by NaNs

'''

import pytplot
from pytplot import get_data, store_data
from .mms_feeps_energy_table import mms_feeps_energy_table

def mms_feeps_correct_energies(probes, data_rate, level='l2', suffix=''):

    types = ['top', 'bottom']
    sensors = range(1, 13)
    units_types = ['intensity', 'count_rate', 'counts']

    for probe in probes:
        for sensor_type in types:
            for sensor in sensors:
                if sensor >= 6 and sensor <= 8: 
                    species = 'ion'
                else: 
                    species = 'electron'

                for units in units_types:
                    var_name = 'mms'+probe+'_epd_feeps_'+data_rate+'_'+level+'_'+species+'_'+sensor_type+'_'+units+'_sensorid_'+str(sensor)

                    times, data = get_data(var_name+suffix)
                    energies = pytplot.data_quants[var_name+suffix].spec_bins.values

                    energy_map = mms_feeps_energy_table(probe, sensor_type[0:3], sensor)

                    store_data(var_name+suffix, data={'x': times, 'y': data, 'v': energies})