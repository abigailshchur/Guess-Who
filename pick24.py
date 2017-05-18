from os import rename, listdir, makedirs
from os.path import isfile, join
import os
import random
from shutil import copyfile
import glob
import sys

def main(dir_name):
  all_images = [f for f in listdir("./all_images/") if isfile(join("./all_images/", f))]
  random24 = random.sample(all_images, 24)
  if not os.path.exists(dir_name):
    makedirs(dir_name)
  for i in glob.glob("./"+dir_name+"/*"):
    os.remove(i)
  for i in range(len(random24)):
    copyfile("./all_images/"+random24[i], "./"+dir_name+"/pic"+str(i)+".jpg")

if __name__ == "__main__":
  if (len(sys.argv) == 1):
    filename = "new_pics"
  else:
    filename = sys.argv[1]
  main(filename)
