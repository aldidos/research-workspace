import sys
sys.path.append('.')
from src.util.data_file_rw import DataFileReader, DataFileWriter
from src.docs.prt_doc import PRTDoc
from src.text_processing.text_proc_factory import TextProcFactory
from src.text_processing.text_processor import TextProcessor
from src.task.proc_task_runner import ProcTaskRunner

def task_func(id, prt_text, text_proc) : 
    info_feat = PRTDoc(prt_text, text_proc).compute_info_features()    

    return {
        'id' : id, 
        'word_ent' : info_feat[0], 
        'n_heading' : info_feat[1], 
        'size_checklist' : info_feat[2]
    }

def main() : 
    results = []

    methods = TextProcFactory.create_default_proc([]) ####    
    text_proc = TextProcessor(methods)

    dataset = DataFileReader.from_json('E:/research_pullreq_template_structure/data/exp_data/prt_text.json')

    task_args = [ ( id, d['text'], text_proc) for id, d in enumerate(dataset) ]
    task_runner = ProcTaskRunner()

    results = task_runner.run(task_func, task_args)    
    
    DataFileWriter.to_json('E:/research_pullreq_template_structure/data/exp_data/prt_text_info_feat.json', results)

if __name__ == '__main__' : 
    main()
