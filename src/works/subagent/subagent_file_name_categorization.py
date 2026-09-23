import sys
sys.path.append('.')
from src.util.data_file_rw import DataFileReader, DataFileWriter
import pandas as pd

# Refined classification function
def classify(name):
    n = name.lower()
    # 1. Code Review
    # 2. Quality assurence    
    # 3. Test    
    # 4. Debugging    
    # 5. Issue    
    # 6. Development & Implementation
    # 7. Documentation    
    # 8. Architecture & System Design    
    # 9. CI/CD    
    # 10. Security    
    # 11. Compliance    
    # 12. Dependency Management    
    # 13. Project Management / Specific perpose
    # 14. Codebase Analysis    
    # Misclassification
    # Undefined
    # Research

    keywords = [
        ['code-review', 'reviewer', 'pr-reviewer'],
        ['quality', 'audit', 'auditor', 'lint', 'linter', 'clean-code', 'readability', 'fidelity', 'code-quality-checker'],
        ['test', 'tester', 'testing', 'playwright', 'vitest', 'unittest', 'e2e', 'bdd', 'mockup'],
        ['debug', 'debugger', 'fix', 'fixer', 'healer', 'troubleshooter', 'crash'],
        ['issue', 'triage', 'triager', 'track-issue', 'plan-issue', 'bug-hunter', 'bug'],
        ['coder', 'developer', 'builder', 'implementer', 'implementation', 'expert', 'engineer', 'frontend', 'backend'],
        ['docs', 'doc', 'documentation', 'readme', 'writer', 'changelog', 'doxygen', 'notes'],
        ['architect', 'architecture', 'design', 'structure', 'pattern', 'schema', 'model'],
        ['ci', 'workflow'],
        ['security', 'vulnerability', 'cve', 'safe', 'safety', 'audit'],
        ['compliance', 'compliant', 'scorm', 'policy', 'standards', 'constitution', 'code-standards-enforcer'],
        ['dependency', 'dependencies', 'updater', 'bump', 'version', 'upgrade'],
        ['manager', 'management', 'planner', 'grooming', 'coordinator', 'product-owner', 'tusk'],
        ['analyzer', 'analysis', 'locator', 'search', 'explorer', 'scanner', 'auditor', 'metrics']
    ]
    categories = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    result = []

    for i in range(len(categories)) : 
        if any(k in n for k in keywords[i]):
            # return 1
            result.append( categories[i] )

    # return 15
    return result

if __name__ == '__main__' : 
    dir = 'E:/research_subagent/data/'####
    filename = 'study_subagent.subagent_file_text'
    file_path = f'{dir}/{filename}.json'
    df = pd.read_json(file_path)
    sub_df = df[['_id', 'file_name']]

    final_mapping = []
    for idx, row in sub_df.iterrows():
        cat = classify(row['file_name'])
        final_mapping.append({
            '_id' : row['_id'],
            'name' : row['file_name'], 
            'category' : cat
        })
        
    df = pd.DataFrame(final_mapping)
    output_file_name = 'subagent_categorization_result.json'
    df.to_json(f'{dir}/{output_file_name}', orient='records') 