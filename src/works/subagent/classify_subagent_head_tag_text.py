import sys
sys.path.append('.')
import pandas as pd
from src.works.subagent.data.dao.subagent_heading_title_labeling_results_dao import subagentHeadingTitleLabelingResultsDao
from src.works.subagent.data.collections import col_subagent_file_with_heading_category
from src.works.subagent.data.collections import col_subagent_head_title_categories
from bson.objectid import ObjectId

def classify_func(head_tag_text_list, label_mapping : list[dict]) : 
    results = []
    for ht_text in head_tag_text_list : 
        if ht_text['head_tag'] == 'h1' or ht_text['head_tag'] == 'h2' : 
            text : str = ht_text['text'] 

            label = None
            for lm in label_mapping : 
                if text.lower() in lm['titles'] : 
                    label = lm['label']
                    break

            results.append(label)

    return results

label_category_names = [
    { 'name' : 'Input & Output', 'labels' : [0,1]}, 
    { 'name' : 'Objective', 'labels' : [2,3,4,5,6,7]},     
    { 'name' : 'Workflow', 'labels' : [8, 9]}, 
    { 'name' : 'Guideline', 'labels' : [10]}, 
    { 'name' : 'Reference', 'labels' : [12]}, 
    # { 'name' : 'Checklist', 'labels' : [13, 15]}, 
    # { 'name' : 'Rule', 'labels' : [14]}, 
    { 'name' : 'Constraint', 'labels' : [19, 20, 21, 22, 23, 24, 25]}, 
    { 'name' : 'Context', 'labels' : [16, 18, 26, 32, 34]}, 
    { 'name' : 'Capability', 'labels' : [27, 33, 35, 36, 37, 38, 39, 42]}
]

def merge_label(labels) : 
    results = []
    for label in labels : 
        for i in range(len(label_category_names)) : 
            if label in label_category_names[i]['labels'] : 
                results.append(i)

    return results

if __name__ == '__main__' : 
    in_file_path = 'E:/research_subagent/data/manual_analysis/heading_text_categorization_work/subagent_head_tag_text.json'
    df = pd.read_json(in_file_path)

    label_mapping = subagentHeadingTitleLabelingResultsDao.get_text_label_mapping_data().to_list()

    df['head_title_labels'] = df['head_tag_text'].apply(classify_func, [label_mapping])    
    df['label_category'] = df['head_title_labels'].apply(merge_label)
    
    label_category_names = [
        { 'id' : id, 'name' : label_categories['name'] } for id, label_categories in enumerate(label_category_names)
    ]
    col_subagent_head_title_categories.delete_many({})
    col_subagent_head_title_categories.insert_many(label_category_names)

    df['_id'] = df['_id'].apply(lambda x : ObjectId(x['$oid']))
    data = df.to_dict(orient='records')
    col_subagent_file_with_heading_category.delete_many({})
    col_subagent_file_with_heading_category.insert_many(data)
