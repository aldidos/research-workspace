import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_repositories
from src.database.agg_stages import lookup, unwind, match, project, Set, group
import pandas as pd

class ExpDatasetDao : 

    def __init__(self) : 
        self.col = col_repositories

    def get_dataset_with_contri_files(self) : 
        stages = [            
            match({
                    'archived' : False,
                }
            ),
            lookup('repo_contents', 'id', 'repo_id', 'contents', [ 
                match( { '$expr' : { '$eq' : [ { '$toLower' : '$name' }, 'contributing.md' ] } } ) 
                ] ),                        
            match({ 
                    '$expr' : {'$gte' : [ {'$size' : '$contents'}, 1 ] }
                }
            ),
            lookup('readmes', 'id', 'repo_id', 'readme' ),
            lookup('contributor_last_urls', 'id', 'repo_id', 'contributor_info', [
                project({ '_id' : 0, 'id' : 0 })
            ] ),  
            lookup('contributor_last', 'id', 'repo_id', 'contributor_last', [
                group('$repo_id', 'contributor_count', { '$count' : {} })
            ]),
            lookup('contributing_file_features', 'id', 'repo_id', 'contributing_file_features', [
               project({ '_id' : 0, 'tag_counts' : 1}) 
            ]),
            lookup('pull_request_last_urls', 'id', 'repo_id', 'pr_last_urls', [
                project({ 'n_page' : 1 })
            ] ),
            lookup('pull_requests_exp_01', 'id', 'repo_id', 'prs', [
                group('$repo_id', 'n_prs', { '$count' : {} })
            ] ),
            unwind('$readme'),
            unwind('$contributor_info'),
            unwind('$contributor_last'),
            unwind('$contributing_file_features'),
            unwind('$pr_last_urls'),
            unwind('$prs'),
            project({
                    '_id' : 0,
                    'id' : 1,
                    'repo_name' : '$full_name',
                    'stargazers_count' : 1,
                    'watchers_count' : 1,
                    'repo_size' : '$size',
                    'created_at' : { '$dateFromString' : {'dateString' : '$created_at'} },
                    'updated_at' : { '$dateFromString' : {'dateString' : '$updated_at'} },
                    'forks_count' : 1,
                    'language' : 1,
                    'contents' : 1,
                    'readme' : 1,
                    'contributor_info' : 1,                    
                    'n_topics' : { '$size' : '$topics' }, 
                    'contributing_file_size' : { '$sum' : '$contents.size'},
                    'n_contri_files' : { '$size' : '$contents.size' }, 
                    'readme_size' : '$readme.size',                    
                    'contributor_size' : '$contributor_info.n_page',                    
                    'n_contributors' : { '$multiply' : ['$contributor_info.n_page', '$contributor_last.contributor_count' ] }, #### 
                    'n_heading' : '$contributing_file_features.tag_counts.heading',
                    'n_list' : '$contributing_file_features.tag_counts.list',
                    'n_listitem' : '$contributing_file_features.tag_counts.listitem',
                    'n_link' : '$contributing_file_features.tag_counts.link',
                    'n_code' : '$contributing_file_features.tag_counts.code', 
                    'n_prs' : { '$multiply' : ['$pr_last_urls.n_page', '$prs.n_prs' ] }, 
                    'repo_active_year' : {
                        '$dateDiff' : {
                            'startDate' : { '$dateFromString' : {'dateString' : '$created_at'} },
                            'endDate' : { '$dateFromString' : {'dateString' : '$updated_at'} },
                            'unit' : 'year'
                        }
                    }
            })
        ]

        return self.col.aggregate(stages)
    
expDatasetDao = ExpDatasetDao()
    
if __name__ == '__main__' : 
    df = pd.DataFrame( expDatasetDao.get_dataset_with_contri_files() )     

    df_exp_repos = df[['id', 'repo_name']]
    df_exp_repos.to_json('../data/exp_data/exp_repos.json', orient='records')