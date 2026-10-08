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
    output_dir = f'{working_base_dir}/data/analysis' 

    df = pd.DataFrame(subagentDatasetDao.get_valid_heading_titles_dataset())

    total_n_heading_titles = df['n_count'].sum()
    n_heading_titles = len(df)

    pd.DataFrame({
        'n_heading_titles' : [n_heading_titles], 
        'total_n_heading_titles' : [total_n_heading_titles], 
    }).to_csv(f'{output_dir}/valid_heading_titles_RQ3.csv')    