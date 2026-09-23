import frontmatter
import pandas as pd
import re

class TitleClassifier : 

    def __init__(self, keyword_map) : 
        self.keyword_map : dict = keyword_map

    def classify_one(self, title : str) : 
        classified_labels =[]
        for label, keywords in self.keyword_map.items() : 
            for keyword in keywords :
                mat = re.search(keyword, title)
                if mat : 
                    classified_labels.append(label)
        return classified_labels

    def classify(self, titles : list[str]) : 
        results = []
        for title in titles : 
            labels = self.classify_one( title.lower() )
            results.append({ 
                'title' : title, 
                'lable' : labels
             })
        return results


if __name__ == '__main__' : 
    kw_map = {
        1 : ['input']
    }
    classifier = TitleClassifier(kw_map)
    results = classifier.classify(['Input', 'Output', 'Rule'])
    print(results)
