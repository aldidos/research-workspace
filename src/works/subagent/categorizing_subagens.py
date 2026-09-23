import sys
sys.path.append('.')
from src.works.subagent.data.collections import col_subagent_file_with_category
from src.works.subagent.data.collections import col_subagent_categories
from src.works.subagent.data.collections import col_subagent_labeling_reulsts
from bson.objectid import ObjectId
import pandas as pd

subagent_category_name_labels = [
    { 'name' : 'Code Review', 'labels' : [1] }, 
    { 'name' : 'QA', 'labels' : [2, 11, 19] }, 
    { 'name' : 'Testing', 'labels' : [3, 4, 5] }, 
    { 'name' : 'Engineering', 'labels' : [6] }, 
    { 'name' : 'Documentation', 'labels' : [7] }, 
    { 'name' : 'Architecture', 'labels' : [8] }, 
    { 'name' : 'CI/CD', 'labels' : [9] },      
    { 'name' : 'Security', 'labels' : [10] },          
    { 'name' : 'Dependency management', 'labels' : [12] },    
    { 'name' : 'Codebase analysis', 'labels' : [14] },    
    { 'name' : 'Planning', 'labels' : [17, 22] },    
    { 'name' : 'Domain-specific', 'labels' : [21] },    
    { 'name' : 'Release', 'labels' : [13, 18, 20] },
    { 'name' : 'Coordinator', 'labels' : [0, 15] },
    { 'name' : 'Undefined', 'labels' : [16] },    
]

def category_transform(category_list) : 
    for category_id, categories in enumerate(subagent_category_name_labels) :          
        if any( n in categories['labels'] for n in category_list) : # if category list has '0'(undefined), 
            return category_id    

if __name__ == '__main__' : 
    # file_path = 'E:/research_subagent/data/analysis/study_subagent.subagent_labeling_results_new.json'
    # df = pd.read_json(file_path)
    df = pd.DataFrame(col_subagent_labeling_reulsts.find())
    df['category'] = df['labels'].apply(category_transform) 

    subagent_category = [ { 'id' : id, 'name' : name_labels['name'], 'labels' : name_labels['labels'] } for id, name_labels in enumerate(subagent_category_name_labels) ]
    col_subagent_categories.delete_many({})
    col_subagent_categories.insert_many(subagent_category)

    # df['_id'] = df['_id'].apply(lambda x : ObjectId(x['$oid']))

    col_subagent_file_with_category.delete_many({})
    col_subagent_file_with_category.insert_many(df.to_dict(orient='records'))
    