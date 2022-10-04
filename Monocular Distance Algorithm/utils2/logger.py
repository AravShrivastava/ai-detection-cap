import numpy as np
import torch
import pickle

from os import listdir
from os.path import isfile, join
import re
from pathlib import Path
from utils2 import constants


def initialize():
    """
    Initialize dictionary with stats for logging.

    Returns:
    logs    -- Dictionary with defined keys
    """
    # Get dict with model stats
    stats_model = constants.model_stats()
    
    # Add inference time key and merge
    stats = {"inference_time":[]}
    stats.update(stats_model)
   
    return stats


def write_log(logs, time_begin, time_end, labels, conf, model_stats):
    """
    Writes log info into dictionary.

    Args:
    logs        -- Dictionary with log info
    time_begin  -- Begin of inference time for current frame
    time_end    -- End of inference time for current frame
    labels      -- Torch tensor with object label indices
    conf        -- Torch tensor with detection confidences
    model_stats -- Dictionary with model stats

    Return:
    logs        -- Updated dictionary with log information
    """

    stats = constants.model_stats()
    logs["inference_time"].append(time_end - time_begin)
    
    for stat in stats:
        logs[str(stat)].append(model_stats[stat])

    return logs


def save_logs(logs, name_in, model_type, lane_detection, distance_approximation):
    """
    Saves logs to disk.
    Default path is: dev/logs

    Args:
    logs        -- Dictionary with log data
    name_in     -- String of the input video without file extension. Is None in camera mode.
    model_type  -- String of the model name which was used with the input
    """

    if name_in is None:
        name_in = "camera"

    if model_type != None:
        name_in = name_in + "-"+ model_type

    if lane_detection is True:
        name_in = name_in + "-lanes"
    
    if distance_approximation is True:
        name_in = name_in + "-distances"

    # Set path out
    Path("logs").mkdir(parents=True, exist_ok=True)
    path_out = "logs"

    # Make new filename index for file with the same name
    # Get filenames in folder
    try:
        # Find all files in folder
        all_files = [f for f in listdir(path_out) if isfile(join(path_out, f))]
        # Find files with the same name as name_in
        existing_files = [f for f in all_files if f[:-8] == name_in]
    except FileNotFoundError:
        print("Folder for logs not found at \"" + path_out +  "\".\nCould not save logs!")
        exit()

    # Find indices
    existing_indices = []
    for f in existing_files:
        # Add only entries with 3 digits using regex
        res = re.findall("[0-9]+", f.split('.')[0][-3:])
        if len(res) == 1:
            existing_indices.append(int(res[0]))

    # New filename index is greatest existing one plus one
    if len(existing_indices) > 0:
        index_out = max(existing_indices) + 1
    else:
        index_out = 1
    
    # Set filename out with the index
    name_out = name_in + "-" + str(index_out).zfill(3)
        
    # Save file
    with open(path_out + "/" + name_out + ".log", 'wb') as handle:
        pickle.dump(logs, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("Logs saved as \"" + name_out +  "\" to path " + "\"dev/logs\".")