import os

CONFIG = {'local_data_dir': 'psp_data/',
          'remote_data_dir': 'https://spdf.sci.gsfc.nasa.gov/pub/data/psp/'}

# override local data directory with environment variables
if os.environ.get('SPEDAS_DATA_DIR'):
    CONFIG['local_data_dir'] = os.sep.join([os.environ['SPEDAS_DATA_DIR'], 'psp'])

if os.environ.get('PSP_DATA_DIR'):
    CONFIG['local_data_dir'] = os.environ['PSP_DATA_DIR']