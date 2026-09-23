import numpy as np
from collections import Counter
import re

def compute_entropy(d_type) : 
    # 2. 확률 분포 계산
    counts = Counter(d_type)
    total = sum(counts.values())
    probabilities = [count / total for count in counts.values()]
    # 3. Shannon Entropy 계산
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    return entropy

def calculate_layout_entropy(markdown_text):
    # 1. 마크다운 요소 정의 (정규표현식)
    patterns = {
        'header': r'^#+\s',
        'checklist': r'^\s*-\s*\[[\sX|x]\]',
        'list': r'^\s*[\*\+-]\s',
        'code_block': r'^```',
        'plain_text': r'^[A-Za-z0-9]'
    }
    
    lines = markdown_text.split('\n')
    line_types = []
    
    for line in lines:
        matched = False
        for name, pattern in patterns.items():
            if re.match(pattern, line.strip()):
                line_types.append(name)
                matched = True
                break
        if not matched and line.strip(): # 비어있지 않은 일반 라인
            line_types.append('plain_text')

    return compute_entropy(line_types)

if __name__ == '__main__' : 
    # 예시 템플릿 적용
    template_sample = """
## Description
Please include a summary of the change.
- [ ] Bug fix
- [ ] New feature

## Checklist
- [ ] I have performed a self-review
- [ ] My code follows the style guidelines
    """

    print(f"Layout Entropy Score: {calculate_layout_entropy(template_sample):.4f}")    