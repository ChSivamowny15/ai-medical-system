import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np

def build_model(input_shape=(128, 128, 3)):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(2,2),

        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),

        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # binary classification
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model


def train_model(images, labels):
    # Convert labels to numbers
    le = LabelEncoder()
    labels_encoded = le.fit_transform(labels)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        images, labels_encoded, test_size=0.2, random_state=42
    )

    model = build_model()

    model.fit(
        X_train, y_train,
        epochs=10,
        validation_data=(X_test, y_test),
        batch_size=32
    )

    return model, le