from src.dataset.aiAgent.dao.exp_issues_dao import expIssuesDao
from src.dataset.aiAgent.dao.exp_pr_dao import expPRDao
from src.tools.file_classifier import SimpleFileClassifier
import pandas as pd
import numpy as np

def transform_issue_label_category(x) : 
    if isinstance(x, list) : 
        return x[0]
    else : 
        if x in ['Skill' ] : 
            return 'Doc'
        return x

def prepare_exp_issue_dataset() : 
    ds = expIssuesDao.get_dataset()  

    class_labels = {
        'SourceFile' : ['ts', 'py', 'tsx', 'rs', 'js', 'cs', 'go', 'css', 'html', 'ipynb', 'jsx', 'sh']
    }
    simple_classifier = SimpleFileClassifier(class_labels)

    temp_ds = []
    for d in ds : 
        len_body = 0
        if d['body'] : 
            len_body = len(d['body'])
        d['len_body'] = len_body

        total_changed_files = 0
        changed_source_files = 0        
        for commit in d['commits'] : 
            total_changed_files += len(commit)
            for file in commit : 
                name = file['filename']            
                file_ext = name.split('.')[-1]
                file_label = simple_classifier.classify(file_ext)
                if file_label == 'SourceFile' : 
                    changed_source_files += 1
        d['code_change_rate'] = 0
        if total_changed_files != 0 : 
            d['code_change_rate'] = changed_source_files / total_changed_files

        temp_ds.append(d)

    df = pd.DataFrame(temp_ds)    
    df['label_category'] = df['label'].apply(lambda x : transform_issue_label_category(x))
    df['n_changed_lines'] = df['n_additions'] + df['n_deletions']
    df['log_closed_hour'] = np.log1p(df['closed_hour'])
    df['log_n_comments'] = np.log1p(df['n_comments'])
    df['log_n_pr_comments'] = np.log1p(df['n_pr_comments'])
    df['log_n_review_comments'] = np.log1p(df['n_review_comments'])
    df['log_n_commits'] = np.log1p(df['n_commits'])    
    df['log_n_changed_files'] = np.log1p(df['n_changed_files'])    
    df['log_n_changed_lines'] = np.log1p(df['n_changed_lines'])
    df['log_body_len'] = np.log1p(df['len_body'])
    df['assignee'] = df['assignee'].apply(lambda x : True if x is not None else False )
    
    return df

def prepare_exp_pr_dataset() : 
    ds = expPRDao.get_dataset()  

    temp_ds = []
    for d in ds : 
        len_body = 0
        if d['body'] : 
            len_body = len(d['body'])
        d['len_body'] = len_body

        temp_ds.append(d)

    df = pd.DataFrame(temp_ds)    
    # df['label_category'] = df['label'].apply(lambda x : transform_issue_label_category(x))
    df['n_changed_lines'] = df['n_additions'] + df['n_deletions']
    df['log_closed_time'] = np.log1p(df['closed_time'])
    df['log_n_comments'] = np.log1p(df['n_comments'])
    df['log_n_review_comments'] = np.log1p(df['n_review_comments'])
    df['log_n_commits'] = np.log1p(df['n_commits'])    
    df['log_n_changed_files'] = np.log1p(df['n_changed_files'])    
    df['log_n_changed_lines'] = np.log1p(df['n_changed_lines'])
    df['log_body_len'] = np.log1p(df['len_body'])
    df['assignee'] = df['assignee'].apply(lambda x : True if x is not None else False )

    return df