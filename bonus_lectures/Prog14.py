filenames = ['1.doc','1.report','1.presentation']
#output should be
# ['1-doc.txt','1-report.txt','1-presentation.txt']
filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
print(filenames)
