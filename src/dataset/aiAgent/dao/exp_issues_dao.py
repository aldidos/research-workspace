import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_exp_issues
from src.database.agg_stages import match, project, lookup
from src.database.exp_stat import expr, eq, array_element_at, get_field, date_diff, date_from_string, size, get_array_obj_field, gte

class ExpIssuesDao : 

    def get_dataset(self) : 
        stages = [                        
            lookup( 'issues', 'url', 'url', 'issue' ),  
            lookup( 'pull_requests', 'url', 'issue_url', 'pr' ), 
            # match( { '$expr' : eq( size('$labels'), 1 ), '$expr' : eq( size('$pr'), 1) }),
            match( { '$and': [ 
                # { 'labels': { '$size': 1 } }, 
                # { 'labels': { '$in': ["Config", 'Doc', 'MCP', 'Model', 'Prompt', 'Response', 'Skill', 'Token', 'Subagent', 'Streaming', 'Tool'] } },
                { '$expr' : eq( size('$pr'), 1) }
            ] }),
            lookup( 'pr_commits', 'pr.url', 'pr_url', 'pr_commits' ), 
            lookup( 'commits', 'pr_commits.url', 'url', 'commits' ), 
            project( {
                '_id' : 0, 
                'repo_id' : 1, 
                'body' : 1, 
                'label' : array_element_at('$labels', 0), 
                'closed_hour' : date_diff( 
                    date_from_string( get_array_obj_field('$issue', 0, 'created_at') ),
                    date_from_string( get_array_obj_field('$issue', 0, 'closed_at') ), 
                    'hour'
                    ), 
                'n_comments' : get_array_obj_field('$issue', 0, 'comments'), 
                'assignee' : get_array_obj_field('$issue', 0, 'assignee'), 
                'n_pr_comments' : get_array_obj_field('$pr', 0, 'comments'),                 
                'n_review_comments' : get_array_obj_field('$pr', 0, 'review_comments'), 
                'n_commits' : get_array_obj_field('$pr', 0, 'commits'), 
                'n_additions' : get_array_obj_field('$pr', 0, 'additions'), 
                'n_deletions' : get_array_obj_field('$pr', 0, 'deletions'), 
                'n_changed_files' : get_array_obj_field('$pr', 0, 'changed_files'), 
                'commits' : '$commits.files'
            } )
        ]

        return col_exp_issues.aggregate(stages)
    
expIssuesDao = ExpIssuesDao()

if __name__ == '__main__' : 
    cur = expIssuesDao.get_dataset()
    dataset = [ doc for doc in cur ]
    print( len(dataset))
