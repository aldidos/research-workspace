import sys
sys.path.append('.')
import pandas as pd
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
from src.works.subagent.data.dao.subagent_category_dao import subagentCategoriesDao
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__' : 
    output_dir = 'E:/research_subagent/data/analysis'
    undefined_category = subagentCategoriesDao.get_undefined_id()

    df = pd.DataFrame( subagentDatasetDao.get_dataset_for_RQ3(undefined_category) )     

    subagent_category_names = df['subagent_category'].unique()
    instruction_category_names = df['ht_category'].unique()

    inst_freq = pd.crosstab(df['subagent_category'], df['ht_category'])
    inst_freq.to_csv(f'{output_dir}/inst_freq.csv')

    sub_file_inst_freq = pd.crosstab(df['_id'], df['ht_category'])        
    inst_category_freq_sum = sub_file_inst_freq.sum()    
    inst_category_freq_sum.to_csv(f'{output_dir}/instruction_category_freq_sum.csv')    

    sub_file_inst_freq['n_instructions'] = sub_file_inst_freq.apply(lambda row : row.sum(), axis = 1)
    sub_file_inst_freq.to_csv(f'{output_dir}/sub_file_inst_freq.csv')
    sub_file_inst_freq['n_instructions'].mode().to_csv(f'{output_dir}/sub_file_inst_freq_mode.csv')
    inst_freq_median = sub_file_inst_freq['n_instructions'].median()
    inst_freq_mean = sub_file_inst_freq['n_instructions'].mean()
    pd.DataFrame({'name' : ['median', 'mean'], 'value' : [inst_freq_median, inst_freq_mean]}).to_csv(f'{output_dir}/sub_file_inst_freq_median_mean.csv')
    
    inst_category_freq_suum_index = inst_category_freq_sum.sort_values(ascending = False).index

    instruction_counts = sub_file_inst_freq['n_instructions'].value_counts() 
    instruction_counts.loc[0] = 253 ####
    df_instruction_counts = pd.DataFrame({ 'counts' : instruction_counts}, index = instruction_counts.index)

    plt.figure(figsize = (18, 10))    
    plt.xlabel('Instruction')
    plt.ylabel('#. Subagents')
    plt.tight_layout()
    sns.countplot(df, x = 'ht_category', order = inst_category_freq_suum_index)    
    plt.savefig(f'{output_dir}/inst_dist_RQ3.png')    

    plt.figure(figsize = (18, 10))
    plt.xlabel('#. Instructions')
    plt.ylabel('#. Subagents')
    sns.barplot(df_instruction_counts, x = 'n_instructions', y = 'counts')
    plt.savefig(f'{output_dir}/inst_num_dist_RQ3.png')

    plt.figure(figsize = (18, 10))
    sns.countplot(df, x = 'subagent_category', hue = 'ht_category')
    plt.xlabel('Subagent')
    plt.ylabel('#. Instructions')
    plt.xticks(rotation = 45, ha='right')    
    plt.tight_layout()
    plt.legend(title = 'Instruction')
    plt.savefig(f'{output_dir}/inst_dist_by_subagent_category_RQ3.png')
