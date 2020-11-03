# SEMEVAL-2021-task6-corpus

__Table of contents:__

- [SEMEVAL-2021-task6-corpus](#semeval-2021-task6-corpus)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Task Description](#task-description)
  - [Data Format](#data-format)
    - [Subtask 1](#subtask-1)
    - [Subtask 2](#subtask-2)
    - [Subtask 3](#subtask-3)
  - [Format checkers](#format-checkers)
    - [Subtask 1](#subtask-1)
    - [Subtask 2](#subtask-2)
    - [Subtask 3](#subtask-3)
  - [Scorers](#scorers)
    - [Subtask 1](#subtask-1)
    - [Subtask 2](#subtask-2)
    - [Subtask 3](#subtask-3)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)
  - [Citation](#citation)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/11/24]__ - Training data for subtasks 1, 2 and 3 are released. 


## Task Description

Subtask 1. Given the “textual content” of a meme, identify the techniques used in it (multilabel classification problem).

Subtask 2. Given the “textual content” of a meme, identify the techniques in it together with the span(s) of text in which each technique appears.

Subtask 3. Given a meme, identify all techniques used in the meme, including the text and the visual content (multimodal task). This is a multilabel classification problem.

## Data Format

The datasets are JSON files. The text encoding is UTF-8. 
The data is located in:
* Subtask 1: /data/training_set_task1.txt
* Subtask 2: /data/training_set_task2.txt
* Subtask 3: /data/training_set_task3.zip

Input and Result files have the same format for all the subtasks. 

### Subtask 1:
An object of the json has the following format:
```
{
  id -> identifier of the example,
  labels -> the list of propaganda techniques appearing in the text,
  text -> textual content of meme
}
```
#### Example
```
{
		"id": "159",
		"labels": [
			"Loaded Language",
			"Glittering generalities (Virtue)",
			"Appeal to fear/prejudice",
			"Causal Oversimplification"
		],
		"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!\n"
}
```
### Subtask 2:
An object of the json has the following format:
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
#### Example
```
{
	"id": "159",
	"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!\n",
	"labels": [
		{
			"end": 241,
			"text_fragment": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!",
			"start": 0,
			"technique": "Causal Oversimplification"
		},
		{
			"end": 111,
			"text_fragment": "Crashed our stock market",
			"start": 87,
			"technique": "Appeal to fear/prejudice"
		},
		{
			"end": 149,
			"text_fragment": "Caused confusion from misinformation",
			"start": 113,
			"technique": "Appeal to fear/prejudice"
		},
		{
			"end": 240,
			"text_fragment": "SHIT",
			"start": 236,
			"technique": "Loaded Language"
		},
		{
			"end": 241,
			"text_fragment": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!",
			"start": 0,
			"technique": "Glittering generalities (Virtue)"
		}
	]
}
```

### Subtask 3:
An object of the json has the following format:
```
{
  id -> identifier of the example,
  text -> textual content of meme
  image -> name of the image file containing the meme
  labels -> list of propaganda techniques appearing in the meme
}
```

#### Example
```
{
		"id": "159",
		"labels": [
			"Glittering generalities (Virtue)",
			"Appeal to fear/prejudice",
			"Loaded Language",
			"Causal Oversimplification",
			"Smears"
		],
		"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove    people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!\n",
		"image": "159_image.png"
}
```
![159_image](https://user-images.githubusercontent.com/33981376/97086976-54fbe380-162f-11eb-9b54-22d332ea3e2b.png)


## Format checkers

The checker for the subtask is located in the [format_checker](format_checker) module of the project.
The format checker verifies that your generated results file complies with the expected format.

You can install all prerequests through, 
> pip install -r requirments.txt

### Subtask 1:
To launch it, run: 
> python3 format_checker/task1.py --pred_files_path=<path_to_your_results_files> --classes_file_path=<path_to_technqiues_categories_for_task1> <br/>

### Subtask 2:
TBA

### Subtask 3:
To launch it, run: 
> python3 format_checker/task3.py --pred_files_path=<path_to_your_results_files> --classes_file_path=<path_to_technqiues_categories_for_task3> <br/>

Note that the checker can not verify whether the prediction file you submit contain all lines/tweets, because it does not have access to the corresponding gold file.

## Scorers

The scorer for the subtasks is located in the [scorer](scorer) module of the project.
The scorer will report official evaluation metric and other metrics of a prediction file. 

You can install all prerequests through, 
> pip install -r requirments.txt

### Subtask 1:
The official evaluation measure is MACRO-F1 and MICRO-F1.

To launch it, run: 
> python3 scorer/task1.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> --classes_file_path=<path_to_technqiues_categories_for_task1> <br/>

NOTE: You can set a flag ```-d```, to print out more detailed scores. 

### Subtask 2:
TBA

### Subtask 3:
The official evaluation measure is MACRO-F1 and MICRO-F1.

To launch it, run: 
> python3 scorer/task3.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> --classes_file_path=<path_to_technqiues_categories_for_task3> <br/>

NOTE: You can set a flag ```-d```, to print out more detailed scores. 


## Baseline

TBA

## Licensing

  These datasets are free for general research use.

## Credits

TBA

## Citation

TBA

