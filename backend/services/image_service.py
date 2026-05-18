import os
import cv2
import numpy as np

IMG_SIZE = 128

def load_images_from_folder(folder_path):
    images = []
    labels = []

    # Check if path exists
    if not os.path.exists(folder_path):
        print("❌ Path not found:", folder_path)
        return np.array(images), np.array(labels)

    for label in os.listdir(folder_path):
        label_path = os.path.join(folder_path, label)

        # Skip if not a folder
        if not os.path.isdir(label_path):
            continue

        for file in os.listdir(label_path):
            img_path = os.path.join(label_path, file)

            # Read image
            img = cv2.imread(img_path)

            # Skip unreadable images
            if img is None:
                continue

            try:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                img = img / 255.0

                images.append(img)
                labels.append(label)

            except:
                continue

    return np.array(images), np.array(labels)