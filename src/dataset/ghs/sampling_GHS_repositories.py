import sys
sys.path.append('.')
from util.data_file_rw import  DataFileReader
import pandas as pd

if __name__ == '__main__' : 
    repos = DataFileReader.from_csv('E:/GHS dataset/repositories-2021-03-08.csv')
    repos = [ repo for repo in repos if repo['is_fork_project'] == 'false']

    results = [ { 'name'  : repo['name'] } for repo in repos ]

    n_samples = 1000
    df = pd.DataFrame(results)
    samples = df.sample(n_samples)

    samples.to_json('../data/GHS_repo_samples_2.json', orient = 'records')