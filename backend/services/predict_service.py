import cv2
import numpy as np
import tensorflow as tf
import os

# =========================
# BASE PATH
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# =========================
# MODEL PATHS
# =========================

MRI_MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "cnn",
    "mri_model.h5"
)

CT_MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "cnn",
    "ct_model.h5"
)

UV_MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "cnn",
    "uv_model.h5"
)

# =========================
# LOAD MODELS
# =========================

mri_model = tf.keras.models.load_model(
    MRI_MODEL_PATH
)

ct_model = tf.keras.models.load_model(
    CT_MODEL_PATH
)

uv_model = tf.keras.models.load_model(
    UV_MODEL_PATH
)

IMG_SIZE = 128


# =========================
# PREDICT FUNCTION
# =========================

def predict_image(image_path, scan_type):

    # =========================
    # READ IMAGE
    # =========================

    img = cv2.imread(image_path)

    if img is None:

        return {
            "error": "Invalid image"
        }

    # =========================
    # PREPROCESS
    # =========================

    img = cv2.resize(
        img,
        (IMG_SIZE, IMG_SIZE)
    )

    img = img / 255.0

    img = np.expand_dims(
        img,
        axis=0
    )

    # =========================
    # SELECT MODEL
    # =========================

    if scan_type == "mri":

        model = mri_model

    elif scan_type == "ct":

        model = ct_model

    elif scan_type == "uv":

        model = uv_model

    else:

        return {
            "error": "Invalid scan type"
        }

    # =========================
    # PREDICT
    # =========================

    pred = model.predict(img)[0][0]

    # =========================
    # LABEL
    # =========================

    label = "yes" if pred > 0.5 else "no"

    confidence = float(
        pred if pred > 0.5
        else 1 - pred
    )

    return {

        "scan_type": scan_type.upper(),

        "prediction": label,

        "confidence": round(
            confidence * 100,
            2
        )
    }