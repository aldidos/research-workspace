from src.database.db_conn import mongo_client

raw_dataset_path = 'e:/research_ai_agent/data'

db_ai_agent = mongo_client.study_ai_agent

col_issues = db_ai_agent.issues
col_pull_requests = db_ai_agent.pull_requests
col_exp_issues = db_ai_agent.exp_issues
col_pr_commits = db_ai_agent.pr_commits
col_commits = db_ai_agent.commits
col_exp_prs = db_ai_agent.exp_prs
col_exp_agent_issues = db_ai_agent.exp_agent_issues