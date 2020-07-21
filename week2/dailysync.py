#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool
import os

# function to backup data
def backup(src):
    # destination directory
    dest = os.getcwd() + "/data/prod_backup/"
    print ("Backing up data from {} to {}.".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    # get source directory
    src = os.getcwd() + "/data/prod/"
    # list files
    list_of_files = os.listdir(src)
    #list of all files
    all_files = []

    # iterating through files
    for value in list_of_files:
        # getting the full file path
        full_path = os.path.join(src, value)
        all_files.append(full_path)

    # mutiprocessing using Pool
    with Pool(len(all_files)) as pool:
        pool.map(backup, all_files)

