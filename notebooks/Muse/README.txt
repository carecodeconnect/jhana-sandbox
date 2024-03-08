Acquire the signal and store it in a CSV file (adding keyboard events), follow the instructions in this repository:
https://github.com/alexandrebarachant/muse-lsl

1- create and activate a Conda environment (name: Muse)
2- pip install git+https://github.com/peplin/pygatt #to install Pygatt on MacOS
3- pip install muselsl
4- conda install -c conda-forge liblsl

Start streaming:
1- !muselsl stream
2- $ muselsl view (on another terminal to make the stream run independently)

Create a static dataset using the sliding window approach and several functions:
https://github.com/jordan-bird/eeg-feature-generation?tab=readme-ov-file

Folder structure:
- muse.ipynb: to start the stream
- EEG_to_CSV: to store the EEG recording into a CSV file and plot the 4 channels
- PPG_to_CSV: to store the PPG recording into a CSV file and plot the 3 channels
- HRV: using heartpy it cleans the PPG signal and calculates the BPM and HRV