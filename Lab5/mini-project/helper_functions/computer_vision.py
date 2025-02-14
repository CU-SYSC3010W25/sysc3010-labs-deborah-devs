from PIL import Image, ImageFilter
import numpy as np

def person_detected(image1_file, image2_file, t1):
    try:
        # Open images, convert to grayscale, and apply Gaussian blur
        img1 = Image.open(image1_file).convert('L').filter(ImageFilter.GaussianBlur(2))
        img2 = Image.open(image2_file).convert('L').filter(ImageFilter.GaussianBlur(2))
    except Exception as e:
        print(f"Error opening images: {e}")
        return False

    # Convert images to numpy arrays
    img1_array = np.array(img1).astype(np.float32)
    img2_array = np.array(img2).astype(np.float32)

    # Normalize and compute the absolute difference
    diff = np.abs(img1_array - img2_array)

    # Compute average pixel difference
    avg_diff = np.mean(diff)

    # Compare against a scaled threshold
    return avg_diff > t1
