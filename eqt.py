import json
import pandas as pd
import rpy2.robjects as ro

def run_eqt(args):
    config = open(args.file)
    input = json.load(config)['eqt']

    arg_dict = {**input['required']}

    for k, v in (input['required']).items():
        if k[-2:] == "df":
            arg_dict[k] = v
        
    for k, v in (input['optional']).items():
        if v != "":
            if k[-2:] == "df":
                arg_dict[k] = v
            else:
                arg_dict[k] = v

    r = ro.r
    r('''source('./eQTpLot/R/eqt_wrapper.R')''')

    run_eqt = ro.globalenv['run_eqt']
    run_eqt(**arg_dict)