import sys
sys.path.append('.')
from src.works.prt.data.dao.exp_dataset_dao import expDatasetDao
from src.works.prt.data.db_collection import col_exp_dataset
    
if __name__ == '__main__' :     
    dataset = expDatasetDao.get_dataset_with_contri_files()
    col_exp_dataset.insert_many(dataset)    