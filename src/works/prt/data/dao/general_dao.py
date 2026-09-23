import sys
sys.path.append('.')
from src.database.agg_stages import unwind, match, project
from src.database.exp_stat import trim, toLower, eq, OR, map, IN
from src.works.prt.data.db_collection import col_pull_request_template_features

class GeneralDao : 

    def find_in_array_word(col, field, words) : 
        stages = [] 

        stages.append( project( {
            field : map(f'${field}', 'heading_text', 
                toLower( trim( f'$$heading_text.text') )
            )}
        ) )
        stages.append( match({             
            '$expr' : 
                OR([ IN(word, f'${field}' )  for word in words ])  
         }))
        
        return col.aggregate(stages)
