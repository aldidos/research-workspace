import sys
sys.path.append('.')
from src.works.subagent.data.collections import data_collections
from src.util.data_file_rw import DataFileWriter, DataFileReader
from bson.objectid import ObjectId
import pandas as pd

def migration_from(dir_path) : 
    for (name, col) in data_collections : 
        ds = [ d for d in col.find() ]
        DataFileWriter.to_json(f'{dir_path}/{name}.json', ds)

def migration_to(dir_path) : 
    for (name, col) in data_collections : 
        df = pd.read_json(f'{dir_path}/{name}.json')
        df['_id'] = df['_id'].apply(lambda x : ObjectId( x['$oid'] ))
        col.insert_many(df)

if __name__ == '__main__' : 
    direction = 'from'
    dir_path = 'e:/research_subagent/data/collection_backup'

    if direction == 'from' : 
        migration_from(dir_path)
    if direction == 'to' : 
        migration_to(dir_path)
