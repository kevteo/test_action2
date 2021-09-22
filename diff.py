import os
import json
# from apps.util import json_merge, generate_number_changes
from flatten_json import flatten
from jsonmerge import Merger
from jsondiff import diff
from git import Repo

def json_merge(base, new, merge_strategy):
    schema = {'mergeStrategy': merge_strategy}
    merger = Merger(schema)
    base = merger.merge(base, new)
    return base

def generate_number_changes(difference_history):
    num_changes = {}
    for difference in difference_history:
        if type(difference) is list:
            continue
        
        for key in difference.keys():
            if key in num_changes:
                num_changes[key] +=1 
            else:
                num_changes[key] = 1
    return num_changes

def main():
    # Read Inputs
    merge_strategy = str(os.environ["INPUT_MERGE_STRATEGY"])

    # Print inputs
    print("Merge Strategy: ", merge_strategy)
    
    # Read Files
    with open('json1.json') as f:
        json1 = json.load(f)
    with open('json2.json') as f:
        json2 = json.load(f)
    
    # Flatten, Merge, Difference & Number of changes per key
    base = None
    json1 = flatten(json1)
    json2 = flatten(json2)
    base = json_merge(base, json1, merge_strategy)
    base = json_merge(base, json2, merge_strategy)
    difference = diff(json1, json2, syntax='symmetric', marshal=True)
    num_changes = generate_number_changes(difference)
    
    # Write Files
    with open('merged_json.json', 'w', encoding='utf-8') as f:
        json.dump(base, f, ensure_ascii=False, indent=4)
    with open('difference.json', 'w', encoding='utf-8') as f:
        json.dump(difference, f, ensure_ascii=False, indent=4)
    with open('num_changes.json', 'w', encoding='utf-8') as f:
        json.dump(num_changes, f, ensure_ascii=False, indent=4)
    
    # Push to Git
    repo = Repo('.')
    repo.git.reset()
    repo.index.add(['merged_json.json', 'difference.json', 'num_changes.json'])
    repo.index.commit('Upload Merged Json')
    origin = repo.remote('origin')
    origin.push()
    repo.index.add(['json1.json', 'json2.json'])

if __name__ == "__main__":
    main()
