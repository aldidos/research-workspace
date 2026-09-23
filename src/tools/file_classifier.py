
class SimpleFileClassifier : 

    def __init__(self, class_labels) : 
        self.class_labels = class_labels

    def classify(self, file_ext) :         
        for cls, exts in self.class_labels.items() : 
            if file_ext in exts : 
                return cls        
        return 'Non'
    

if __name__ == '__main__' : 
    class_labels = {
        'SourceFile' : ['ts', 'py', 'tsx', 'rs', 'js', 'cs', 'go', 'css', 'html', 'ipynb', 'jsx', 'sh']
    }
    file_name = "packages/nx/src/ai/set-up-ai-agents/set-up-ai-agents.txt"
    file_ext = file_name.split('.')[-1]
    classifier = SimpleFileClassifier(class_labels)
    file_label = classifier.classify(file_ext)
    print(file_label)