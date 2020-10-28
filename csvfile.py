import csv
import os

def exportCsv(file,x,y):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    li = []
    li.append([x])
    write = open(my_file,'w')
    write.write(str(['x','y']))
    for l in range(len(li)):
        write.write(str(li[l]))