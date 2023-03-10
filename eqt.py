import json
import subprocess

def run_eqt(args):
    config = open(args.file)
    input = json.load(config)['eqt']
    print(input)