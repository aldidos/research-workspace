import sys
sys.path.append('.')
import pandas as pd
import dotenv
import os
dotenv.load_dotenv()

def transform_res(res) : 
    if res == 'negligible' : 
        return 'N'
    if res == 'small' : 
        return 'S'
    if res == 'medium' : 
        return 'M'
    
    return 'L'

def pvalue_check(row) : 
    pvalue = row['p-value']
    res = row['res']
    tp = ''
    if pvalue < 0.001 : 
        tp = '***'    
    elif pvalue < 0.01 : 
        tp = '**'
    elif pvalue < 0.05 : 
        tp = '*'
    
    str_format = "{}{}".format(res, tp)    
    return str_format

if __name__ == '__main__' : 
    working_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    dir_path = f'{working_dir}/data/analysis/'
    df = pd.read_csv(f'{dir_path}/study_subagent.temp_mwu_result.csv')

    df['res'] = df['res'].transform(transform_res)
    df['str_effect_size'] = df.apply(pvalue_check, axis = 1)

    vars = ['n_words', 'fre_score', 'h2', 'h3']
    for var in vars :     
        df_new = df[df['var'] == var]
        df_new_effectsize = df_new.pivot(index = 'x', columns = 'y', values = 'str_effect_size')
        df_new_effectsize.to_csv(f'{dir_path}/{var}_effectsize.csv')
