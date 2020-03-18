# -*- coding: utf-8 -*-
# 2 challenge of magneto hackaton 2020
# writing by fabiohernandezr10@gmail.com
# alvarojhr96@gmail.com
# cirossj10@hotmail.com
import requests, json
from loadData import load_data
import pandas as pd  
from netLSTM import longShortMemory
configFile="config.json"

with open(configFile) as f:
        data = json.load(f)#data is the configuration file 
#train routine        
ld= load_data(data) #define class to load data
dolarData=ld.load_dolar_data() #loading dolar data 
lstm = longShortMemory(data,dolarData['Tasa de cambio representativa del mercado (TRM)'].values,dolarData['Fecha (dd/mm/aaaa)'].values)#define class to train ML model
x_train,y_train,x_test,y_test=lstm.preprocessing() # preprocessing the input data
#model=lstm.train(x_train,y_train) #training ML model 
#lstm.save_model(model) #saving the model trained
model = lstm.load_model() #load  the model
predict=lstm.test(x_test,y_test,model)#testing ML model
                              #printing results and metrics
#graphic model
                              
lstm.graphic(x_train,x_test,predict,y_train,y_test)
 
#Forecasting
