import glob
import cv2
import os
import atexit
import threading
import sys

# Global variables 
input_instructions = "Press 1 to continue adding pictures for the same product\nPress 2 to take a picture for the next product\nPress 3 to manually enter the next product\nPress 4 to replace previous picture\n"
# Take the destination folder as an input argument
DESTINATION_FOLDER = os.path.expanduser(sys.argv[1])
current_filename = None
take = False
camera = cv2.VideoCapture(0)  # 0 for the default camera

# Function to release resources when the program ends


def release_resources():
    camera.release()
    cv2.destroyAllWindows()


# Register the function to be called on exit
atexit.register(release_resources)

# Function to find the smallest index for a filename that does not exist yet


def find_smallest_index(filename):
    index = 1
    while True:
        file_to_check = f"{filename}_{index}.jpg"
        if not os.path.isfile(os.path.join(DESTINATION_FOLDER, file_to_check)):
            return index
        index += 1


# Function to find a new product code that does not exist yet


def find_new_productCode(filename):
    productCode = filename
    while True:
        file_to_check = f"{productCode}_1.jpg"
        if not glob.glob(os.path.join(DESTINATION_FOLDER, file_to_check)):
            return productCode
        productCode = str(int(productCode) + 1)

# Function to show the camera preview in a window


def show_camera_preview():
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to take a picture.")
            break

        cv2.imshow('Preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Main function to capture images and save them to files


def capture_images():
    global current_filename

    if not os.path.exists(DESTINATION_FOLDER):
        os.makedirs(DESTINATION_FOLDER)

    # Start a separate thread for the camera preview
    threading.Thread(target=show_camera_preview).start()

    while True:
        if current_filename is None:
            while True:
                user_filename = input("Product number (digits only): ")
                if user_filename.isdigit():
                    current_filename = user_filename
                    count = find_smallest_index(current_filename)
                    break
                else:
                    print("Format error, please enter a number.")

        while True:

            user_input = input()

            if user_input in ('1', '2', '3', '4'):
                take = True
                break
            else:
                take = False
                count = find_smallest_index(current_filename)
                print("Invalid input.\n")
                print(input_instructions)

        if user_input == '3':
            current_filename = None
            continue
        if user_input == '2':
            current_filename = find_new_productCode(current_filename)
            count = find_smallest_index(current_filename)
        if user_input == '1':
            count = find_smallest_index(current_filename)

        ret, frame = camera.read()
        if not ret:
            print("Failed to take a picture.")
            break
        if take:
            file_path = os.path.join(
                DESTINATION_FOLDER, f"{current_filename}_{count}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"Picture has been successfully saved to {file_path}\n")


if __name__ == "__main__":
    capture_images()
