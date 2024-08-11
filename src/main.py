import argparse
from cell_counter import CellCounter

def main(image_path, threshold):
    # Create an instance of CellCounter
    cell_counter = CellCounter()

    # Count the cells in the image
    cell_count = cell_counter.count_cells(image_path, threshold)

    # Print the result
    print(f"Number of cells in the image: {cell_count}")

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Cell Counting Project")

    # Add the image path argument
    parser.add_argument("image_path", help="Path to the image file")

    # Add a threshold argument
    parser.add_argument("--t", type=int, default=20, help="Threshold value for cell detection")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the image path argument
    main(args.image_path, args.t)