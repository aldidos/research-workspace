import re

def search_word(text, word) : 
    mat = re.search(word, text)
    if mat : 
        return True
    return False    

def search_word_categories(check_words : list[str], word_categories : dict ) :  ####
        results = { w_category['category'] : False for w_category in word_categories }

        for check_word in check_words : 
            c_word = check_word.lower()

            for wc in word_categories : 
                cate = wc['category']                            
                has_word = False
                for t_words in wc['words'] : 
                    if search_word(c_word, t_words) : 
                        has_word = True
                        results[ cate ] = has_word
                        break
                if has_word :
                    break        
      
        return results