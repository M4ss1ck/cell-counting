import cv2
from utils.image_processing import preprocess_image, count_cells_in_image

class CellCounter:
    def count_cells(self, image_path, threshold):
        # Load the image
        image = cv2.imread(image_path)

        cell_count = preprocess_image(image, threshold)

        return cell_count