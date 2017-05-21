from os import rename, listdir, makedirs
from os.path import isfile, join
import os
import random
from shutil import copyfile
import glob
import sys
import pandas as pd
import json

def main(dir_name):
  all_images = [f for f in listdir("./all_images/") if isfile(join("./all_images/", f))]
  random24 = random.sample(all_images, 24)
  if not os.path.exists(dir_name):
    makedirs(dir_name)
  for i in glob.glob("./"+dir_name+"/*"):
    os.remove(i)
  for i in range(len(random24)):
    copyfile("./all_images/"+random24[i], "./"+dir_name+"/pic"+str(i)+".jpg")
  labels = pd.read_csv("pics3_labeling-100v2.csv")
  cols = list(labels)[2:]
  data = {}
  for i in range(24):
    data["pic"+str(i)] = []
    index = -1
    count = 0
    for j in labels["Name"]:
      if random24[i][0:len(random24[i])-9]==j[0:len(j)-1]:
        index=count
      count+=1
    for c in cols:
      if (labels[c][index]=="Y"):
        data["pic"+str(i)].append({c:"yes"})
      else:
        data["pic"+str(i)].append({c:"no"})
  with open("./"+dir_name+"/data.json", 'w') as outfile:
    json.dump(data, outfile)


if __name__ == "__main__":
  if (len(sys.argv) == 1):
    filename = "new_pics"
  else:
    filename = sys.argv[1]
  main(filename)
