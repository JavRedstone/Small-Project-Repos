import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks

def save_fft_as_image(input_folder, output_folder):
    audio_files = glob.glob(os.path.join(input_folder, '*.wav'))  # Change the file extension if needed

    for file_path in audio_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Read audio file
        sample_rate, data = wavfile.read(file_path)

        # Compute FFT
        fft_data = np.fft.fft(data)

        # Generate frequency axis
        freq_axis = np.fft.fftfreq(len(data), 1/sample_rate)

        print('Generated FFT for ' + file_name)

        # Set the figure size
        plt.figure(figsize=(64, 56))  # Adjust the width and height as desired

        # Plot FFT
        plt.plot(freq_axis, np.abs(fft_data))
        plt.title('FFT')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.xlim(0, sample_rate / 2)  # Set the x-axis limits

        # Find peaks in the FFT data
        peaks, _ = find_peaks(np.abs(fft_data), distance=1000)

        print('Annotating Peaks for ' + file_name)

        # Annotate frequency for each peak
        for peak in peaks:
            freq = freq_axis[peak]
            plt.annotate(f'{round(freq)} Hz', xy=(freq, np.abs(fft_data)[peak]), xytext=(5, 5),
                            textcoords='offset points', ha='center', va='bottom')

        # Save FFT as an image
        output_path = os.path.join(output_folder, f'{file_name}_fft.png')
        plt.savefig(output_path)
        plt.close()

        print('Completed FFT for ' + file_name)
        print('================================================================')

# Example usage
input_folder = './FFTIn'
output_folder = './FFTOut'

save_fft_as_image(input_folder, output_folder)
