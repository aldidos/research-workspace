import sys
sys.path.append('.')
from src.works.subagent.title_classifier import TitleClassifier
from works.subagent.data.dao.subagent_heading_title_labeling_results_dao import col_subagent_heading_title_labeling_results
from src.works.subagent.data.collections import col_subagent_heading_title_counts
from src.works.subagent.data.collections import col_subagent_head_title_labels
from bson.objectid import ObjectId
import pandas as pd

if __name__ == '__main__' :     
    keywords_set = [
        ['input'], 
        ['output'], 

        ['role'],
        ['mission'],
        ['objective'], 
        ['goal'], 
        ['purpose'],

        ['responsibilit'],
        ['workflow'],
        ['process'],
        ['guideline'], 
        ['instruction'],
        ['reference'], 
        ['checklist'],            
        ['rule'],
        ['note'],
        ['outline'],
        ['summary'],
        ['overview'],

        ['constraint'],
        ["what you are not"],
        ["what not to do"],
        ["anti-examples: what not to do"],
        ["what you don't do"],
        ["what this does not do"],
        ["what you never do"],

        ['context'],
        ['capabilit'],
        ['criteria'],
        ['prerequisit'],
        ['approach'],
        ['principle'],
        ['scope'],
        ['behavior'],
        ['background'],

        ["what this agent does"],
        ["what you do"],
        ["what you do (and what you no longer do)"],

        ["how to work"],
        ["how you work"],
        ["problems this solves"],
        ["how to use"],
        ["your expertise"],
    ]

    df = pd.DataFrame(col_subagent_heading_title_counts.find())
    df['_id'] = df['_id'].apply(lambda x : ObjectId(x))

    kw_map = {
        order : keywords for order, keywords in enumerate(keywords_set)
    }

    head_title_labels = [
        {'id' : order, 'keyword' : keywords} for order, keywords in enumerate(keywords_set)
    ]
    col_subagent_head_title_labels.delete_many({})
    col_subagent_head_title_labels.insert_many(head_title_labels)

    classifier = TitleClassifier(kw_map)
    df['label'] = df['head_title'].apply(lambda x : classifier.classify_one(x.lower()) )

    ## label filtering
    df_filter_titles = pd.read_json('E:/research_subagent/data/manual_analysis/heading_text_categorization_work/filtering_head_titles.json')
    filters = df_filter_titles['filter_titles'].to_list()    
    for idx, row in df.iterrows() : 
        if str(row['_id']) in filters : 
            row['label'].clear()   

    col_subagent_heading_title_labeling_results.remove_all()
    col_subagent_heading_title_labeling_results.add(df.to_dict(orient='records'))
