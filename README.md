# SEMEVAL-2021-task6-corpus


Tasks
--------------------------------------------

Subtask 1. Given the “textual content” of a meme, identify the techniques used in it (multilabel classification problem).

Subtask 2. Given the “textual content” of a meme, identify the techniques in it together with the span(s) of text in which each technique appears.

Subtask 3. Given the meme, identify all techniques used in the meme itself, i.e., in the whole meme, including the visual content (multimodal task). This is a multilabel classification problem.

Data format
--------------------------------------------

The datasets are JSON files. The text encoding is UTF-8. 
The data is located in:
* Subtask 1: /data/training_set_task1.txt
* Subtask 2: /data/training_set_task2.txt
* Subtask 3: /data/training_set_task3.zip


#### Subtask 1:
An object of the json has the following format:
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
#### Subtask 2:
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
      text -> textual content of the span
    }
  ]
}
```
##### Example
```
{
	"id": "159",
	"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!\n",
	"labels": [
		{
			"end": 241,
			"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!",
			"start": 0,
			"technique": "Causal Oversimplification"
		},
		{
			"end": 111,
			"text": "Crashed our stock market",
			"start": 87,
			"technique": "Appeal to fear/prejudice"
		},
		{
			"end": 149,
			"text": "Caused confusion from misinformation",
			"start": 113,
			"technique": "Appeal to fear/prejudice"
		},
		{
			"end": 240,
			"text": "SHIT",
			"start": 236,
			"technique": "Loaded Language"
		},
		{
			"end": 241,
			"text": "Do you remember when: Swine Flu Ebola Virus, and Zika Virus Caused mass cancellations?\nCrashed our stock market?\nCaused confusion from misinformation?\nDrove people to stockpile toilet paper?\n\nOf Course not... Because Obama HANDLED that SHIT!",
			"start": 0,
			"technique": "Glittering generalities (Virtue)"
		}
	]
}
```

#### Subtask 3:
An object of the json has the following format:
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
