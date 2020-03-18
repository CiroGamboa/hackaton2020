# -*- coding: utf-8 -*-
# 2 challenge of magneto hackaton 2020
# writing by fabiohernandezr10@gmail.com
# alvarojhr96@gmail.com
# cirossj10@hotmail.com
 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import load_model
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
class longShortMemory:
    def __init__(self,Json,x_data,y_data):
        self.numberOfNeurons=Json["LSTM"]["numberOfNeurons"]
        self.numberOfLayers= Json["LSTM"]["numberOfLayers"]
        self.testSize= Json["LSTM"]["test_size"]
        self.lookBack = Json["LSTM"]["look_back"]
        self.modelName = Json["LSTM"]["model_name"]
        self.numberOfFeatures = Json["LSTM"]["number_features"]
        self.x_data=x_data
        self.y_data=y_data
        
    def preprocessing(self):
        #self.x_data.reshape((-1,1))
        
        split_percent = 1-self.testSize
        split = int(split_percent*len(self.x_data))
        self.y_data=pd.to_datetime(self.y_data)
        trace = go.Scatter(
        x = self.y_data,
        y =self.x_data,
        mode = 'lines',
        name = 'Data'
        )
        layout = go.Layout(
        title = "",
        xaxis = {'title' : "Date"},
        yaxis = {'title' : "Close (Dollars)"}
        )
        fig = go.Figure(data=[trace], layout=layout)
        plotly.offline.plot(fig,  filename="inputData.html")
        x_train= self.x_data[:split] 
        y_train= self.y_data[:split] 
        x_test= self.x_data[split:]
        y_test=self.y_data[split:]
        return (x_train,y_train,x_test,y_test)
    
    def save_model(self,model):
        model.save(self.modelName)
    def load_model(self):
        model = load_model(self.modelName)
        return model
    def train(self,x_train,y_train):        
        x_train = x_train.reshape((len(x_train),self.numberOfFeatures))        
        train_generator = TimeseriesGenerator(x_train, x_train, length=self.lookBack, batch_size=100)  
        model = Sequential()
        model.add(
            LSTM(self.numberOfNeurons,
                activation='relu',
                input_shape=(self.lookBack,1))
        )
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')        
        num_epochs =50
        model.fit_generator(train_generator, epochs=num_epochs, verbose=1)
        print("entrenado")
        return model
        
    def test(self,x_test,y_test,model):    
        x_test = x_test.reshape((len(x_test),self.numberOfFeatures))        
        test_generator = TimeseriesGenerator(x_test, x_test, length=self.lookBack, batch_size=1)
        prediction =  model.predict_generator(test_generator)
        return prediction
    
    def graphic(self,close_train,close_test,prediction,date_train,date_test):
        close_train = close_train.reshape((-1))
        close_test = close_test.reshape((-1))
        prediction = prediction.reshape((-1))
        
        trace1 = go.Scatter(
            x = date_train,
            y = close_train,
            mode = 'lines',
            name = 'Data'
        )
        trace2 = go.Scatter(
            x = date_test,
            y = prediction,
            mode = 'lines',
            name = 'Prediction'
        )
        trace3 = go.Scatter(
            x = date_test,
            y = close_test,
            mode='lines',
            name = 'test_data'
        )
        layout = go.Layout(
            title = "TRM Dolar",
            xaxis = {'title' : "Date"},
            yaxis = {'title' : "COP"}
        )
        fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
        plotly.offline.plot(fig,  filename="testData.html")
  
    def predict(self,num_prediction,model,x_train,y_train):
        prediction_list = x_train[-self.lookBack:]
        for _ in range(num_prediction):
           x = prediction_list[-self.lookBack:]
           x = x.reshape((1, self.lookBack, 1))
           out = model.predict(x)[0][0]
           prediction_list = np.append(prediction_list, out)
       prediction_list = prediction_list[self.lookBack-1:]
       return prediction_list
   
    def predict_dates(self,num_prediction):
        
    
    
