from tkinter import*
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("633x366")
root.title("pycharm")
def myfunc():
    print("welcome")
def help():
    print(" i will help you")
    tmsg.showinfo("help","rutu will help you")
def rate():
    print("rate us")
    value=tmsg.askquestion("how are you?","what your experiance?")
    print("value")
#create menu
mainu_bar = Menu(root)

#create file menu
m1=Menu(mainu_bar,tearoff=0)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Open",command=myfunc)
root.config(menu=mainu_bar)                    #display file menu
mainu_bar.add_cascade(label="File",menu=m1)   #add m1 file in File menu

#create edit menu
m2 =Menu(mainu_bar, tearoff=0)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Cut",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainu_bar)                        #display edit menu
mainu_bar.add_cascade(label="Edit", menu=m2)   #add m2 file in edit menu

#create help menu
m3 =Menu(mainu_bar, tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
mainu_bar.add_cascade(label="Help", menu=m3)   #add m3 file in Help
root.config(menu=mainu_bar)                 #disply help menu
root.mainloop()