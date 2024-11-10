import os
contents = ["My Name is "
            "Saurabh",
            "I am working in Barclays",
            "I have total 15 years of exp" ]
filenames = ['name','company','experience']


for content,filename in zip(contents,filenames):
     file = open(f"files/{filename}","w")
     file.write(content)
     file.close()