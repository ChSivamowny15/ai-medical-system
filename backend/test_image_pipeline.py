from services.image_service import load_images_from_folder

images, labels = load_images_from_folder("data/mri")

print("Images shape:", images.shape)
print("Unique labels:", list(set(labels)))