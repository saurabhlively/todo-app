import FreeSimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("Select files to compress: ")
input1=sg.Input()
choose_button1 = sg.FileBrowse("Choose",key='files')


label2 = sg.Text("Enter Destination Folder: ")
input2=sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key='folder')

compress_button=sg.Button('compress')
output_label = sg.Text(key="output",text_color="green")
window = sg.Window("File Compressor",
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],
                           [compress_button,output_label]])
while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed")
window.close()



