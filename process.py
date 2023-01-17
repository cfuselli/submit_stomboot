import sys
import batch_stbc
import time
from argparse import ArgumentParser, SUPPRESS
import shutil
import json


parser = ArgumentParser()
parser.add_argument('--config', type=str, default='config_test',
                        help='path to analysis configuration file.')

args = parser.parse_args()
config_file = args.config 

config = json.load(open(config_file, 'r'))

cmt_global      = config['cmt_global']
container       = config['container']
runs_filename   = config['runs_filename']
output_folder   = config['output_folder']
log_dir         = config['log_dir']
pyfile          = config['log_pyfiledir']
mem_per_cpu     = config['mem_per_cpu']


print('Ciao')

"""
Here do your st.make stuff
"""

print('Ciao ciao')



