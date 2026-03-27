#!/usr/bin/env python3
import whisper
import subprocess
import os

model = whisper.load_model("base")

video_files = [
    "domo_vang-20260317_202704-137995838.mp4",
    "domo_vang-20260319_023544-3220115204.mp4",
    "domo_vang-20260319_204526-116661272.mp4",
    "domo_vang-20260320_181858-1167292339.mp4",
    "domo_vang-20260321_035328-2614426481.mp4",
    "domo_vang-20260321_222317-277784430.mp4",
    "domo_vang-20260322_004435-2396537831.mp4",
    "domo_vang-20260323_161842-2563107606.mp4",
    "domo_vang-20260323_231313-2414108731 (1).mp4",
    "domo_vang-20260323_231313-2414108731.mp4",
    "domo_vang-20260324_014500-870372777.mp4",
    "domo_vang-20260324_184537-3746132322.mp4",
    "domo_vang-20251101_202557-2019469565.mp4",
    "domo_vang-20251107_205518-4073998992.mp4",
    "domo_vang-20260202_061043-1196849496.mp4",
]

for video in video_files:
    if not os.path.exists(video):
        print(f"Skipping {video} - not found")
        continue

    audio_file = video.replace(".mp4", ".wav")
    txt_file = video.replace(".mp4", ".txt")

    print(f"Extracting audio from {video}...")
    subprocess.run([
        "ffmpeg", "-y", "-i", video,
        "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
        audio_file
    ], capture_output=True)

    print(f"Transcribing {video}...")
    result = model.transcribe(audio_file, language="fr")
    
    with open(txt_file, "w") as f:
        f.write(result["text"])
    
    print(f"Saved: {txt_file}")
    
    os.remove(audio_file)

print("Done!")
