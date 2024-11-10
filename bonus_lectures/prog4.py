filenames = ["1.raw_data.txt","2.Reports.txt","3.Presentation.txt"]
filename_new = []

for filename in filenames:
    #Changing first dots of eah filename to _
    replaced_f = filename.replace(".","_",1)
    print(replaced_f)
    filename_new.append(replaced_f)
    print(filename_new)
