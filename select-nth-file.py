from os import listdir, mkdir, rmdir
from os.path import isfile, join, isdir
import shutil

path = input("Path: ")
n = int(input("n: "))
files = [f for f in listdir(path) if isfile(join(path, f))]

if isdir(path+"/selected"):
    rmdir(path + "/selected")
mkdir(path + "/selected")

for i, file in enumerate(files):
    if i % n == 0:
        shutil.copy(path + "/" + file, path + "/selected")
print(len(listdir(path + "/selected")), "files copied")