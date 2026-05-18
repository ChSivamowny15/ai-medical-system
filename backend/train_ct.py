# pyrefly: ignore [missing-import]

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

print("🚀 STARTING CT TRAINING...")

IMG_SIZE = 128
BATCH_SIZE = 32

# =========================
# TRAIN DATA
# =========================

train_generator = ImageDataGenerator(
    rescale=1./255
)

train_data = train_generator.flow_from_directory(
    "../data/ct/train",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

# =========================
# VALIDATION DATA
# =========================

valid_generator = ImageDataGenerator(
    rescale=1./255
)

valid_data = valid_generator.flow_from_directory(
    "../data/ct/valid",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

# =========================
# CNN MODEL
# =========================

model = Sequential([

    tf.keras.Input(shape=(128,128,3)),

    Conv2D(
        32,
        (3,3),
        activation='relu'
    ),

    MaxPooling2D(2,2),

    Conv2D(
        64,
        (3,3),
        activation='relu'
    ),

    MaxPooling2D(2,2),

    Flatten(),

    Dense(
        128,
        activation='relu'
    ),

    Dense(
        1,
        activation='sigmoid'
    )
])

# =========================
# COMPILE MODEL
# =========================

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("✅ MODEL CREATED")

# =========================
# TRAIN MODEL
# =========================

model.fit(
    train_data,
    validation_data=valid_data,
    epochs=5
)

print("✅ TRAINING COMPLETED")

# =========================
# SAVE MODEL
# =========================

model.save("models/cnn/ct_model.h5")

print("✅ CT MODEL SAVED SUCCESSFULLY")