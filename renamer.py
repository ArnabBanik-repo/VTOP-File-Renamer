import os
import re
import platform
import random
from zipfile import ZipFile
# dir = os.path.dirname(__file__)
usr = os.getlogin()
basedir = '/home/'+usr+'/Downloads/'
if platform.system() == "Windows":
    basedir = 'C:/Users/'+usr+'/Downloads/'

for dir in os.listdir(basedir):
    if not re.match("CoursePage-Material_", dir):
        continue
    if not os.path.isdir(os.path.join(basedir, dir)):
        if os.path.splitext(dir)[1] == '.zip':
            with ZipFile(os.path.join(basedir, dir), 'r') as zObject:
                zObject.extractall(path=os.path.join(
                    basedir, os.path.splitext(dir)[0]))
            dir = os.path.splitext(dir)[0]
            # print(dir)
        else:
            continue
    if os.path.isdir(os.path.join(basedir, dir)):
        org = os.path.join(basedir, dir)
        dir = (re.findall("\\_\w{3}\d{4}\\_", dir)[0].strip("_"))
        dir = os.path.join(basedir, dir)
        try:
            os.rename(org, dir)
        except:
            dir = dir+"_"+str(random.randint(1, 1000))
            os.rename(org, dir)
        files = os.listdir(os.path.join(basedir, dir))
        k = 1
        for i in files:
            if (os.path.isdir(os.path.join(basedir, dir, i))):
                continue
            if i == 'renamer.py':
                continue
            name, ext = os.path.splitext(i)
            try:
                name = re.split("\d{2}-\d{2}-\d{4}_", name)[1]
                name = re.split(
                    "^\d+\W*\d*\\_*", name)[1] if re.match("^\d+\W*\d*\\_*", name) else name
                name = re.sub("(\\_)\d*", " ", name)
                name = re.sub("-\d+", "", name)
                name = re.sub("\s+", " ", name)
                name = re.sub("\s+\W", "", name)
                name = name.capitalize()
            except:
                try:
                    name = (re.split("_\d", re.split("VL\d{13}", name)[1])[
                        0] + "_Syllabus")
                    # print(name)
                except:
                    # print("Some error")
                    name = "Syllabus"
                # print("Not handled")

            name = re.sub("\\)", "", name)
            name = name.strip(" ")
            # name += ext
            if not os.path.exists(os.path.join(dir, name + ext)):
                os.rename(os.path.join(dir, i), os.path.join(dir, name + ext))
            else:
                os.rename(os.path.join(dir, i), os.path.join(
                    dir, name + "_" + str(k) + ext))
                k += 1
            # print(name+"."+ext)
