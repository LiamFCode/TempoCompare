import librosa
import argparse

def compare_tempo(audio_file, target_bpm):
    #*---load-audio-file-and-guage-tempo---*#
    y, sr = librosa.load(audio_file, sr=22050, mono=True)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    #*---handle-NumPy-array-return---*#
    detected_bpm = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)

    #*---out---*#
    if detected_bpm <= 0:
        print("ERROR: unreliable tempo")
        return

    difference = detected_bpm - target_bpm
    percentage = (difference / target_bpm) * 100

    print(f"Target tempo:   {target_bpm:.1f} BPM")
    print(f"Detected tempo: {detected_bpm:.1f} BPM")

    if abs(difference) < 0.5:
        print("RESULT: Approx. same tempo")
    elif difference > 0:
        print(f"RESULT: Not quite my tempo. Rushing by {difference:.1f} BPM ({percentage:+.1f}%)")
    else:
        print(f"RESULT: Not quite my tempo. Dragging by {abs(difference):.1f} BPM ({percentage:+.1f}%)")

#*---prevent-run-when-imported-&&-start---*#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare tempo of recording to target bpm")
    parser.add_argument("audio_file", help="Path to audio recording")
    parser.add_argument("target_bpm", type=float, help="Target tempo in bpm")
    args = parser.parse_args()

    compare_tempo(args.audio_file, args.target_bpm)
