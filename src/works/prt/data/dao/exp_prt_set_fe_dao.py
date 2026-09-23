from src.works.prt.data.db_collection import col_exp_prt_set_fe
from src.database.agg_stages import project, lookup, unwind

class ExpPrtSetFe : 

    def get_dataset() : 
        stages = [
            lookup('repositories', 'repo_id', 'id', 'repo'),
            unwind('$repo'),
            project({
                '_id' : 0, 
                'id' : 1, 
                'n_heading' : '$tag_counts.heading',
                'n_list' : '$tag_counts.list',
                'n_listitem' : '$tag_counts.listitem',
                'n_link' : '$tag_counts.link',
                'n_code' : '$tag_counts.code',
                'n_table' : '$tag_counts.table',
                'has_desc' : '$heading_titles.Description',
                'has_test' : '$heading_titles.Testing',
                'has_checklist' : '$heading_titles.Checklist',
                'has_pr_type' : '$heading_titles.PR Type',
                'has_motiv' : '$heading_titles.Motivation',
                'n_words' : 1, 
                'n_checklist_items' : 1, 
                'n_comments' : 1, 
                'n_comment_size' : 1, 
                'popularity' : '$repo.stargazers_count'
            })
        ]

        return col_exp_prt_set_fe.aggregate(stages)
