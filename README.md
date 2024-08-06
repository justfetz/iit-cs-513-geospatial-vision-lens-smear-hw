# Lens Smear Detection Process
### Illinois Institute of Technology CS - 513

## Project Description
This project detects lens smears in geospatial images using Python. The program leverages libraries such as numpy and OpenCV (cv2) to process images and identify smears. The process involves reading images from a specified folder, processing them, and displaying comparison visuals.

## Prerequisites
- Python 3.x
- numpy
- OpenCV (cv2)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/lens-smear-detection.git
    cd lens-smear-detection
    ```

2. **Install the dependencies:**
    ```sh
    pip install numpy opencv-python
    ```

## Usage

1. **Set the Folder Path:**
    - Open the `smearOne.py` file.
    - Locate the commented variable for reading the folder path.
    - Replace the placeholder with the correct folder path containing your images (e.g., `path/to/your/folder/*.jpg`).
    - If you have PNG files, change the extension accordingly.

2. **Run the Program:**
    - Save the `smearOne.py` file locally in any folder.
    - Navigate to that folder in the terminal.
    - Run the script:
      ```sh
      python smearOne.py
      ```

3. **Interact with the Program:**
    - The program includes wait periods using the `waitKey(0)` function, which waits for the user to hit 'Enter' to proceed through the script.
    - For "comparison" visuals, close the window to move to the next one.
    - The final image in the program will not prompt you but will exit automatically after displaying.

## Example

### Code Example
```python
import cv2
import numpy as np
import glob

# Define the path to the folder containing the images
images_path = 'path/to/your/folder/*.jpg'  # Update this path

# Read images from the specified folder
images = [cv2.imread(file) for file in glob.glob(images_path)]

for image in images:
    # Process each image
    # Example: Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and processed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', gray_image)

    # Wait for the user to press 'Enter' to proceed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Final image display
cv2.imshow('Final Image', gray_image)
cv2.waitKey(5000)  # Display for 5 seconds
cv2.destroyAllWindows()

