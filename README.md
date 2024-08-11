# Cell Counting Project

This project is a Python application that uses the OpenCV library to count cells in an image of a plate.

## Project Structure

The project has the following files:

- `src/main.py`: This file is the entry point of the application. It imports the `cell_counter` module and calls the necessary functions to count cells in an image.

- `src/cell_counter.py`: This file exports a class `CellCounter` which has a method `count_cells` that takes an image file path as input and returns the count of cells in the image. It uses the `utils/image_processing` module to process the image using OpenCV.

- `src/utils/image_processing.py`: This file exports functions for image processing using the OpenCV library. It includes functions such as `load_image` and `preprocess_image` that are used by the `CellCounter` class to process the image and count the cells.

- `requirements.txt`: This file lists the dependencies required for the project. It includes the `opencv-python` library to use OpenCV for image processing.

## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies listed in `requirements.txt` using a package manager like pip. Run the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To count cells in an image, follow these steps:

1. Place the image file in the project directory.

2. Open a terminal and navigate to the project directory.

3. Run the `main.py` file using a Python interpreter, passing the path to your image file as a command-line argument.

   ```sh
   python src/main.py path/to/your/image/file
   ```

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Please note that you need to replace the placeholder text with the actual content specific to your project.
