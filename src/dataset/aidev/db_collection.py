from src.database.db_conn import mongo_client

db_aidev = mongo_client.aidev

col_all_repository = db_aidev.all_repository
col_all_pull_request = db_aidev.all_pull_request
col_all_user = db_aidev.all_user
col_human_pr_task_type = db_aidev.human_pr_task_type
col_human_pull_request = db_aidev.human_pull_request
col_issue = db_aidev.issue
col_pr_comments = db_aidev.pr_comments
col_pr_commit_details = db_aidev.pr_commit_details
col_pr_commits = db_aidev.pr_commits
col_pr_review_comments = db_aidev.pr_review_comments
col_pr_review_comments_v2 = db_aidev.pr_review_comments_v2
col_pr_reviews = db_aidev.pr_reviews
col_pr_task_type = db_aidev.pr_task_type
col_pr_timeline = db_aidev.pr_timeline
col_pull_request = db_aidev.pull_request
col_related_issue = db_aidev.related_issue
col_repository = db_aidev.repository
col_user = db_aidev.user
