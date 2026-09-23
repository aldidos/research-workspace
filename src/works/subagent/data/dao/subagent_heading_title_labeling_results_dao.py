from src.database.agg_stages import lookup, match, project, unwind, group, sort
from src.works.subagent.data.collections import col_subagent_heading_title_labeling_results

class SubagentHeadingTitleLabelingResultsDao :     

    def get_text_label_mapping_data(self) : 
        stages = [
            unwind('$label'), 
            group('$label', 'titles', {'$addToSet' : '$head_title'}), 
            project({
                '_id' : 0, 
                'label' : '$_id',
                'titles' : 1
            })
        ]

        return col_subagent_heading_title_labeling_results.aggregate(stages)

    def get(self) : 
        return col_subagent_heading_title_labeling_results.find()

    def remove_all(self) : 
        col_subagent_heading_title_labeling_results.delete_many({})
    
    def add(self, dataset) : 
        col_subagent_heading_title_labeling_results.insert_many(dataset)

subagentHeadingTitleLabelingResultsDao = SubagentHeadingTitleLabelingResultsDao()