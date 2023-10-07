# Inventory Image Logger

## Author
Liang Chu

liamchu@protonmail.com


## Description
Inventory Image Logger was originally designed for a small auction and trading company that purchases Amazon returns for resale. Staff members utilize this script to automatically capture images of items within the packages, renaming them systematically before adding them to the inventory.
# Usage

**Inventory Image Logger** is designed to facilitate the process of capturing images for inventory management. Here's how to use it:

## Setup Destination Folder

The script requires a destination folder where the images will be saved. This can be provided as an argument when running the script.

## Capture Images

1. Run the script.
2. You'll see a camera preview. This is where you'll position the items for capturing images.
3. Enter the product number when prompted. Ensure you enter digits only.
4. Follow the on-screen instructions to capture images:
    - Press `1` to continue adding pictures for the same product.
    - Press `2` to take a picture for the next product.
    - Press `3` to manually enter the next product.
    - Press `4` to replace the previous picture.

## Output Images

Images are saved in the format `item-code_index.jpg`, where:
- `item-code` is the unique identifier you entered for the item.
- `index` is a sequential number indicating the order of images for the same item.

## Exiting

Close the command window to exit.


## Functions in autoPic.py
- `capture_images`: Main function to initiate the image capture process.
- `find_new_productCode`: Determines the next product code based on existing files.
- `find_smallest_index`: Finds the smallest index for a given filename.
- `release_resources`: Releases camera resources and destroys any OpenCV windows.
- `show_camera_preview`: Displays the camera preview to the user.

## System Requirements
### Hardware:
- A computer with a USB or built-in camera.
- Sufficient storage space for saving images.

## Software Requirements

- **Python**: The latest version of Python is **3.12.0**. Please ensure you have this version installed on your system.
- **OpenCV (cv2)**: The latest version of OpenCV for Python is **4.8.1.78**. This library is used in your script for image processing.
- **Operating System**: The script requires an operating system that supports the execution of Python scripts and batch files. As of Python 3.12, it supports Windows 8.1 and newer. If you require Windows 7 support, please install Python 3.8.


### Additional Requirements:
- A camera (either built-in or external) is essential for capturing images.

## Build Instructions
1. Clone the GitHub repository to your local machine.
2. Ensure you have Python installed. If not, download and install it from the official Python website.
3. Install the required Python libraries using pip:
    ```shell
    pip install opencv-python
    ```
4. Navigate to the directory containing the script.
5. Run the script using the command:
    ```css
    python autoPic.py [Destination Folder]
    ```
    Replace `[Destination Folder]` with the path where you want the images to be saved.

    or modify the take_pic.bat and simply click it for easier access. Make sure take_pic.bat and autoPic.py are in the same folder.
## License

This project is licensed under the terms of the MIT License. See the LICENSE file for details.
