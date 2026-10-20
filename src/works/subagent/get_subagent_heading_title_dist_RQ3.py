import sys
sys.path.append('.')
import pandas as pd
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == '__main__' : 
    working_base_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    file_dir = f'{working_base_dir}/data/analysis/RQ3'
    file_name = 'freq_uniq_instructions'
    dataset = subagentDatasetDao.get_heading_title_labeling_results()
    df = pd.DataFrame(dataset)

    plt.figure(figsize = (16, 10))

    sns.countplot(df, x = 'n_count')

    plt.xlabel('#. Subagents', fontsize = 16)
    plt.ylabel('#. Instructions', fontsize = 16)
    plt.xticks(rotation = 45, fontsize = 16)

    output_path = f'{file_dir}/{file_name}.png'
    plt.savefig(output_path)