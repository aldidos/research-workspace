import sys
sys.path.append('.')
import pandas as pd
from wordcloud import WordCloud

class WordProcessing : 

    def join_words(word_lists : list[list[str]]) -> dict : 
        return [ { 'text' : ' '.join(word_list) } for word_list in word_lists ]

    def compute_words_count(word_lists : list[list[str]]) -> list :  
        words = []
        [ words.extend(word_list) for word_list in word_lists]
        ser = pd.Series(words)
        temp_words_count = ser.value_counts()    
        words_count = [ {'word' : w, 'count' : c } for w, c in temp_words_count.items() ]
        words_count.sort(key = lambda x : x['count'], reverse = True)
        return words_count
    
    def generate_wordcloud(text) : ####
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        return wordcloud    
    
def main() : 
    word_lists = [
        ['aaa', 'bbb', 'ccc','aaa', 'bbb','aaa', 'bbb','bbb','bbb']
    ]
    text = WordProcessing.join_words(word_lists)
    word_counts = WordProcessing.compute_words_count(word_lists)

    print(text)
    print(word_counts)

if __name__ == '__main__' : 
    main()