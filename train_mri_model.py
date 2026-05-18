from services.image_service import load_images_from_folder
from models.cnn.mri_model import train_model

# Load dataset
images, labels = load_images_from_folder("data/mri")

print("Training started...")

model, label_encoder = train_model(images, labels)

# Save model
model.save("backend/models/cnn/mri_model.h5")

print("Model trained and saved successfully!")