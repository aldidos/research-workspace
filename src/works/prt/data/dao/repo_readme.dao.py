import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_readmes
from src.database.agg_stages import lookup, match, unwind, project, Set
import pandas as pd

class ReadmeDao : 

    def __init__(self) : 
        self.col = col_readmes

    def get_readme_download_urls(self) : 
        stages = [
            lookup('exp_dataset', 'repo_id', 'id', 'exp_repo'),
            match({
                '$expr' : { '$gte' : [ { '$size' : '$exp_repo'}, 1 ] }
            }),
            unwind('$exp_repo'),          
            project({
                '_id' : 0, 'id' : '$exp_repo.id', 'repo_name' : '$exp_repo.repo_name', 'file_path' : '$path', 'file_namt' : '$name', 'download_url' : 1
            })
        ]

        return self.col.aggregate(stages)

if __name__ == '__main__' : 
    dao = ReadmeDao()
    df = pd.DataFrame( dao.get_readme_download_urls() )
    df.to_json('../data/temp_readme_dl_urls.json', orient = 'records')