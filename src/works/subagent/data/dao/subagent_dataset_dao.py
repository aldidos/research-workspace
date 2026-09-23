from src.database.agg_stages import lookup, match, project, unwind, group, sort
from src.works.subagent.data.collections import col_subagent_file_text_fe, col_subagent_file_with_category

class SubagentDatasetDao :     

    def make_subagent_category_lookup(self, undefined_category) : 
        return lookup('subagent_file_with_category', '_id', '_id', 'category_info', [
                match({ 'category' : {'$not' : {'$eq' : undefined_category } } }), ####
                lookup('subagent_categories', 'category', 'id', 'suba_category_info'), 
                unwind('$suba_category_info')
            ] )

    def get_dataset_for_RQ2(self, undefined_category) : 
        stages = [
            self.make_subagent_category_lookup(undefined_category), 
            unwind('$category_info'), 
            lookup('subagent_fre_scores', '_id', '_id', 'fre_score' ),             
            unwind('$fre_score'), 
            project({
                '_id' : 0, 
                'n_words' : 1,
                'fre_score' : '$fre_score.fre_score',
                'h1' : '$num_tags.h1',
                'h2' : '$num_tags.h2',
                'h3' : '$num_tags.h3',
                'h4' : '$num_tags.h4',
                'h5' : '$num_tags.h5',
                'h6' : '$num_tags.h6', 
                'category' : '$category_info.suba_category_info.name', 
            })
        ]

        return col_subagent_file_text_fe.aggregate(stages)

    def get_dataset_for_RQ3(self, undefined_category) : 
        stages = [
            self.make_subagent_category_lookup(undefined_category), 
            unwind('$category_info'), 
            lookup('subagent_file_with_heading_category', '_id', '_id', 'heading_title_category', [ 
                project( {'label_category' : { '$setUnion' : [ '$label_category', [] ]} }),                 
                unwind('$label_category'), 
                lookup('subagent_head_title_categories', 'label_category', 'id', 'ht_label_info'), 
                unwind('$ht_label_info') 
            ] ), 
            unwind('$heading_title_category'),
            project({ 
                'subagent_category' : '$category_info.suba_category_info.name', 
                'ht_category' : '$heading_title_category.ht_label_info.name'
            })
        ]

        return col_subagent_file_text_fe.aggregate(stages)

    def get_subagent_category_distribution(self) : 
        stages = [
            lookup('subagent_categories', 'category', 'id', 'category_info'),
            unwind('$category_info'),
            group('$category_info.name', 'n_subagents', {'$count' : {}} ), 
            sort('n_subagents', -1)            
        ]

        return col_subagent_file_with_category.aggregate(stages)

subagentDatasetDao = SubagentDatasetDao()
