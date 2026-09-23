import sys
sys.path.append('.')
import pandas as pd
from pathlib import Path
from src.dataset.aiConfig.collections import col_repos, col_subagents

dir_path = 'e:/research_dataset/ai-config_dataset'

cols = [col_repos, col_subagents]
csv_file_names = ['repos', 'subagents']

# csv_files = Path('e:/research_dataset/ai-config_dataset').glob('**/*.csv')
# file_name = 'repos'

for i in range(len(cols)) : 
    df = pd.read_csv(f'{dir_path}/{csv_file_names[i]}.csv')
    cols[i].insert_many( df.to_dict('records') )
    # col_subagents.insert_many( df.to_dict('records') )

# for csv_file in csv_files : 
#     df = pd.read_csv(csv_file)
