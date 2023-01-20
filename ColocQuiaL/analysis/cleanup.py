import os
import shutil

keep = ['cleanup.py', 'colocquial_wrapper.sh', 'QTL_config.R', 'qtl_config.sh']

for f in os.listdir():
    if f in keep:
        continue

    if os.path.isdir(f):
        shutil.rmtree('./{}'.format(f))
    else:
        os.remove(f)