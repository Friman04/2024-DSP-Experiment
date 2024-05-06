import os
import shutil
from mutagen.mp3 import MP3

def classify_audio_files(directory):
    categories = ['希儿', '黑希儿', '死生之律者', '魇夜星渊']
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                for category in categories:
                    if file.startswith(category):
                        target_folder = os.path.join(directory, category)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                        shutil.copy(os.path.join(root, file), os.path.join(target_folder, file))
                        break
classify_audio_files('../希儿')

import os

def calculate_total_duration(directory):
    total_duration = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                audio = MP3(os.path.join(root, file))
                total_duration += audio.info.length
    return total_duration

#print(calculate_total_duration(r'C:\Users\Friman\Desktop\DSP实验\1-语音合成\dataset\希儿\希儿'))
