import sys
sys.path.append('.')
import pandas as pd
import src.dataset.aidev.db_collection as aidev
from src.util.data_file_rw import DataFileWriter

data_file_name = [ 'all_repository.parquet' ]
cols = [ aidev.col_all_repository ]
# data_file_name = [ 'all_repository.parquet', 'all_user.parquet', 'human_pr_task_type.parquet', 'human_pull_request.parquet', 'issue.parquet', 'pr_comments.parquet', 
#                   'pr_commit_details.parquet', 'pr_commits.parquet', 'pr_review_comments.parquet', 'pr_review_comments_v2.parquet', 'pr_reviews.parquet', 'pr_task_type.parquet', 
#                    'pr_timeline.parquet', 'pull_request.parquet', 'related_issue.parquet', 'repository.parquet', 'user.parquet' ]
# cols = [ aidev.col_all_repository, aidev.col_all_repository, aidev.col_all_user, aidev.col_human_pr_task_type, aidev.col_human_pull_request, aidev.col_issue, aidev.col_pr_comments, 
#              aidev.col_pr_commit_details, aidev.col_pr_commits, aidev.col_pr_review_comments, aidev.col_pr_review_comments_v2, aidev.col_pr_reviews, aidev.col_pr_task_type, 
#               aidev.col_pr_timeline, aidev.col_pull_request, aidev.col_related_issue, aidev.col_repository, aidev.col_user ]
target_path = 'E:/research_ai_agent/AIDev'
N = len(data_file_name)

for i in range(N) : 
    try : 
        df = pd.read_parquet(f'{target_path}/{data_file_name[i]}')
        subdf = df[['id', 'full_name', 'url', 'language', 'forks', 'stars']]
        subdf.to_json('e:/research_ai_agent/data/all_repositories.json', orient = 'records')        
        cols[i].insert_many( subdf.to_dict('records'), ordered=False )            
    except Exception as e : 
        print(e)

    print(data_file_name[i])