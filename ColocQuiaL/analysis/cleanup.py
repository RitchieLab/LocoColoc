# Run to remove all files generated during running of ColocQuiaL

import os
import shutil

keep = ['cleanup.py', 'colocquial_wrapper.sh', 'QTL_config.R', 'qtl_config.sh', 'old_config', 'generated_config']

for f in os.listdir():
    if f in keep:
        continue

    if os.path.isdir(f):
        shutil.rmtree('./{}'.format(f))
    else:
        os.remove(f)