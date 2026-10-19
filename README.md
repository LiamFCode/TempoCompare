# Rushing or Dragging?
One of life's greatest mysteries has finally been solved. Was Andrew Neiman rushing or dragging?
This python script integrates the librosa signal processing library to determine the approximate tempo of an audio file and compare it to an inputted reference tempo.

## Context

[Whiplash Scene: Rushing or Dragging](https://www.youtube.com/watch?v=VnuImW1dWAk)

## Implementation

1. Clone the repo
```$ git clone https://github.com/LiamFCode/WhiplashAnswer.git```

2. Install requirements
```$ python -m pip install librosa```

3. Run the tool
```$ python3 whiplash.py [audio file path] [target tempo]```

ex) for Windows  ```$ python3 whiplash.py "C:\Users\JohnSmith\Desktop\AudioFiles\recording.mp3" 120```\
    or for MacOS ```$ python3 whiplash.py "/Users/JohnSmith/Desktop/AudioFiles/recording.mp3" 120```

