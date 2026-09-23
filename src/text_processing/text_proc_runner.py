import sys
sys.path.append('.')
from src.text_processing.text_proc_factory import TextProcFactory
from src.text_processing.text_processor import TextProcessor
from src.util.data_file_rw import DataFileReader, DataFileWriter
from src.text_processing.word_processing import WordProcessing

def main() : 
    file_dir = f'e:/research_subagent/data' ####
    output_dir = f'e:/research_subagent/data' ####   
    file_names = ['study_subagent.subagent_file_text']  ####
    stop_words = ['md', 'agent', 'AGENTS', 'CLAUDE', 'README'] ####    
    k = 40 ####    
    text_field = 'file_name' ####
    delimiter = '.'
    
    # text_proc : TextProcessor = TextProcFactory.create_default_proc(stop_words) ####
    text_proc : TextProcessor = TextProcFactory.create_file_name_proc(stop_words, delimiter) ####

    for file_name in file_names : 
        corpus = DataFileReader.from_json(f'{file_dir}/{file_name}.json')        
        text_set = [ [d[text_field]] for d in corpus if d[text_field] is not None ]        

        word_lists = text_proc.run_processing(text_set)

        result_preproced = WordProcessing.join_words(word_lists)
        word_counts = WordProcessing.compute_words_count(word_lists)
        top_k_words = word_counts[0:k]
    
        DataFileWriter.to_json(f'{output_dir}/{file_name}_{text_field}_preproced.json', result_preproced)
        DataFileWriter.to_json(f'{output_dir}/{file_name}_{text_field}_word_counts.json', word_counts)
        DataFileWriter.to_json(f'{output_dir}/{file_name}_{text_field}_top_k_words.json', top_k_words)

if __name__ == '__main__' : 
    main()