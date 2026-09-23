from src.database.db_conn import mongo_client

db_subagent = mongo_client.study_subagent

col_repositories = db_subagent.repositories
col_commits = db_subagent.commits
col_commit_detail = db_subagent.commit_detail
col_readme_contents = db_subagent.readme_contents
col_readme_files = db_subagent.readme_files
col_repo_contents = db_subagent.repo_contents
col_repos = db_subagent.repos

col_head_text = db_subagent.head_text
col_subagent_categories = db_subagent.subagent_categories
col_subagent_category_labels = db_subagent.subagent_category_labels

col_subagent_file_info = db_subagent.subagent_file_info
col_subagent_file_text = db_subagent.subagent_file_text
col_subagent_file_text_fe = db_subagent.subagent_file_text_fe
col_subagent_file_with_category = db_subagent.subagent_file_with_category
col_subagent_file_with_heading_category = db_subagent.subagent_file_with_heading_category
col_subagent_fre_scores = db_subagent.subagent_fre_scores

col_subagent_head_title_categories = db_subagent.subagent_head_title_categories
col_subagent_head_title_labels = db_subagent.subagent_head_title_labels
col_subagent_heading_title_counts = db_subagent.subagent_heading_title_counts

col_subagent_heading_title_labeling_results = db_subagent.subagent_heading_title_labeling_results
col_subagent_labeling_reulsts = db_subagent.subagent_labeling_results

data_collections = [
    ('col_repositories', col_repositories), 
    ('col_repos', col_repos), 
    ('col_commits', col_commits), 
    ('col_commit_detail', col_commit_detail), 
    ('col_readme_contents', col_readme_contents), 
    ('col_readme_files', col_readme_files), 
    ('col_repo_contents', col_repo_contents), 
    ('col_head_text', col_head_text),
    ('col_subagent_categories', col_subagent_categories), 
    ('col_subagent_file_info', col_subagent_file_info), 
    ('col_subagent_file_text', col_subagent_file_text),
    ('col_subagent_file_text_fe', col_subagent_file_text_fe),
    ('col_subagent_file_with_category', col_subagent_file_with_category),
    ('col_subagent_file_with_heading_category', col_subagent_file_with_heading_category),
    ('col_subagent_fre_scores', col_subagent_fre_scores),    
    ('col_subagent_head_title_categories', col_subagent_head_title_categories),
    ('col_subagent_head_title_labels', col_subagent_head_title_labels),
    ('col_subagent_heading_title_counts', col_subagent_heading_title_counts),
    ('col_subagent_heading_title_labeling_results', col_subagent_heading_title_labeling_results),
    ('col_subagent_labeling_reulsts', col_subagent_labeling_reulsts)
]