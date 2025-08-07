import os

def rotate_log(filename, max_size=10*1024):
    if filename in os.listdir() and os.stat(filename)[6] > max_size:
        os.rename(filename, filename.replace(".csv", ".bak"))

def log_to_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")
