import sys
sys.path.append('.')
import pandas as pd
import math
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
from src.works.subagent.data.dao.subagent_category_dao import subagentCategoriesDao

if __name__ == '__main__' : 
    file_dir = 'E:/research_subagent/data/analysis'
    file_name = 'subagent_dataset_RQ2'
    undefined_category = subagentCategoriesDao.get_undefined_id()

    db_cursor = subagentDatasetDao.get_dataset_for_RQ2(undefined_category)
    df = pd.DataFrame(db_cursor)
    df = df.fillna(0)
    
    df['n_words_log'] = df['n_words'].apply(lambda x : math.log1p(x) )

    output_file_path = f'{file_dir}/{file_name}.json'
    df.to_json(output_file_path, orient='records') 

    medians = df.groupby('category')[['n_words', 'fre_score', 'h1', 'h2', 'h3', 'h4', 'h5']].median()
    medians.to_json(f'{file_dir}/{file_name}_medians.json')

    ####
    file_name = 'mwu_result'
    df = pd.read_json(f'{file_dir}/{file_name}.json')
    df['effect_size'] = df['effect_size'].apply(lambda x : abs(x) )
    index = 'x'
    column = 'y'
    value = 'effect_size'
    mwu_vars = ['n_words', 'fre_score', 'h1', 'h2', 'h3', 'h4', 'h5' ]

    for mwu_var in mwu_vars : 
        sub_df = df[df['var'] == mwu_var]    
        sub_df.pivot(index = index, columns = column, values = value).to_json(f'{file_dir}/mwu_result_{mwu_var}.json')    