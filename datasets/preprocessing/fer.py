import os
import shutil

import pandas as pd

file = 'E:\\Datasets\\FER2013\\FERPlus\\fer2013new.csv'
df = pd.read_csv(file)
df = df.dropna()

split = list(df['Usage'])
file_name = list(df['Image name'])
val_files = set()
for i in range(len(split)):
    if 'Test' in split[i]:
        val_files.add(file_name[i])


expressions = list(df[['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear', 'contempt', 'unknown', 'NF']].idxmax(axis=1))
selected_expressions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
dest_root = 'E:\\Datasets\\FER2013\\FERPlus\\images'
for e in selected_expressions:
    os.makedirs(os.path.join(dest_root, 'train', e), exist_ok=True)
    os.makedirs(os.path.join(dest_root, 'val', e), exist_ok=True)

dic = {file_name[i]: expressions[i] for i in range(len(file_name))}

all_files = []
for path, subdirs, files in os.walk('E:\\Datasets\\FER2013\\fer+\\images'):
    for name in files:
        all_files.append(os.path.join(path, name))

for file in all_files:
    name = file.split('\\')[-1]
    if dic[name] in selected_expressions:
        if name in val_files:
            shutil.copy(file, os.path.join(dest_root, 'val', dic[name], name))
        else:
            shutil.copy(file, os.path.join(dest_root, 'train', dic[name], name))
