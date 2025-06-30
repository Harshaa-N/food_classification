import os
os.chdir('Prawn_fry')
i=1
for file in os.listdir():
    src=file
    dst="Prawn_fry "+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

