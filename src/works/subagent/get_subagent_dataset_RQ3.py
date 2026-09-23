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
    heading_category_names = df['ht_category'].unique()

    results = []
    for scn in subagent_category_names : 
        sub_df = df[ df['subagent_category'] == scn ]
        n_subagents = len(sub_df['_id'].unique())
        for hcn in heading_category_names : 
            n_hcn = len(sub_df[sub_df['ht_category'] == hcn])
            
            results.append({
                'subagent_category' : scn,
                'heading_category' : hcn,
                'proportion' : n_hcn / n_subagents
            })

    temp_df = pd.DataFrame(results)
    temp_df.to_json(f'{output_dir}/ht_category_prop_by_subagents.json', orient='records')     

    plt.figure(figsize = (18, 10))

    sns.barplot(temp_df, x = 'subagent_category', y = 'proportion', hue = 'heading_category')

    total_num_subagents = len(df['_id'].unique()) 
    ht_category_counts = df['ht_category'].value_counts()
    ht_category_prop = ht_category_counts.apply(lambda x : x / total_num_subagents )
    ht_category_prop.to_json(f'{output_dir}/ht_category_prop.json')    

    plt.xticks(rotation = 45, ha='right')    
    plt.xlabel('Subagent category')
    plt.ylabel('Proportion')
    plt.tight_layout()    
    plt.legend(ncol = 2, loc = 'upper left', fontsize = 12, bbox_to_anchor = (0.0, 1.0))
    plt.savefig(f'{output_dir}/subagent_instruction_category_prop_RQ3.png')    
