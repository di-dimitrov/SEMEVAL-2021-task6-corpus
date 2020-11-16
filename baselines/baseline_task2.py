dev_file = "../data/dev_set_task2.txt"
propaganda_techniques_file = "../techniques_list_task1-2.txt" 
task_2_output_file = "baseline-output-task2.txt"

#dev_file = "../data/training_set_task2.txt" 		# this is to run baseline
#task_2_output_file = "baseline-output-task2-train.txt" 	# on the training set

#
# Baseline task 2: create random spans for the development set
#
#
#

import sys
import json
import random

random.seed(42) # to make runs deterministic

try:
    with open(dev_file, "r") as f:
        jsonobj = json.load(f)
except:
    sys.exit("ERROR: cannot load json file")

with open(propaganda_techniques_file, "r") as f:
    propaganda_techniques_names = [ line.rstrip() for line in f.readlines() if len(line)>2 ]

for example in jsonobj:
        start_fragment, end_fragment, text_length = (0, 0, len(example['text']))
        current_example_annotations = []
        while end_fragment < text_length:
            if end_fragment > 0:
                technique_name = propaganda_techniques_names[random.randint(0, len(propaganda_techniques_names)-1)]
                # check that there is no other annotation for the same anrticle and technique that overlaps
                intersection_length = 0
                if len(current_example_annotations) > 0:
                    span_annotation = set(range(start_fragment, end_fragment))
                    intersection_length = sum( [ len(span_annotation.intersection(set(range(start_fragment, end_fragment)))) for previous_technique, start_fragment, end_fragment in current_example_annotations if previous_technique==technique_name ])
                if len(current_example_annotations) == 0 or intersection_length > 0:
                    current_example_annotations.append((technique_name, start_fragment, end_fragment))
            start_fragment += random.randint(0, max(1, text_length-start_fragment))
            end_fragment = min(start_fragment + random.randint(1, text_length-start_fragment+1), text_length)
        example['labels'] = [ {"technique":l, "start":s, "end":e} for l,s,e in current_example_annotations ]
        print("example %s: added %d fragments" % (example['id'], len(current_example_annotations)))    

with open(task_2_output_file, "w") as fout:
    json.dump(jsonobj, fout, indent=4)
print("Predictions written to file " + task_2_output_file)
