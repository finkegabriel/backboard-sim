import csv
import os

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def exportCsv(file,x,y,z):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    # write = open(my_file,'w')
    with open(file, 'w') as csvfile: 
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile)         
    # writing the fields 
        csvwriter.writerow(['x','y','z']) 
    # writing the data rows 
        # row = [chunks(x,3),chunks(y,3),chunks(z,3)]
        xx = chunks(x,3)
        yy = chunks(y,3)
        zz = chunks(z,3)
        row = [
            xx,yy,zz
        ]
        # print(row)
        # # for l in xx:
        # for xxx in xx:
        #     for yyy in yy:
        #         for zzz in zz:  
        #             csvwriter.writerows([xxx,yyy,zzz])