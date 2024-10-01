import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

class DeepLearningModel:
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

class GenerativeAdversarialNetwork(DeepLearningModel):
    def __init__(self, input_shape, num_classes):
        super().__init__(input_shape, num_classes)
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()

    def build_generator(self):
        model = tf.keras.models.Sequential([
            Dense(128, activation='relu', input_shape=(100,)),
            Dense(128, activation='relu'),
            Dense(self.input_shape[1], activation='tanh')
        ])
        return model

    def build_discriminator(self):
        model = tf.keras.models.Sequential([
            Dense(128, activation='relu', input_shape=self.input_shape),
            Dense(128, activation='relu'),
            Dense(1, activation='sigmoid ')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        for epoch in range(epochs):
            for i in range(len(X_train)):
                noise = np.random.normal(0, 1, (batch_size, 100))
                generated_images = self.generator.predict(noise)
                d_loss_real = self.discriminator.train_on_batch(X_train[i:i+batch_size], np.ones((batch_size, 1)))
                d_loss_fake = self.discriminator.train_on_batch(generated_images, np.zeros((batch_size, 1)))
                g_loss = self.generator.train_on_batch(noise, np.ones((batch_size, 1)))
