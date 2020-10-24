# SEMEVAL-2021-task6-corpus


Tasks
--------------------------------------------

Subtask 1. Given the “textual content” of a meme, identify the techniques used in it (multilabel classification problem).

Subtask 2. Given the “textual content” of a meme, identify the techniques in it together with the span(s) of text in which each technique appears.

Subtask 3. Given the meme, identify all techniques used in the meme itself, i.e., in the whole meme, including the visual content (multimodal task). This is a multilabel classification problem.

Data format
--------------------------------------------

The datasets are JSON files. The text encoding is UTF-8. An object of the json has the following format:

Subtask 1:
```
{
  id -> identification of the sample,
  labels -> a list of propaganda techniques related to the text,
  text -> textual content of meme
}
```
Subtask 2:
```
{
  id -> identification of the sample,
  text -> textual content of meme
  labels : [ -> list of objects
    {
      start -> start index of technique span,
      end -> end index of technique span,
      technique -> technique related to the given span,
      text -> textual content of the span
    }
  ]
}
```

Subtask 3:
```
{
  id -> identification of the sample,
  text -> textual content of meme
  image -> name of the image related to the labels,text,id
  labels -> list of propaganda techniques related to the image and text
}
```

Examples:

Subtask 1:
```
{
  "id": "1",
  "labels": [
    "Loaded Language"
  ],
  "text": "What people think super heroes look like:\n\nWhat super heroes actually look like:\n",
}
```

Subtask 2:
```
{
  "id": "92",
  "text": "AT LAST, THE ILLEGALS AND ECONOMIC DEADBEATS AND PARASITES HAVE A PRESIDENT ON THEIR MONEY\n\nU.S. DEPARTMENT OF AGRICULTURE\n\nFOOD COUPON\n\nVALUE\n1\nDOLLAR\n\nNON-TRANSFERABLE EXCEPT UNDER CONDITIONS PRESCRIDED BY THE SECRETARY OF AQGRICULTURE\n",
  "labels": [
    {
      "start": 49,
      "end": 58,
      "technique": "Loaded Language",
      "text": "PARASITES"
    }
  ]
}
```
Subtask 3:
```
{
  "id": "5",
  "labels": [
    "Name calling/Labeling",
    "Loaded Language",
    "Smears"
  ],
  "text": "The Axis of Evil of the United States of America\n",
  "image": "5_image.png"
}
```
