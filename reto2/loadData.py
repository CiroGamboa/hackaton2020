# -*- coding: utf-8 -*-
# 2 challenge of magneto hackaton 2020
# writing by fabiohernandezr10@gmail.com
# alvarojhr96@gmail.com
# cirossj10@hotmail.com

import pandas as pd
import numpy as np
from datetime import timezone,datetime
class load_data:
    def __init__(self,Json):
        self.__copToUsdPath=Json["Paths"]["copToUsd"]
        self.__copToUsdPathCsv= Json["Paths"]["copToUsdCsv"]

    def load_dolar_data(self):
        cols=[0,1]
        dolar_dataset =pd.read_excel(self.__copToUsdPath,skiprows=7,encoding="cp1252",usecols=cols, sep='\t')
        dolar_dataset = dolar_dataset[:-4]
        
        #convert to numpy object
        #dolar_dataset = np.array(dolar_dataset)   
        #length = dolar_dataset.shape[0]-4
        
        #dolar_dataset  = dolar_dataset[0:length]
        # date to UnixTimeStamp     
        #for i  in range (0, length):
        #   dolar_dataset[i,0]=dolar_dataset[i,0].timestamp()      
        return dolar_dataset

