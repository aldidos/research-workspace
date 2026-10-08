import sys
sys.path.append('.')
import pandas as pd
import dotenv
import os
dotenv.load_dotenv()

def pvalue_check(pvalue) : 
    tp = ''
    if pvalue < 0.001 : 
        tp = '***'    
    elif pvalue < 0.01 : 
        tp = '**'
    elif pvalue < 0.05 : 
        tp = '*'
    
    str_format = "{:.3f}{}".format(pvalue, tp)    
    return str_format

if __name__ == '__main__' : 
    working_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    dir_path = f'{working_dir}/data/analysis/'
    df = pd.read_csv(f'{dir_path}/study_subagent.temp_mwu_result.csv')

    df['str_effect_size'] = df['p-value'].apply(pvalue_check)

    vars = ['n_words', 'fre_score', 'h2', 'h3']
    for var in vars :     
        df_new = df[df['var'] == var]
        df_new_effectsize = df_new.pivot(index = 'x', columns = 'y', values = 'str_effect_size')
        df_new_effectsize.to_csv(f'{dir_path}/{var}_effectsize.csv')
