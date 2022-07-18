import shutil
from tqdm import tqdm
import pandas as pd
import os

root = '/scratch/a/amiilab/shuvendu/data/AffectNet/'
class_dict = {
    0: 'neutral',
    1: 'happy',
    2: 'sad',
    3: 'surprise',
    4: 'fear',
    5: 'disgust',
    6: 'anger'
}

for key, val in class_dict.items():
    os.makedirs(os.path.join(root, 'train', val), exist_ok=True)
    os.makedirs(os.path.join(root, 'val', val), exist_ok=True)

# train images
data = pd.read_csv(os.path.join(root, 'training.csv'))
data.groupby('expression').count()

files = list(data['subDirectory_filePath'])
expression = list(data['expression'])

for i in tqdm(range(len(files))):
    file = files[i]
    src = os.path.join(root, 'images', file)
    file = file.split('/')[-1]
    if expression[i] in class_dict:
        dest = os.path.join(root, 'train', class_dict[expression[i]], file)
        shutil.copy(src, dest)

# val images
data = pd.read_csv(os.path.join(root, 'validation.csv'))

files = list(data['subDirectory_filePath'])
expression = list(data['expression'])

for i in tqdm(range(len(files))):
    file = files[i]
    src = os.path.join(root, 'images', file)
    file = file.split('/')[-1]
    if expression[i] in class_dict:
        dest = os.path.join(root, 'val', class_dict[expression[i]], file)
        shutil.copy(src, dest)
