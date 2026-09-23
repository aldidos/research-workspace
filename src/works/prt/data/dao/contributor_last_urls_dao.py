import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_contributor_last_urls
from src.database.agg_stages import lookup, unwind, match, project, Set
from src.works.prt.data.dao.exp_dataset_dao import expDatasetDao
import pandas as pd
from util.data_file_rw import DataFileReader

class ContributorLastUrlsDao : 

    def __init__(self) : 
        self.col = col_contributor_last_urls

    def get(self, repo_id_list) : 
        stages = [
            match({ 
                'response_status_code' : 200, 
                'repo_id' : {'$in' : repo_id_list}
                }),                        
            project({
                    '_id' : 0,
                    'repo_id' : 1,
                    'repo_name' : { '$concat' : [ '$owner', '/', '$name' ] }, 
                    'page' : '$n_page'
            })
        ]

        return self.col.aggregate(stages)
    
contriLastUrlsDao = ContributorLastUrlsDao()
    
if __name__ == '__main__' :     
    repo_id_list = [ data['id'] for data in expDatasetDao.get_dataset_with_contri_files()]
    df = pd.DataFrame( contriLastUrlsDao.get( repo_id_list ) ) 
    
    df.to_json('../data/exp_data/exp_repos_contributor_last_pages.json', orient='records')