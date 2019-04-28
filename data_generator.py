import numpy as np
import pandas as pd

class ProcessCsvData:
    def __init__(self):
        pass
    def loadCsvData(self, file_path):
        try:
            file=open(file_path,'r')
        except:
            print('Error: not found the csv file')
        file_rows=file.readlines()
        nb_rows=len(file_rows)
        csv_data=np.zeros((nb_rows, 256), dtype=int)
        index=0
        for rows in file_rows:
            row_data=rows.strip().split(',')
            csv_data[index,:]=row_data[0:256]
            index+=1
        return csv_data
    
    def reshapeOneRowData(self, row_data):
        train_set=[]
        test_set=[]
        for i in range(len(row_data.reshape(4,8,8))-1):
            train_set.append(row_data.reshape(4,8,8)[i])
        test_set.append(row_data.reshape(4,8,8)[-1])
        return train_set, test_set
    
    def reshapeDataset(self, dataset):
        train_set=[]
        test_set=[]
        for i in range(np.shape(dataset)[0]):
            train, test=ProcessCsvData().reshapeOneRowData(dataset[i,:])
            train_set.append(train)
            test_set.append(test)
        return train_set, test_set
     
    def splitTrainTestSet(self, train_set, test_set):
        X=np.asarray(train_set)
        y=np.asarray(test_set)
        
        X_train=X[0:int(len(X)*0.95)]
        y_train=y[0:int(len(y)*0.95)]
        X_test=X[int(int(len(X)*0.95)):len(X)]
        y_test=y[int(len(y)*0.95):len(y)]
        
        return X_train, y_train, X_test, y_test
    
    
    