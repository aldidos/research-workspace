from src.database.agg_stages import lookup, match, project, unwind
from src.works.subagent.data.collections import col_subagent_file_text_fe

class SubagentTextFeDao : 

    def __init__(self) : 
        self.col = col_subagent_file_text_fe

    def get_(self) : 
        stages = [
            lookup('subagent_file_text', '_id', '_id', 'r', [ match({'text' : {'$regex' : '^---'}}) ])
        ]

        return self.col.aggregate(stages)

subagentTextFeDao = SubagentTextFeDao()
