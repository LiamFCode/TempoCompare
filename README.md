# Rushing or Dragging?
One of life's greatest mysteries has finally been solved. Was Andrew Neiman rushing or dragging?
This python script integrates the librosa signal processing library to determine the approximate tempo of an audio file and compare it to an inputted reference tempo.

## Context
This project was inspired by the famous scene from the movie Whiplash, in which drummer Neiman repeatedly does not match the count off tempo and cannot determine if he was rushing or dragging.
This tool finds exactly how much a recording is rushing or dragging in both bpm and percent and outputs it back to the terminal, leaving no room for guesswork or hurled chairs.\
[![Whiplash Scene: Rushing or Dragging](https://www.youtube.com/watch?v=VnuImW1dWAk)](https://www.youtube.com/watch?v=VnuImW1dWAk)

## Implementation

1. Clone the repo
```$ git clone https://github.com/LiamFCode/WhiplashAnswer.git```

2. Install requirements
```$ python -m pip install librosa```

3. Run the tool
```$ python3 whiplash.py [audio file path] [target tempo]```

ex) for Windows  ```$ python3 whiplash.py "C:\Users\JohnSmith\Desktop\AudioFiles\recording.mp3" 120```\
&nbsp;&nbsp;&nbsp;&nbsp;or for MacOS ```$ python3 whiplash.py "/Users/JohnSmith/Desktop/AudioFiles/recording.mp3" 120```

## How it Works
The WhiplashAnswer tool takes the inputted audio file and approximates its tempo through the librosa python signal processing library. Next it compares this tempo to the inputted target tempo, finds the BPM and percent difference, and outputs it with the format shown in the example below.
```
Target tempo:   120 BPM
Detected tempo: 130 BPM
RESULT: Not quite my tempo. Rushing by 10 BPM (8.3%)
```

## Known Issues
- Librosa identifies double time or half time as rushing or dragging, respectively, by 200%
