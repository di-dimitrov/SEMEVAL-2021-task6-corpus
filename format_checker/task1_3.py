import os
import argparse
import logging
import json

"""
This script checks whether the results format for subtask 1 and subtask 3 is correct. 
It also provides some warnings about possible errors.

The submission of the result file should be in json format. 
It should be a list of objects:
{
  id     -> identifier of the test sample,
  labels -> the list of propaganda techniques detected in the text (for subtask 1) 
            or image (for subtask 3) 
}

"""

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
KEYS = ['id', 'labels']

def read_classes(file_path):
  CLASSES = []
  with open(file_path) as f:
    for label in f.readlines():
      label = label.strip()
      if label:
        CLASSES.append(label)
  return CLASSES

def check_format_task1_task3(file_path, CLASSES=[]):
  if not os.path.exists(file_path):
    logging.error("File doesnt exists: {}".format(file_path))
    return False
  
  try:
    with open(file_path) as p:
      submission = json.load(p)
  except:
    logging.error("File is not a valid json file: {}".format(file_path))
    return False
  for i, obj in enumerate(submission):
    for key in KEYS:
      if key not in obj:
        logging.error("Missing entry in {}:{}".format(file_path, i))
        return False
    for label in obj['labels']:
      if label not in CLASSES:
        logging.error("Unknown Label in {}:{}".format(file_path, i))
        return False
  return True


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--pred_files_path", "-p", nargs='+', required=True, 
    help="The absolute path to the files you want to check.", type=str)
  parser.add_argument("--classes_file_path", "-c", required=True, 
    help="The absolute path to the file containing all the labels categories. (Note taht the different subtasks will have different techniques. Make sure to provide path for the right subtask)", type=str)
  
  args = parser.parse_args()
  logging.info("Subtask 1 and 3: Checking files: {}".format(args.pred_files_path))
  
  if not os.path.exists(args.classes_file_path):
    logging.error("File doesnt exists: {}".format(classes_file_path))
    raise ValueError("File doesnt exists: {}".format(classes_file_path))
  CLASSES = read_classes(args.classes_file_path)

  for pred_file_path in args.pred_files_path:
    check_format_task1_task3(pred_file_path, CLASSES)