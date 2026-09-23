import sys
sys.path.append('.')
from src.works.subagent.data.dao.subagent_text_fe_dao import subagentTextFeDao
import pandas as pd

if __name__ == '__main__' : 
    dataset = subagentTextFeDao.get_()

    head_text = []
    for d in dataset : 
        for i in range(len(d['head_tag_text'])) : 
            if i == 0 : 
                continue
            h_tag = d['head_tag_text'][i]
            if h_tag['head_tag'] == 'h1' or h_tag['head_tag'] == 'h2' : 
                head_text.append({'h_text' : h_tag['text']})

    output_file_path = 'E:/research_subagent/data/analysis/subagent_head_text.json'
    pd.DataFrame(head_text).to_json(output_file_path, orient='records')