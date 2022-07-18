import os
import shutil

root = '/scratch/a/amiilab/shuvendu/data/RAF-DB'
for i in range(1, 8):
    os.makedirs(os.path.join(root, 'train', str(i)), exist_ok=True)
    os.makedirs(os.path.join(root, 'val', str(i)), exist_ok=True)

with open(os.path.join(root, 'list_patition_label.txt')) as f:
    for line in f:
        file, cls = line.split(' ')
        cls = cls.strip()
        file = file[:-4]+'_aligned.jpg'
        src = os.path.join(root, 'aligned', file)
        if file.startswith('train'):
            dest = os.path.join(root, 'train', cls, file)
        else:
            dest = os.path.join(root, 'val', cls, file)
        shutil.copy(src, dest)
