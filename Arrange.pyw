import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror



#create the window
wn = Tk()
wn.title("Computer-Arranger")
wn.geometry("700x500")
#wn.wm_iconbitmap('bookmark.ico')

#introduction text
intro_txt1 = Label(wn ,text="welcome to computer - arranger!                        ")
intro_txt2 = Label(wn ,text="this program will arrange your messy computer!\n")
intro_txt1.grid(row = 0,column = 0)
intro_txt2.grid(row = 1,column = 0)

def path():
    global files,new_path
    #print(os.getcwd())
    new_path = os.path.join(os.getcwd(),"..\\")
    os.chdir(new_path)
    new_path = os.path.join(os.getcwd(),"..\\")
    os.chdir(new_path)
    files = os.listdir(new_path)
    #print (files)
    return files


def choice_file():
    global folder
    label=Label(wn,text="Choose the folder you want to arrange:",bg='LightSteelBlue3', bd=1, relief=RAISED, width = 30)
    label.grid(row = 2,column = 0)

    folder=ttk.Combobox(wn,values=path(),width=15)
    folder.grid(row = 2,column = 1)
    


def check_arrange():
    global choose
    label=Label(wn,text="\n\n\n\n\n")
    label.grid(row = 3,column = 0)
    choices = ["arrange by name","arrange by ending","arrange by size"]
    choose=ttk.Combobox(wn,values=choices,width=20)
    choose.grid(row = 3,column = 0)


wn.counter = 0

def add_arrange():
    global letter,text
    space = Label(wn,text= "         ")
    choice = choose.get()
    wn.counter += 1
    if choice == "arrange by name":
        #print("<by name>")
        nr = wn.counter + 4
        lab=Label(wn,text= "put all the files contains the letters", bg='LightSteelBlue2', bd=1, relief=RAISED, width = 30)
        lab.grid(row = nr,column = 0)

        letter = Entry(wn,)
        letter.grid(row = nr,column = 1)
    
        lab2 = Label(wn,text= "in the fold", bg='LightSteelBlue2', bd=1, relief=RAISED, width = 10)
        lab2.grid(row = nr,column = 3)
        
        text = Entry(wn,)
        text.grid(row = nr,column = 4)
        


        


def new_button():
    add = Button(wn , text = "new",bd = "5", command = add_arrange, state = "normal")
    add.grid(row = 3,column = 1)

    
def start_button():
    start_b = Button(wn , text = "start",bd = "5", command = organize, state = "normal")
    start_b.grid(row = 3,column = 2)
    
def file_creator(f_name):
    flag = False
    files = os.listdir(new_path + "//" + folder_choice)
    #print(files)
    for file in files:
        if f_name.lower() == file.lower():
            showerror(title = "Error", message = "the files will organzie in an existing file!")
            flag = True
    if flag == False:
        #print(os.getcwd())
        os.chdir(new_path + "//" + folder.get())
        os.mkdir(f_name)
    
def replace_files(ffo,f_name,new_path):
    for file in ffo:
        #print(file)
        file_loc = new_path + "\\" + file 
        fif_loc = new_path + "\\" + f_name + "\\" + file
        #print("file location: ", file_loc)
        #print("file  location in folder: ",fif_loc)
        os.rename(file_loc,fif_loc)
        path()
        main()
        



def organize():
    global folder_choice
    ffo = []
    folder_choice = folder.get()
    new_path = os.path.join(os.getcwd(),folder_choice)
    #print(new_path)
    os.chdir(new_path)
    files = os.listdir(new_path)
    letters = letter.get()
    f_name = text.get()
    if letters != "" and text != "": 
        for file in files:
            if file.find(letters) != -1:
                ffo += [file]
        #print(ffo)
        
    else:
        showerror(title = "Error", message = "input is empty!")
    file_creator(f_name)
    replace_files(ffo, f_name,new_path)
def main():
    choice_file()

    check_arrange()

    new_button()

    start_button()

main()
wn.mainloop()

