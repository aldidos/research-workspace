import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_issues
from src.database.agg_stages import unwind, match, project
import pandas as pd

class TextDataSetDao : 

    def get_issue_title_text_set(self, label_names : list[str] ) : 
        stages = [            
            match({
                'labels.name' : {
                    '$in' : label_names
                }
            }),          
            project({
                '_id' : 0,
                'text' : '$title'
            })
        ]

        return col_issues.aggregate(stages)
    
if __name__ == '__main__' : 
    dao = TextDataSetDao()
    label_names = ['agent-generated', 'area/agent', 'agentic-workflows', 'area:agents']        
    cur = dao.get_issue_title_text_set(label_names)

    df = pd.DataFrame(cur)
    print(df)

    df.to_json('E:/research_ai_agent/data/exp_data/issue_title_text.json', orient='records')