import sys
sys.path.append('.')
import pandas as pd
import math
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
from src.works.subagent.data.dao.subagent_category_dao import subagentCategoriesDao
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import seaborn as sns
import os
load_dotenv()

if __name__ == '__main__' : 
    working_base_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    file_dir = f'{working_base_dir}/data/analysis/RQ2'
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
    df_mwu_result = pd.read_json(f'{file_dir}/{file_name}.json')
    df_mwu_result['effect_size'] = df_mwu_result['effect_size'].apply(lambda x : abs(x) )
    index = 'x'
    column = 'y'
    value = 'effect_size'
    mwu_vars = ['n_words', 'fre_score', 'h1', 'h2', 'h3', 'h4', 'h5' ]

    for mwu_var in mwu_vars : 
        sub_df = df_mwu_result[df_mwu_result['var'] == mwu_var]    
        sub_df.pivot(index = index, columns = column, values = value).to_json(f'{file_dir}/mwu_result_{mwu_var}.json') 

    #### heading tag distribution
    category = 'category'
    xlabel = 'Subagent'
    ylabel = '# Count'
    legend_title = 'Heading tag'
    output_file_path = f'{file_dir}/heading_counts_grouped_boxplot_RQ2.png'
    font_size = 16
        
    target_vars = ['h1', 'h2', 'h3', 'h4', 'h5']    

    df_long = pd.melt(
        df,
        id_vars=[category],
        value_vars=target_vars,
        var_name="Variable",
        value_name="Value",
    )    

    # 3. 그룹형 박스 플롯 그리기
    plt.figure(figsize=(16, 10))
    o = sns.boxplot(
        data=df_long,
        x=category,
        y="Value",
        hue="Variable",  # h, p, list별로 박스를 나눔
        palette="Set2", 
        showfliers = False
    )

    plt.xticks(rotation = 45, ha='right', fontsize = font_size)
    plt.tight_layout()
    plt.xlabel(xlabel, fontsize=font_size)
    plt.ylabel(ylabel, fontsize=font_size)    
    plt.legend(title=legend_title, loc = 'upper center', fontsize = font_size, title_fontsize = font_size)
    plt.savefig(output_file_path)

    # Distribution of n_words and fre_score    
    x = 'category'
    vars = ['n_words_log', 'fre_score']
    x_labels = ['Category', 'Category']
    y_labels = ['# words(log)', 'FRE score']
    ascendings = [False, True]

    for i in range(len(vars)) : 
        var = vars[i]
        plt.figure(figsize = (18, 10))
        order = df.groupby(x)[var].median().sort_values(ascending = ascendings[i]).index
        sns.violinplot(data=df, x=x, y=var, order=order) 

        plt.xlabel(x_labels[i], fontsize = font_size)
        plt.ylabel(y_labels[i], fontsize = font_size)
        plt.xticks(rotation = 45, ha='right', fontsize = font_size)
        plt.tight_layout()

        plt.savefig(f'{file_dir}/{var}_violin.png')