import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

class NeuralNetwork:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.num_classes, activation='softmax'))
        model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, min_delta=0.001)
        model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True, mode='min')
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, callbacks=[early_stopping, model_checkpoint])

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        return self.model.predict(X)

class RecurrentNeuralNetwork(NeuralNetwork):
    def __init__(self, input_shape, num_classes, sequence_length):
        super().__init__(input_shape, num_classes)
        self.sequence_length = sequence_length
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(tf.keras.layers.LSTM(128, input_shape=(self.sequence_length, self.input_shape[1])))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.num_classes, activation='softmax'))
        model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
        return model

class Autoencoder(NeuralNetwork):
    def __init__(self, input_shape):
        super().__init__(input_shape, input_shape)
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(128, activation='relu', input_shape=self.input_shape))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.input_shape[1], activation='sigmoid'))
        model.compile(optimizer=Adam(lr=0.001), loss='mean_squared_error')
        return model
