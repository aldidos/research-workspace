import sys
sys.path.append('.')
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == '__main__' : 
    df = pd.DataFrame(subagentDatasetDao.get_exp_repo_dataset())    
    work_base_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')

    contributors_desc = df['contributors'].describe()
    stargazers_desc = df['stargazers'].describe()

    fig, axs = plt.subplots(2, 1)    
    fig.set_size_inches(16, 10)
    axs[0].set_title('(a)')
    axs[0].set_xlabel('#. Contributors')

    axs[1].set_title('(b)')
    axs[1].set_xlabel('#. Popularity')
    sns.boxplot(df, x = 'contributors', ax = axs[0]) 
    sns.boxplot(df, x = 'stargazers', ax = axs[1])
    plt.savefig(f'{work_base_dir}/data/analysis/n_contributors_popularity_dist.png')

    main_language_counts = df['mainLanguage'].value_counts()
    lang_idx = main_language_counts.sort_values(ascending = False).index
    main_language_desc = main_language_counts.describe()    

    plt.figure(figsize = (16, 10))
    sns.countplot(df, x = 'mainLanguage', order = lang_idx)
    plt.xlabel('Language')
    plt.ylabel('#. Frequency')
    plt.savefig(f'{work_base_dir}/data/analysis/main_language_counts.png')

    contributors_desc.to_csv(f'{work_base_dir}/data/analysis/contributors_desc.csv')
    stargazers_desc.to_csv(f'{work_base_dir}/data/analysis/stargazers_desc.csv')
    main_language_counts.to_csv(f'{work_base_dir}/data/analysis/main_language_counts.csv')

    