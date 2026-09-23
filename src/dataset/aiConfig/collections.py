from src.database.db_conn import mongo_client

raw_dataset_path = ''

db_ai_config = mongo_client.ai_config

col_repos = db_ai_config.repos
col_subagents = db_ai_config.subagents
