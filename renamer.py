import os
import re
import platform
import random
# dir = os.path.dirname(__file__)
usr = os.getlogin()
basedir = '/home/'+usr+'/Downloads/'
if platform.system() == "Windows":
    basedir = 'C:/Downloads/'

for dir in os.listdir(basedir):
    org = os.path.join(basedir, dir)
    if not os.path.isdir(os.path.join(basedir, dir)):
        continue
    if not re.match("CoursePage-Material_", dir):
        continue
    else:
        dir = (re.findall("\\_\w{3}\d{4}\\_", dir)[0].strip("_"))
        dir = os.path.join(basedir, dir)
        try:
            os.rename(org, dir)
        except:
            dir = os.rename(org, dir+"_"+str.format(random.randint(1, 1000)))
        files = os.listdir(os.path.join(basedir, dir))
        for i in files:
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
            except:
                try:
                    name = (re.split("_\d", re.split("REFERENCE_MATERIAL_", name)[1])[
                        0] + "_Syllabus")
                except:
                    print("Some error")
                # print("Not handled")

            name = name.strip(" ")
            name += ext

            os.rename(os.path.join(dir, i), os.path.join(dir, name))
