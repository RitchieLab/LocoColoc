import json

from cql_consts import setup_config_r_keys, setup_config_sh_keys, qtl_config_r_keys, qtl_config_sh_keys

def create_config_files(setup_args, qtl_args):
    cql_dir = setup_args['colocquial_dir']
    analysis_dir = '{}/analysis'.format(cql_dir)

    with open('{}/setup_config.sh'.format(cql_dir), 'w') as setup_sh:
        for key in setup_config_sh_keys:
            setup_sh.write('{}=\"{}\"\n'.format(key, setup_args[key]))

    setup_sh.close()

    with open('{}/setup_config.R'.format(cql_dir), 'w') as setup_r:
        for key in setup_config_r_keys:

            if isinstance(setup_args[key], list):
                arr = setup_args[key]
                vector_string = 'c('
                for i in range(len(arr)):
                    if i < len(arr) - 1:
                        vector_string += '\"{}\",'.format(arr[i])
                    else:
                        vector_string += '\"{}\")'.format(arr[i])
                val = vector_string
            elif isinstance(setup_args[key], int) or isinstance(setup_args[key], float):
                val = '{}'.format(setup_args[key])
            else:
                val = '\"{}\"'.format(setup_args[key])
            
            setup_r.write('{} = {}\n'.format(key, val))
            
    setup_r.close()

    with open('{}/qtl_config.sh'.format(analysis_dir), 'w') as qtl_sh:
        for key in qtl_config_sh_keys:
            if isinstance(qtl_args[key], int) or isinstance(qtl_args[key], float):
                val = '{}'.format(qtl_args[key])
            else:
                val = '\"{}\"'.format(qtl_args[key])

            qtl_sh.write('{}={}\n'.format(key, val))
            
    qtl_sh.close()

    with open('{}/QTL_config.R'.format(analysis_dir), 'w') as qtl_r:
        for key in qtl_config_r_keys:
            
            if isinstance(qtl_args[key], int) or isinstance(qtl_args[key], float):
                val = '{}'.format(qtl_args[key])
            else:
                val = '\"{}\"'.format(qtl_args[key])

            qtl_r.write('{} = {}\n'.format(key, val))
        
        qtl_r.write('chrom = CHROMOSOME\n')
        qtl_r.write('colocStart = STARTBP\n')
        qtl_r.write('colocStart = STOPBP\n')

    qtl_r.close()


def run_cql(args):
    config = open(args.file)
    input = json.load(config)['cql']

    create_config_files(input['setup_config'], input['qtl_config'])