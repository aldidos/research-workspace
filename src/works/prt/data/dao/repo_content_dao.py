from src.works.prt.data.db_collection import col_repo_contents, col_repositories
from src.database.agg_stages import lookup, match, unwind, project, Set
import pandas as pd

class RepoContentDao : 

    def __init__(self) : 
        self.col = col_repo_contents

    def search_contents(self, names, content_type) : 
        stages = [
            lookup('repo_contents', 'id', 'repo_id', 'contents', [
                Set({ 'name_lower' : { '$toLower' : '$name' } }),
                match({ 'name_lower' : { '$in' : names }, 'type' : content_type})
            ]), 
            match({
                '$expr' : { '$gte' : [ {'$size' : '$contents'}, 1 ] }
             }),
            unwind('$contents'),            
            project({ 
                '_id' : 0, 'id' : 1, 'repo_name' : '$full_name', 'download_url' : '$contents.download_url', 'file_name' : '$contents.name', 'file_path' : '$contents.path'
            })
        ]

        return col_repositories.aggregate(stages)
    
    def search_contents_exp_repos(self, names, content_type) : 
        stages = [            
            lookup('exp_dataset', 'repo_id', 'id', 'exp_repos'), 
            Set({ 'name_lower' : { '$toLower' : '$name' } }),            
            match({
                'name_lower' : { '$in' : names }, 'type' : content_type,
                '$expr' : { '$gte' : [ {'$size' : '$exp_repos'}, 1 ] }
            }),
            unwind('$exp_repos'),            
            project({ 
                '_id' : 0, 'id' : '$repo_id', 'repo_name' : '$exp_repos.repo_name', 'download_url' : 1, 'file_name' : '$name', 'file_path' : '$path'
            })
        ]

        return self.col.aggregate(stages)
    
if __name__ == '__main__' :     
    search_file_name = 'pull_request_template.md' 
    file_type = 'file'

    dao = RepoContentDao()
    cur = dao.search_contents([search_file_name], file_type)
    df = pd.DataFrame(cur)    
    df.to_json(f'../data/dl_urls_{search_file_name}_temp.json', orient = 'records')