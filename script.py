import os

print("To run, uncomment the code in here.")

with open("1.20.txt", "w") as o: #open file in write mode (w)
    for dirpath,_,filenames in os.walk(os.getcwd() + "/assets/minecraft"): #uhh
        for f in filenames: #?
            o.write(os.path.abspath(os.path.join(dirpath, f))[len(os.getcwd() + "/assets/minecraft/"):] + "\n") #i dont know python help

print("Success") #i sure fucking hope it worked