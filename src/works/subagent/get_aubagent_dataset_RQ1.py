import sys
sys.path.append('.')
import pandas as pd
import math
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
from src.works.subagent.data.dao.subagent_category_dao import subagentCategoriesDao
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == '__main__' : 
    working_base_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    file_dir = f'{working_base_dir}/data/analysis'
    file_name = 'subagent_dataset_RQ2'
    undefined_category = subagentCategoriesDao.get_undefined_id()

    db_cursor = subagentDatasetDao.get_dataset_for_RQ1(undefined_category)
    df = pd.DataFrame(db_cursor)        

    subdf = pd.crosstab(df['repo_id'], df['category'])    
    subdf = (subdf > 0).astype(int)    
    sum_categories = subdf.sum()
    sum_categories = sum_categories.sort_values(ascending=False)
    sum_categories.to_csv(f'{file_dir}/dist_repos_by_subagent_categories_RQ1.csv')    
    subdf['n_subagents'] = subdf.sum(axis=1)
    count_n_subagents = subdf['n_subagents'].value_counts()
    count_n_subagents.to_csv(f'{file_dir}/dist_repos_by_n_subagents_RQ1.csv')
    subdf['n_subagents'].mode().to_csv(f'{file_dir}/n_subagents_mode.csv')
    pd.DataFrame({
        'median' : subdf['n_subagents'].median(), 
        'mean' : subdf['n_subagents'].mean()
    }, index=['median', 'mean']).to_csv(f'{file_dir}/mean_median.csv')
    
    subdf.to_csv(f'{file_dir}/crosstab_repo_subagents_RQ1.csv')    

    plt.figure()
    sns.countplot(subdf, x = 'n_subagents')
    plt.xlabel('#. Used subagent categories')
    plt.ylabel('#. Repositories')
    plt.savefig(f'{file_dir}/dist_repos_by_n_subagents_RQ1.png')

    plt.figure()
    # sns.countplot(df, x = 'category')
    sns.barplot(sum_categories)
    plt.xticks(rotation = 45, ha='right')
    plt.xlabel('Subagent category')
    plt.ylabel('#. Repositories')
    plt.tight_layout()
    plt.savefig(f'{file_dir}/dist_repos_by_subagent_categories_RQ1.png')
    