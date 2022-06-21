from PyPDF2 import PdfFileMerger

from tkinter import *
  
from tkinter import filedialog
  


files=[]
window = Tk()
filesToMerge=Label(window,width=50,text="",bg="white",fg="black")
location=Label(window,width=50,text="",bg="white",fg="black")
filename_entry=Entry(window,width=50)

errors=Label(window,text="",fg="red",bg="#c2cecd")

locationpath=[]

def browseFiles():
    
    filename = filedialog.askopenfilenames(initialdir = "/", title = "Select a File",
                                          filetypes = (("PDFs","*.pdf"),("All types","*.*")))
    print(len(filename))
    text1=""
    for mulfiles in filename:
        text1=text1+mulfiles+"\n "
        files.append(mulfiles)
    print(text1)
    filesToMerge.configure(text=text1)
    

def destFolder():
    filename = filedialog.askdirectory(initialdir = "/",
                                          title = "Select a File")
    location.configure(text=filename)
    locationpath.append(filename)
    print(filename)
      
def show():
    for i in files:
        print(i)

def merge():
    merger = PdfFileMerger()
    if len(files)<1 or len(files)==1:
        errors.configure(text="Error: Please select one or more files")
        print("No files selected")
    elif len(locationpath)==0:
        errors.configure(text="Error: Please enter destination path")
    elif filename_entry.get()=="":
        errors.configure(text="Error: Please enter destination filename")
    else:
        for pdfs in files:
            merger.append(pdfs)
        print(files)
        print(locationpath[0]+filename_entry.get())

        merger.write(locationpath[0]+"/"+filename_entry.get()+".pdf")
        locationpath.clear()
        

                                                                                                  
window.title('Pdf Merger')
  

#window.iconbitmap("Add icon file path to chenge the window icon")
window.config(background = "#c2cecd")
  

label_file_explorer = Label(window,
                            text = "Files to merge: ",
                        
                            fg = "black",
                            )


dest_folder= Label(window,
                            text = "Destination folder: ",
                        
                            fg = "black")

enter_filename=Label(window,text="Enter Destination filename: ",fg="black")

  
      
button_explore = Button(window,
                        text = "Select Files",
                        command = browseFiles,width=15,height=2)
  
button_merge = Button(window,
                     text = "Merge",
                     command = merge,
                     height=2,
                     width=10)

save_location=Button(window,text="Destination folder",command=destFolder,width=15,height=2)




label_file_explorer.grid(column = 0, row = 0,padx=(5,5),pady=(25,1),sticky="w") #Label
filesToMerge.grid(column=0,row=1,padx=(5,5),pady=(5,5),sticky="w") #Text entry
button_explore.grid(column = 1, row = 1,padx=(5,10)) #Button

dest_folder.grid(column=0,row=2,padx=(5,5),pady=(20,1),sticky="w") #Label 
location.grid(column=0,row=3,padx=(5,5),pady=(5,5)) #Text entry
save_location.grid(column=1,row=3,padx=(5,10))# Button

enter_filename.grid(column=0,row=4,padx=(5,5),pady=(20,1),sticky="w")
filename_entry.grid(column=0,row=5,padx=(5,5),pady=(5,5),sticky="w")

button_merge.grid(column = 0,row = 6,pady=(30,30)) #Merge button
errors.grid(column=0,row=7,pady=(10,10))

  
# Let the window wait for any events
window.mainloop()

#pyinstaller --clean --windowed --onefile PdfMerger.py  
#Pyinstaller version 4.10 works 5.1 does not work