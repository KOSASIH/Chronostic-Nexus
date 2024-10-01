import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

class NeuralNetwork:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(128, activation='relu'),
            Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

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
        model = tf.keras.models.Sequential([
            tf.keras.layers.LSTM(128, input_shape=(self.sequence_length, self.input_shape[1])),
            Dense(128, activation='relu'),
            Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

class Autoencoder(NeuralNetwork):
    def __init__(self, input_shape):
        super().__init__(input_shape, input_shape)
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential([
            Dense(128, activation='relu', input_shape=self.input_shape),
            Dense(64, activation='relu'),
            Dense(128, activation='relu'),
            Dense(self.input_shape[1], activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
