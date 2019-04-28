from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np
from keras.layers import Dense, Dropout, Activation, Flatten, Reshape
from keras.optimizers import SGD

K.set_image_data_format('channels_first')
K.image_data_format()


class CNN:
    def __init__(self, batch_size, nb_epoch):
        self.batch_size=batch_size
        self.nb_epoch=nb_epoch
        
    def trainingModel(self, X_train, y_train, X_test, y_test):
        # X_predict
        model = Sequential()#192=8*8*3, 192 matrice 8*8 en sortie correspond au filtre et 3*3 comment ils sont séparés
        
        model.add(Conv2D(128,kernel_size=(3, 3), padding='same', activation='relu',input_shape=(3,8,8)))# pas de vanish gradient                                                                                                #avec relu
        model.add(Dropout(0.25))
        
        model.add(Conv2D(64,kernel_size=(3, 3), padding='same', activation='relu'))
        
        model.add(Conv2D(32,kernel_size=(3, 3), padding='same',activation='relu'))
        model.add(Dropout(0.25))
        #model.add(Conv2D(64,kernel_size=(3, 3), padding='same',activation='relu'))
        #model.add(Dropout(0.25))
        #model.add(Conv2D(64,kernel_size=(3, 3), padding='same',activation='relu'))
        #model.add(Dropout(0.25))
        model.add(Conv2D(1,kernel_size=(3, 3), padding='same',activation='relu'))
        model.add(Dropout(0.25))
        
        model.add(Reshape((1,1,64)))
        model.add(Activation('softmax'))#une dimension
        model.add(Reshape((1,8,8)))
        model.compile(loss='mse',#minumum square error keras.losses.categorical_crossentropy, 
                      optimizer='adam', #technique de gradient descent stochastique (min globale)
                      metrics=['accuracy'])

        # batch_size = 128 #take 128 samples and train network
        # nb_epoch = 5 #propagation-backpropagation
        model.fit(X_train, y_train, batch_size=self.batch_size, epochs=self.nb_epoch, verbose=1,shuffle=True,validation_data=(X_test, y_test))
        score = model.evaluate(X_test, y_test, verbose=0)#mélanger les exemples de train
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
        return model