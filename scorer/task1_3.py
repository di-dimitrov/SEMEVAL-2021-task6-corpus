import pdb
import json
import logging.handlers
import argparse
import os
from sklearn.metrics import f1_score
from sklearn.preprocessing import MultiLabelBinarizer

import sys
sys.path.append('.')
from format_checker.task1_3 import check_format_task1_task3
from format_checker.task1_3 import read_classes

"""
Scoring of SEMEVAL-Task-6--subtask-1-and-3  with the metrics f1-macro and f1-micro. 
"""

logger = logging.getLogger("task1-3_scorer")
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.setLevel(logging.INFO)
#logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)


def _read_gold_and_pred(pred_fpath, gold_fpath):
  """
  Read gold and predicted data.
  :param pred_fpath: a json file with predictions, 
  :param gold_fpath: the original annotated gold file.
    [{
      id     -> identifier of the test sample,
      labels -> the list of propaganda techniques detected in the text,
    }]

  :return: {id:pred_labels} dict; {id:gold_labels} dict
  """

  gold_labels = {}
  with open(gold_fpath, encoding='utf-8') as gold_f:
    gold = json.load(gold_f)
    for obj in gold:
      gold_labels[obj['id']] = obj['labels']

  pred_labels = {}
  with open(pred_fpath, encoding='utf-8') as pred_f:
    pred = json.load(pred_f)
    for obj in pred:
      pred_labels[obj['id']] = obj['labels']

  if set(gold_labels.keys()) != set(pred_labels.keys()):
      logger.error('There are either missing or added examples to the prediction file. Make sure you only have the gold examples in the prediction file.')
      raise ValueError('There are either missing or added examples to the prediction file. Make sure you only have the gold examples in the prediction file.')
  
  return pred_labels, gold_labels

def evaluate(pred_fpath, gold_fpath, CLASSES):
  """
    Evaluates the predicted classes w.r.t. a gold file.
    Metrics are: macro_f1 nd micro_f1
    :param pred_fpath: a json file with predictions, 
    :param gold_fpath: the original annotated gold file.
    [{
      id     -> identifier of the test sample,
      labels -> the list of propaganda techniques detected in the text,
    }]
  """
  pred_labels, gold_labels = _read_gold_and_pred(pred_file, gold_file)
  
  gold = []
  pred = []
  for id in gold_labels:
    gold.append(gold_labels[id])
    pred.append(pred_labels[id])
  
  mlb = MultiLabelBinarizer()
  mlb.fit([CLASSES])
  gold = mlb.transform(gold)
  pred = mlb.transform(pred)

  macro_f1 = f1_score(gold, pred, average="macro", zero_division=1)
  micro_f1 = f1_score(gold, pred, average="micro", zero_division=1)
  return macro_f1, micro_f1

def validate_files(pred_files, gold_files, CLASSES):
  if not check_format_task1_task3(pred_file, CLASSES):
    logger.error('Bad format for pred file {}. Cannot score.'.format(pred_file))
    return False
  return True

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--gold_file_path",
    '-g',
    type=str,
    required=True,
    help="Paths to the file with gold annotations."
  )
  parser.add_argument(
    "--pred_file_path",
    '-p',
    type=str,
    required=True,
    help="Path to the file with predictions"
  )
  parser.add_argument(
    "--log_to_file",
    "-l",
    action='store_true',
    default=False,
    help="Set flag if you want to log the execution file. The log will be appended to <pred_file>.log"
  )
  parser.add_argument(
    "--classes_file_path", 
    "-c", 
    required=True, 
    help="The absolute path to the file containing all the labels categories."
  )
  args = parser.parse_args()

  pred_file = args.pred_file_path
  gold_file = args.gold_file_path

  if args.log_to_file:
    output_log_file = pred_file + ".log"
    logger.info("Logging execution to file " + output_log_file)
    fileLogger = logging.FileHandler(output_log_file)
    fileLogger.setLevel(logging.DEBUG)
    fileLogger.setFormatter(formatter)
    logger.addHandler(fileLogger)
    logger.setLevel(logging.DEBUG) #

  if not os.path.exists(args.classes_file_path):
    logger.errors("File doesnt exists: {}".format(classes_file_path))
    raise ValueError("File doesnt exists: {}".format(classes_file_path))
  CLASSES = read_classes(args.classes_file_path)

  if args.log_to_file:
    logger.info('Reading gold file')
  else:
    logger.info("Reading gold predictions from file {}".format(args.gold_file_path))
  if args.log_to_file:
    logger.info('Reading predictions file')
  else:
    logger.info('Reading predictions file {}'.format(args.pred_file_path))

  if validate_files(pred_file, gold_file, CLASSES):
    logger.info('Prediction file format is correct')
    macro_f1, micro_f1 = evaluate(pred_file, gold_file, CLASSES)
    logger.info("macro-F1={:.5f}\tmicro-F1={:.5f}".format(macro_f1, micro_f1))
    if args.log_to_file:
      print("{}\t{}".format(macro_f1, micro_f1))

