import sys
sys.path.append('.')
from src.database.agg_stages import *
from src.works.subagent.data.collections import col_subagent_categories

class SubagentCategoriesDao : 

    def get_undefined_id(self) : 
        doc = col_subagent_categories.find_one({'name' : 'Undefined'})
        return doc['id']

subagentCategoriesDao = SubagentCategoriesDao() 