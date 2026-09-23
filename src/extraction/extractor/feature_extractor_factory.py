from src.extraction.extractor.md_doc_feature_extractor import MDDocFeatureExtractor
from src.extraction.extractor.prt_doc_feature_extractor import PRTFeatureExtractor
from src.extraction.extractor.subagent_feature_extractor import SubagentFeatureExtractor

class FeatureExtractorFactory :

    def create(doc_name, text_proc = None) : 
        if doc_name == 'pull_request_template' : 
            return PRTFeatureExtractor(text_proc)

        if doc_name == 'subagent' : 
            return SubagentFeatureExtractor(text_proc)

        return MDDocFeatureExtractor(text_proc)