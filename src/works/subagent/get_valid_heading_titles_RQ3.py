import sys
sys.path.append('.')
import pandas as pd
from src.works.subagent.data.dao.subagent_dataset_dao import subagentDatasetDao
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
load_dotenv()


if __name__ == '__main__' : 
    working_base_dir = os.getenv('SUBAGENT_WORK_BASE_DIR')
    output_dir = f'{working_base_dir}/data/analysis' 

    df = pd.DataFrame(subagentDatasetDao.get_heading_title_labeling_results())    

    heading_title_freq = df['n_count'].value_counts()

    sns.countplot(df, x='n_count')

    plt.show()