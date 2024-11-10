import glob

"""Used to filter files as per extension in python from directory"""
myfiles = glob.glob("files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath,'r') as f:
        print(f.read().upper())


