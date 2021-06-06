# Data for [SemEval-2021 Task 6: Detection of Persuasive Techniques in Texts and Images](https://arxiv.org/abs/2105.09284)

The website of the shared task, with the submission instructions, updates on the competition and the live leaderboard can be found here: https://propaganda.math.unipd.it/semeval2021task6/

__Table of contents:__

- [SEMEVAL-2021-task6-corpus](#semeval-2021-task6-corpus)
  - [List of Versions](#list-of-versions)
  - [Task Description](#task-description)
  - [Data Format](#data-format)
  - [Format checkers](#format-checkers)
  - [Scorers](#scorers)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Citation](#citation)

## List of Versions
* __v1.6.3 [2021/02/15]__ - Gold labels for test data for subtasks 1, 2 and 3 are released
* __v1.6.2 [2021/01/22]__ - Gold labels for dev data for subtasks 1, 2 and 3 are released
* __v1.6.1 [2021/01/22]__ - Test data for subtasks 1, 2 and 3 is released (200 new memes); in addition, 80 new memes for training have been added; in total we have 687 for train + 63 for dev + 200 for test.
* __v1.5 [2020/12/28]__ - Fifth batch of training data for subtasks 1, 2 and 3 is released (120 new memes; a total of 607 for train + 63 for dev).
* __v1.4 [2020/12/21]__ - Fourth batch of training data for subtasks 1, 2 and 3 is released (197 new memes; a total of 487 for train + 63 for dev).
* __v1.3 [2020/12/03]__ - Third batch of training data for subtasks 1, 2 and 3 is released (88 new memes; a total of 290 for train + 63 for dev).
* __v1.2 [2020/11/26]__ - Second batch of training data for subtasks 1, 2 and 3 is released (101 new memes; a total of 202 for train + 63 for dev).
* __v1.1 [2020/11/02]__ - Development data for subtasks 1, 2 and 3 released (63 memes).
* __v1.0 [2020/10/24]__ - Training data for subtasks 1, 2 and 3 released (101 memes).

Note that, for subtask 1 and subtask 2, you are free to use the annotations of the [PTC corpus](https://propaganda.qcri.org/semeval2020-task11/
) (more than 20,000 sentences). The domain of that corpus is news articles, but the annotations are made using the same guidelines, altough fewer techniques were considered. 

## Task Description

**Subtask 1:** Given the textual content of a meme, identify the techniques used in it (multilabel classification problem).

**Subtask 2:** Given the textual content of a meme, identify the techniques in it together with the span(s) of text in which each propaganda techniques appear

**Subtask 3:** Given a meme, identify all techniques used in the meme, including the text and the visual content (multimodal task). This is a multilabel classification problem.

## Data Format

The datasets are JSON files. The text encoding is UTF-8.
The data is located in:
* **Subtask 1:**
  * data/training_set_task1.txt
  * data/dev_set_task1.txt  
* **Subtask 2:**
  * data/training_set_task2.txt
  * data/dev_set_task1.txt   
* **Subtask 3:**
  * data/training_set_task3.zip
  * data/dev_set_task3.zip


**Note:** The input and the result files have the same format for all the subtasks.

### Input data format

#### Subtask 1:
An object of the JSON has the following format:
```
{
  id -> identifier of the example,
  labels -> the list of propaganda techniques appearing in the text,
  text -> textual content of meme
}
```
##### Example
```
{
        "id": "125",
        "labels": [
            "Loaded Language",
            "Name calling/Labeling"
        ],
        "text": "I HATE TRUMP\n\nMOST TERRORIST DO"
}
```
#### Subtask 2:
An object of the JSON has the following format:
```
{
  id -> identifier of the example,
  text -> textual content of meme
  labels : [ -> list of objects
    {
      start -> start index of the span covering the technique,
      end -> end index of the span covering technique,
      technique -> technique in the given span,
      text_fragment -> textual content of the span
    }
  ]
}
```
##### Example
```
{
        "id": "125",
        "text": "I HATE TRUMP\n\nMOST TERRORIST DO",
        "labels": [
            {
                "start": 2,
                "end": 6,
                "technique": "Loaded Language",
                "text_fragment": "HATE"
            },
            {
                "start": 19,
                "end": 28,
                "technique": "Name calling/Labeling",
                "text_fragment": "TERRORIST"
            }
        ]
}
```

#### Subtask 3:
An object of the JSON has the following format:
```
{
  id -> identifier of the example,
  text -> textual content of meme
  image -> name of the image file containing the meme
  labels -> list of propaganda techniques appearing in the meme
}
```

##### Example
```
{
        "id": "125",
        "labels": [
            "Reductio ad hitlerum",
            "Smears",
            "Loaded Language",
            "Name calling/Labeling"
        ],
        "text": "I HATE TRUMP\n\nMOST TERRORIST DO",
        "image": "125_image.png"
}
```
<!--![125_image](https://user-images.githubusercontent.com/33981376/99262849-1c62ba80-2827-11eb-99f2-ba52aa26236a.png)-->
<img src="https://user-images.githubusercontent.com/33981376/99262849-1c62ba80-2827-11eb-99f2-ba52aa26236a.png" width="350" height="350">

### Prediction Files Format

A prediction file, for example for the development set, must be one single JSON file for all memes. The entry for each meme must include the fields "id" and "labels". As an example, the input files described above would be also valid prediction files.  
In the case of task 2, each entry of the field labels must include the fields "start", "end", "technique". We provide format checkers to automatically check the format of the submissions (see below). 

If you want to check the performance of your model on the development and test (when available) sets, upload your predictions' file to the website of the shared task: https://propaganda.math.unipd.it/semeval2021task6/. 
See instructions on the website about how to register and make a submission. 

## Format checkers

The format checkers for the subtasks 1 and 2 are located in the [format_checker](format_checker) module of the project. 
Each format checker verifies that your generated results file complies with the expected format. 
The format checker for subtask 2 is included in the scorer. 

Before running the format checker please install all prerequisites through,
> pip install -r requirements.txt

### Subtask 1 and 3:
To launch it, please run the following command:

```python
python3 format_checker/task1_3.py --pred_files_path=<path_to_your_results_files> --classes_file_path=<path_to_techniques_categories_for_task>
```
Note that the checker can not verify whether the prediction file you submit contain all lines, because it does not have access to the corresponding gold file.

### Subtask 2:
Run the scorer to have the format of the input file checked. 

## Scorer and Official Evaluation Metrics

The scorer for the subtasks is located in the [scorer](scorer) module of the project.
The scorer will report official evaluation metric and other metrics of a prediction file.

You can install all prerequisites through,
> pip install -r requirements.txt

### Subtask 1 and 3:
The **official evaluation metric** for the task is **micro-F1**. However, the scorer also reports macro-F1. 

To launch it, please run the following command:
```python
python3 scorer/task1_3.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> --classes_file_path=<path_to_techniques_categories_for_task>
```

Note: You can set a flag ```-d```, to print out more detailed scores.

### Subtask 2:
The scorer for task 2 is coded in another repository. In order to add it to the project type the following commands:
```
git submodule init
git submodule update
git pull
```
Task 2 is a multi-label sequence tagging task. We modify the standard micro-averaged F1 to account for partial matching between the spans. 
In addition, an F1 value is computed for each propaganda technique.
```
cd scorer/task2; 
python3 task-2-semeval21_scorer.py -s prediction_file -r gold_labels_file -p ../../techniques_list_task1-2.txt 
```
To access the command line help of the scorer type
```
python3 task-2-semeval21_scorer.py -h
```
Note that the option -d prints additional debugging information.


## Baselines

### Task 1

 * Random baseline
 ```
cd baselines; python3 baseline_task1_random.py
 ```
If you submit the predictions of the baseline on the development set to the shared task website, you would get a F1 score of 0.04494.

### Task 2

The baseline for task 2 simply creates random spans and technique names for the development set. No learning is performed. 
Run as
```
cd baselines; python3 baseline_task2.py
```
If you submit the predictions of the baseline on the development set to the shared task website, you would get a F1 score of 0.00699.
If you score the baseline on the training set (uncomment lines 5-6 in baseline_task2.py), you should get a F1 score of 0.038112
```
python3 task-2-semeval21_scorer.py -s ../../baselines/baseline-output-task2-train.txt -r ../../data/training_set_task2.txt -p ../../techniques_list_task1-2.txt 
...
F1=0.00699
...
```

### Task 3

 * Random baseline
 ```
cd baselines; python3 baseline_task3_random.py
 ```
If you submit the predictions of the baseline on the development set to the shared task website, you would get a F1 score of 0.03376.


## Licensing

These datasets are free for general research use.


## Citation

```bibtex
@InProceedings{SemEval2021:task6,
  author    = {Dimitar Dimitrov and Bin Ali, Bishr and Shaden Shaar and Firoj Alam and Fabrizio Silvestri and Hamed Firooz and Preslav Nakov and Da San Martino, Giovanni},
  title     = {{SemEval-2021 Task 6}: Detection of Persuasion Techniques in Texts and Images},
  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
  series    = {SemEval~'21},
  year      = {2021},
  url = {https://arxiv.org/abs/2105.09284},
}
```
