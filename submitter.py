"""
Carlo Fuselli
cfuselli@nikhef.nl
-------------------

Example script to submit jobs to stomboot using the batch_stcb module 

"""


import sys
#sys.path.insert(0, '/data/xenon/cfuselli/stomboot_thesis/')

import batch_stbc
import time
from argparse import ArgumentParser, SUPPRESS
import shutil
import json

parser = ArgumentParser()
parser.add_argument('--config', type=str, default='config_test',
                        help='path to analysis configuration file.')
args = parser.parse_args()


config_file = 'configs/' + args.config + '.json' 
timestr = time.strftime("_%Y%m%d_%H%M%S")
tmp_config_file = 'configs/tmp/' + args.config + timestr + '.json' 

with open(config_file, 'r') as f:
    config = json.load(f)

shutil.copyfile(config_file, tmp_config_file)

cmt_global      = config['cmt_global']
container       = config['container']

runs_filename   = config['runs_filename']
npergroup       = config['npergroup']


output_folder   = config['output_folder']
log_dir         = config['log_dir']
pyfile          = config['pyfile']

mem_per_cpu     = config['mem_per_cpu']


with open(runs_filename) as file:
    run_ids = file.readlines()
    run_ids = [line.rstrip() for line in run_ids]


print('Preparing to process:')
for i in range(len(run_ids)):
    
    log       = log_dir + ('log_%i.sh' % i)
    jobname   = 'job_%i' % i

    jobstring = f"""
    
    echo "Starting process_data"
    echo "{i} {tmp_config_file}"
    echo "soourcing /cvmfs/xenon.opensciencegrid.org/releases/nT/{container}/setup.sh"
    source /cvmfs/xenon.opensciencegrid.org/releases/nT/{container}/setup.sh 

    python {pyfile} --config {tmp_config_file}    
    
    echo "Script complete, bye byeee!"
    echo `date`
    
    """
    
    
    print('Submitting %i/%i' % (i, len(run_ids
                                      )-1), jobname)
    batch_stbc.submit_job(jobstring, 
                      log=log, 
                      jobname=jobname, 
                      mem_per_cpu=mem_per_cpu)

print('Finished')


