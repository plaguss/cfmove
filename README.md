# cfmove
crossfit movement classifier

The objective of this project is to obtain a dataset suitable to train a model to properly classify the different popular movements in CrossFit.


## What is this

The repository is organized as follows:

- [scripts](/scripts)

    - [download.py](/scripts/download.py) contains the script to download the relevant videos from youtube.

    - [manifester.py](/scripts/manifester.py) uses the annotations obtained from supervisely to generate the clips of each movement.
    When the script is run, writes the mp4 files to [clips](/clips) folder.

- [annotations](/annotations)

    This folder contains the annotations generated using [supervisely](https://supervise.ly/), a json file per video which contains the reference labeled frames that represent a repetition of a certain movement.

- [clips](/clips)

    Contains a series of folders, each one corresponding to a movement (only data available for 2 movements for the moment). Inside the folders, there is a series of clips (short videos of a repetition of a movement from an athlete), which will be sample observations to train the model.

- [notebooks](/notebooks)

    Notebook with a tensorflow example on how to run id3 model.
    Not used, just to play around and show the generated clips
    in a notebook.

- [videos](/videos)

    Folder not tracked. Contains the videos downloaded using [download.py](scripts/download.py) scripts.


## Data extraction process

The process to obtain the data is as follows:

1) Write a url to a video in the urls.txt file (the comments, or lines starting with #, are ignored).

2) Download the video using [download.py](scripts/download.py) script.

3) Upload the video to supervise.ly, label it and generate the annotations json file. This file must be placed inside [annotations](/annotations) folder.

4) Run the [manifester.py](/scripts/manifester.py) script to generate the clips from the annotations file and the downloaded video.


### Notes

- A clip is a repetition of a movement performed by an athlete.
- 15 repetitions of each movement are extracted per athlete (video) when possible.
- The intent is to have a balance of clips from the different movements, from different camera angles, for both men and women.


### To be continued

A family of video networks is proposed in 
[movinet ref](https://arxiv.org/abs/2103.11511), which are efficient to train and also obtain state-of-the-art accuracy on kinetics 600 dataset. Furthermore, these models are ready for fine tuning: [movinet in tensorflow](https://tfhub.dev/google/collections/movinet/1). 

A model fine tuned for the case of the crossfit dataset may be able to obtain a proper accuracy for these type of data. Regarding the amount of data necessary for the task at hands, lets use as a reference UCF101 dataset. It contains a set of 101 classes, with roughly 130 clips per class. 

In this case with 20 videos approx, and 15 repetitions per video, around 300 clips may be extracted per movement.
