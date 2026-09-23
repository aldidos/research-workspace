import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.task.proc_task_runner import ProcTaskRunner
from src.util.data_file_rw import DataFileReader, DataFileWriter
from src.extraction.extractor.md_doc_feature_extractor import MDDocFeatureExtractor
from src.extraction.extractor.feature_extractor_factory import FeatureExtractorFactory
from src.text_processing.text_processor import TextProcessor
from src.text_processing.text_proc_factory import TextProcFactory
import pandas as pd

class MDDocFERunner : 
    ''''Markdown Text Feature Extraction Runner'''
    
    def __init__(self, extractor : MDDocFeatureExtractor) : 
        self.extractor = extractor

    def _excute(self, doc_id, text) : 
        r = self.extractor.extract(text)
        r['doc_id'] = doc_id

        return r

    def run(self, args) : 
        runner = ProcTaskRunner()
        results = runner.run(self._excute, args)

        return results

def main() : 
    in_file_path = 'E:/research_subagent/data/study_subagent.subagents_content.json'  ####
    out_file_path = 'E:/research_subagent/data/subagent_contents_fe.json' ####
    doc_name = '' ####
    doc_id = '_id'

    # categories = ['Description', 'Testing', 'Checklist', 'PR Type', 'Motivation']
    categories = []
    words = [['desc', 'summary', 'overview'], ['test'], ['checklist'], ['type'], ['motivati']]
    # checking_heading_titles = [ 
    #     { 'category' : categories[i], 'words' : words[i] }for i in range(len(categories)) 
    # ]
    checking_heading_titles = []

    text_proc = TextProcFactory.create_default_proc([])
    extractor = FeatureExtractorFactory.create(doc_name, text_proc)
    dataset = DataFileReader.from_json(in_file_path)
    text_set = [ [ data[doc_id], data['text']] for data in dataset ]
    
    runner = MDDocFERunner(extractor)
    results = runner.run(text_set)

    # temp_results = []
    # for i in range(len(dataset)) : 
    #     temp_results.append({
    #         '_id' : dataset[i][doc_id],
    #         'feature' : results[i]
    #     })

    DataFileWriter.to_json(out_file_path, results)     
    
if __name__ == '__main__' : 
    main()