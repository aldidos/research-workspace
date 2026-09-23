import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_repositories
import pandas as pd
from src.database.agg_stages import Set, project

class RepoDao : 

    def __init__(self) : 
        self.col = col_repositories

    def get_all_data(self) : 
        stages = [            
            project({
                    '_id' : 0,
                    'id' : 1,
                    'full_name' : 1,
                    'stargazers_count' : 1, 
                    'watchers_count' : 1, 
                    'forks_count' : 1
            })
        ]
        
        cur = col_repositories.aggregate(stages)
        return cur
    
if __name__ == '__main__' : 
    dao = RepoDao()
    df = pd.DataFrame( dao.get_all_data() ) 
    df.to_json('../data/repo_dataset.json', orient='records')