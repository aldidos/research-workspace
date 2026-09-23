import sys
sys.path.append('.')
from src.works.subagent.data.dao.subagent_file_text_dao import subagentFileTextDao
import pandas as pd
from pathlib import Path

if __name__ == '__main__' : 
    _id_list = [
        "6a929ac1fe49adfd31deec2f",
        "6a929ac1fe49adfd31deec0b",
        "6a929ac1fe49adfd31deec62",
        "6a929ac1fe49adfd31deec29",
        "6a929ac1fe49adfd31deec6a",
        "6a929ac1fe49adfd31deec63",
        "6a929ac1fe49adfd31deec25",
        "6a929ac1fe49adfd31deecc7",
        "6a929ac1fe49adfd31deef37",
        "6a929ac1fe49adfd31deec27",
        "6a929ac1fe49adfd31deedb8",
        "6a929ac1fe49adfd31deec2d",
        "6a929ac1fe49adfd31deed87",
        "6a929ac1fe49adfd31deeca1",
        "6a929ac1fe49adfd31deecf5",
        "6a929ac1fe49adfd31deed5f",
        "6a929ac1fe49adfd31deec77"
    ]    

    df = pd.DataFrame(subagentFileTextDao.find_by_id(_id_list))
    for idx, row in df.iterrows() :         
        Path(f'E:/research_subagent/data/analysis/example_subagent_file_text/{row["file_name"]}').write_text(row['text'], 'utf-8')
    