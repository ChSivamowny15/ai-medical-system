# pyrefly: ignore [missing-import]

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

print("🚀 STARTING UV TRAINING...")

IMG_SIZE = 128
BATCH_SIZE = 32

# =========================
# DATASET
# =========================

generator = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = generator.flow_from_directory(
    "../data/uv",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="training"
)

valid_data = generator.flow_from_directory(
    "../data/uv",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation"
)

# =========================
# MODEL
# =========================

model = Sequential([

    tf.keras.Input(shape=(128,128,3)),

    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(128, activation='relu'),

    Dense(1, activation='sigmoid')
])

# =========================
# COMPILE
# =========================

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("✅ MODEL CREATED")

# =========================
# TRAIN
# =========================

model.fit(
    train_data,
    validation_data=valid_data,
    epochs=5
)

print("✅ TRAINING COMPLETED")

# =========================
# SAVE
# =========================

model.save("models/cnn/uv_model.h5")

print("✅ UV MODEL SAVED SUCCESSFULLY")