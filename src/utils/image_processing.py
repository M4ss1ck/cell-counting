import cv2
import numpy as np
from datetime import datetime
import os

def load_image(image_path):
    """
    Load an image from the given file path.
    """
    image = cv2.imread(image_path)[:,:,1].copy()
    image = cv2.medianBlur(image, ksize=3)
    # imshow(image)
    return image

def preprocess_image(image, threshold):
    """
    Preprocess the image for cell counting.
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_canvas = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    bg = cv2.medianBlur(gray_image, ksize=101)
    signal = cv2.subtract(gray_image, bg)
    signal = (signal / signal.max() * 255).astype(np.uint8)
    smooth = cv2.GaussianBlur(signal, ksize=None, sigmaX=2)
    valmask = (smooth > threshold)
    peakmask = (smooth == cv2.dilate(smooth, kernel=None, iterations=20))
    blobs = (valmask & peakmask)
    blobs = cv2.morphologyEx(blobs * np.uint8(255), cv2.MORPH_DILATE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11)))
    blobs = blobs.astype(bool)
    (nlabels, labelmap, stats, centroids) = cv2.connectedComponentsWithStats(blobs.astype(np.uint8))
    print(nlabels-1, "components")
    np.hstack([centroids[:5], stats[:5,2:4]]) # first is background

    canvas = cv2.cvtColor(signal, cv2.COLOR_GRAY2BGR)
    for pt in centroids[1:]:
        cv2.circle(canvas, center=pt.astype(int), radius=20, color=(255,255,0), thickness=2)

    # save result image
    save_image(f"count_{nlabels-1}", canvas)

    # Compose the image with gray image on the left and preprocessed on the right
    composed_image = np.hstack((gray_canvas, canvas))

    # Save the composed image
    save_image('composed', composed_image)

    # Return the preprocessed image.
    return nlabels-1

def count_cells_in_image(image):
    """
    Count the number of cells in the given image.
    """
    cell_count = 0
    # Apply cell counting algorithm using OpenCV or any other method.
    # Return the count of cells.
    return cell_count

def save_image(name, canvas):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # Get the parent directory of the src directory
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    # Create the results directory if it doesn't exist
    results_dir = os.path.join(parent_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)
    # Create the output file path with the timestamp
    output_path = os.path.join(results_dir, f"{timestamp}_{name}.png")
    
    cv2.imwrite(output_path, canvas)
    print(f"{output_path} saved!")