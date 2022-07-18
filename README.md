
# Analysis of Semi-Supervised Methods for Facial Expression Recognition
 
Official Code for release for ***Analysis of Semi-Supervised Methods for Facial Expression Recognition***. The paper has been accepted in Affective Computing and Intelligent Interaction (ACII), 2022.

<img src="figures/overview.png" alt="drawing" width="600"/>

### Dataset
We used the following dataset 
1. [AffectNet](http://mohammadmahoor.com/affectnet/)
2. [FER-13](https://www.kaggle.com/datasets/msambare/fer2013)
3. [RAF-DB](http://www.whdeng.cn/RAF/model1.html)

Once the dataset is downloaded use the scripts in `datasets/preprocessing` to preprocess the dataset.
The porcessed dataset structure should look like this:
```
dataset
├── train
│   ├── class_001
|   |      ├── 1.jpg
|   |      ├── 2.jpg
|   |      └── ...
│   ├── class_002
|   |      ├── 1.jpg
|   |      ├── 2.jpg
|   |      └── ...
│   └── ...
└── val
    ├── class_001
    |      ├── 1.jpg
    |      ├── 2.jpg
    |      └── ...
    ├── class_002
    |      ├── 1.jpg
    |      ├── 2.jpg
    |      └── ...
    └── ...
```

### Run
Modify the config files in `config/` directory if needed.

```
python [ALGO_NAME].py --c [CONFIG_FILE]
```


### Results
<img src="figures/results.png" alt="drawing" width="700"/>

### Acknowledgements
The semi-supervised algorithm implementations are followed from the following repository: [TorchSSL](https://github.com/TorchSSL/TorchSSL)

### Citation
 
Please cite our paper if you this code repo in your work.
```
@inproceedings{roy2022analysis,
  title={Analysis of Semi-Supervised Methods for Facial Expression Recognition},
  author={Roy, Shuvendu and Etemad, Ali},
  booktitle={2022 10th International Conference on Affective Computing and Intelligent Interaction (ACII)},
  pages={1--8},
  year={2022},
  organization={IEEE}
}
```

## Contact
Thanks for your attention!
If you have any suggestion or question, you can leave a message here or contact us directly:
- shuvendu.roy@queensu.ca

