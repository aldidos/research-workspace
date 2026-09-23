from src.works.subagent.data.collections import col_subagent_file_text
from bson.objectid import ObjectId

class SubagentFileTextDao  :

    def find_by_id(self, _id_strs) : 
        _id_objs = [ ObjectId(_id_str) for _id_str in _id_strs ]
        return col_subagent_file_text.find({
            '_id' : {'$in' : _id_objs}
        })

subagentFileTextDao = SubagentFileTextDao()