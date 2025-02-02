import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        # Load the image using OpenCV
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        # Split the image into its RGB channels
        b, g, r = cv2.split(image)

        # Calculate the histograms of pixel intensities
        hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
        hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])

        # Create a figure and axes for the histograms
        fig, ax = plt.subplots()

        # Plot the histograms
        ax.plot(hist_r, color='red', label='R')
        ax.plot(hist_g, color='green', label='G')
        ax.plot(hist_b, color='blue', label='B')

        # Set labels and title
        ax.set_xlabel('Pixel Intensity')
        ax.set_ylabel('Number of Pixels')
        ax.set_title('Pixel Intensity Histogram')

        # Add a legend
        ax.legend()

        # Save the graph to the output folder
        output_path = os.path.join(output_folder, f'{os.path.splitext(image_file)[0]}.png')
        plt.savefig(output_path)
        plt.close()

        print(f'Processed {image_file}.')

    print('Image processing completed.')


# Example usage
input_folder = './LCIn'
output_folder = './LCOut'

process_images(input_folder, output_folder)
