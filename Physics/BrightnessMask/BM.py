import os
import cv2

def create_brightness_mask(source_folder, destination_folder, crop_width, crop_height):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of video files in the source folder
    video_files = [f for f in os.listdir(source_folder) if f.endswith('.mp4')]

    for video_file in video_files:
        # Construct paths for source and destination files
        source_path = os.path.join(source_folder, video_file)
        destination_path = os.path.join(destination_folder, video_file)

        # Open the video file
        capture = cv2.VideoCapture(source_path)

        # Get video properties
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = capture.get(cv2.CAP_PROP_FPS)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Calculate cropping parameters
        start_x = (width - crop_width) // 2
        end_x = start_x + crop_width
        start_y = (height - crop_height) // 2
        end_y = start_y + crop_height

        # Create a VideoWriter object to save the modified video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output = cv2.VideoWriter(destination_path, fourcc, fps, (crop_width, crop_height))

        for _ in range(frame_count):
            # Read a frame from the video
            ret, frame = capture.read()

            if ret:
                # Crop the frame
                cropped_frame = frame[start_y:end_y, start_x:end_x]

                # Convert the cropped frame to grayscale
                grayscale_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)

                # Apply histogram equalization to enhance contrast
                equalized_frame = cv2.equalizeHist(grayscale_frame)

                # Create a binary mask based on brightness threshold
                _, mask = cv2.threshold(equalized_frame, 253, 255, cv2.THRESH_BINARY)

                # Apply the mask to the original frame
                masked_frame = cv2.bitwise_and(cropped_frame, cropped_frame, mask=mask)

                # Write the modified frame to the output video file
                output.write(masked_frame)

        # Release the VideoCapture and VideoWriter objects
        capture.release()
        output.release()

        print(f"Processed video: {video_file}")

    print("Processing completed.")

# Example usage
source_folder = './BMIn'
destination_folder = './BMOut'
crop_width = 1050  # Specify the desired crop width
crop_height = 1050  # Specify the desired crop height
create_brightness_mask(source_folder, destination_folder, crop_width, crop_height)
