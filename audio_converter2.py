import os

def main():
    files= os.listdir("./")
    count=0
    list=[]
    for f in files:
        if f.lower()[-3:]=="aif":
                print("processing",f)
                process(f)
                count=count+1
                '''
                list.append(f)
                word=f.split("_")
                print(word[3])
                
                
    
    count2=0
    for i in list:
        if os.path.exists(i[:-3]+"aif"):
            os.remove(i[:-3]+"aif")
            count2= count2+1
     
   
    print("removed",count2)
'''
    print("converted",count)
def process(f):
    infile= f
    outfile= f[:-3]+"wav"
    cmd= "ffmpeg -i {} {}".format(infile, outfile)
    os.popen(cmd)

if __name__ == '__main__':
    main()
