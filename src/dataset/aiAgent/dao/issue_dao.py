from src.dataset.aiAgent.db_collection import col_issues
from src.database.agg_stages import unwind, match, project

class IssueDao : 

    def get_by_labels(self, label_names : list[str] ) : 
        stages = [
            {
                unwind('$lables'), 
                match({
                    'labels.name' : {
                        '$in' : label_names
                    }
                }),
                project({
                    '_id' : 0,
                    'id' : 1,
                    'title' : 1,
                    'body': 1,
                    'repo_id' : 1,
                    'number' : 1,
                    'label' : '$labels.name'
                })
            }
        ]

        return col_issues.aggregate(stages)