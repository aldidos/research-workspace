import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.task.proc_task_runner import ProcTaskRunner
from src.util.data_file_rw import DataFileReader, DataFileWriter
from src.extraction.extractor.subagent_feature_extractor import SubagentFeatureExtractor
from src.extraction.extractor.feature_extractor_factory import FeatureExtractorFactory
from src.text_processing.text_processor import TextProcessor
from src.text_processing.text_proc_factory import TextProcFactory
import pandas as pd

class SubagentFERunner : 
    def __init__(self, extractor : SubagentFeatureExtractor) : 
        self.extractor = extractor

    def _excute(self, doc_id, text) : 
        features_info = self.extractor.extract(text)
        features_info['_id'] = doc_id

        return features_info

    def run(self, args) : 
        runner = ProcTaskRunner()
        results = runner.run(self._excute, args)

        return results

def main() : 
    in_file_path = 'E:/research_subagent/data/study_subagent.subagent_file_text.json'  ####
    out_file_path = 'E:/research_subagent/data/study_subagent.subagent_file_text_fe.json' ####
    doc_type = 'subagent' ####
    doc_id = '_id'

    text_proc = TextProcFactory.create_default_proc([])
    extractor = FeatureExtractorFactory.create(doc_type, text_proc)
    # dataset = DataFileReader.from_json(in_file_path)
    df = pd.read_json(in_file_path)
    text_set = [ [row[doc_id], row['text']] for idx, row in df.iterrows() ]
    
    runner = SubagentFERunner(extractor)
    results = runner.run(text_set)

    pd.DataFrame(results).to_json(out_file_path, orient='records')    
    
if __name__ == '__main__' : 
    main()