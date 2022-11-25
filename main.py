import pymysql

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk




# User Interface
root = Tk()
root.title("Anime Managment System")
root.geometry("1280x720")
root.configure(bg = "#2f2f2f")
tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)


def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='anime_db',
    )
    return conn

def refreshTable():
    for data in tree.get_children():
        tree.delete(data)

    for array in read():
        tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE', font=('Verdana', 13))
    tree.grid(row=10, column=0, columnspan=5, rowspan=11, padx=20, pady=20)
    
def returnInitialState():
    try:
        animeNameInput.delete(0, tk.END)
        animeGenresInput.delete(0, tk.END)
        animeAuthorInput.delete(0, tk.END)
        numberOfSeasonsInput.delete(0, tk.END)
    except:
        messagebox.showinfo("Error", "Something Went Wrong")
        return;    
            

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animes")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results    



def add():
    animeName = str(animeNameInput.get())
    animeGenre = str(animeGenresInput.get())
    animeAuthor = str(animeAuthorInput.get())
    numberOfSeasons = str(numberOfSeasonsInput.get())

    if  (animeName == "" or animeName == " ") or (animeGenre == "" or animeGenre == " ") or (animeAuthor == "" or animeAuthor == " ") or (numberOfSeasons == "" or numberOfSeasons == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animes(ANIME_NAME,GENRES,AUTHOR,NUMBER_OF_SEASONS) VALUES ('"+animeName+"','"+animeGenre+"','"+animeAuthor+"','"+numberOfSeasons+"') ")
            conn.commit()
            conn.close()
            
        except:
            messagebox.showinfo("Error", "Anime ID already exist")
            return

    refreshTable()
    returnInitialState()

def delete():
    decision = messagebox.askquestion("Warning!!", "Are you sure you want to delete this item ?")
    if decision != "yes":
        return 
    else:
        selected_item = tree.selection()[0]
        deleteData = str(tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM animes WHERE ANIMEID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()    

        
def select():
    try:
        selected_item = tree.selection()[0]
        animeId = str(tree.item(selected_item)['values'][0])
        animeName = str(tree.item(selected_item)['values'][1])
        animeGenres = str(tree.item(selected_item)['values'][2])
        animeAuthor = str(tree.item(selected_item)['values'][3])
        numberOfSeasons = str(tree.item(selected_item)['values'][4])

        setph(animeId,1)
        setph(animeName,2)
        setph(animeGenres,3)
        setph(animeAuthor,4)
        setph(numberOfSeasons,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")        
        
def update():
    selectedAnimeid = ""

    try:
        selected_item = tree.selection()[0]
        selectedAnimeid = str(tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    animeName = str(animeNameInput.get())
    animeGenres = str(animeGenresInput.get())
    animeAuthor = str(animeAuthorInput.get())
    numberOfSeasons = str(numberOfSeasonsInput.get())

    if  (animeName == "" or animeName == " ") or (animeGenres == "" or animeGenres == " ") or (animeAuthor == "" or animeAuthor == " ") or (numberOfSeasons == "" or numberOfSeasons == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE animes SET ANIMEID='"+
            selectedAnimeid+"', ANIME_NAME='"+
            animeName+"', GENRES='"+
            animeGenres+"', AUTHOR='"+
            animeAuthor+"',  NUMBER_OF_SEASONS='"+
            numberOfSeasons+"' WHERE ANIMEID='"+
            selectedAnimeid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Anime ID already exist")
            return

    refreshTable()        

label = Label(root,text="Anime Managment System (CRUD application) ", font=('Verdana Bold',25) , background="#2f2f2f" , foreground="#fe6f27")
label.grid(row= 0,column=0,rowspan = 2,columnspan=8,padx=200,pady=40)

#animeIdLabel = Label(root,text="Anime ID",font=('Verdana',18), background="#2f2f2f", foreground="#fe6f27")
animeNameLabel = Label(root,text="Anime Name",font=('Verdana',18), background="#2f2f2f", foreground="#fe6f27")
animeGenresLabel = Label(root,text="Anime Genres",font=('Verdana',18), background="#2f2f2f", foreground="#fe6f27")
animeAuthorLabel  = Label(root,text="Anime Author",font=('Verdana',18), background="#2f2f2f", foreground="#fe6f27")
numberOfSeasonsLabel = Label(root,text="Number of Seasons",font=('Verdana',18), background="#2f2f2f", foreground="#fe6f27")


#animeIdLabel.grid(sticky = W,row= 3,column=0,columnspan=1,padx=90,pady=5)
animeNameLabel.grid(sticky = W,row= 4,column=0,columnspan=1,padx=90,pady=5)
animeGenresLabel.grid(sticky = W,row= 5,column=0,columnspan=1,padx=90,pady=5)
animeAuthorLabel.grid(sticky = W,row= 6,column=0,columnspan=1,padx=90,pady=5)
numberOfSeasonsLabel.grid(sticky = W,row= 7,column=0,columnspan=1,padx=90,pady=5)

animeNameInput = Entry(root,width= 60,bd=5,font=("Ariel",18), textvariable = ph2)
animeGenresInput = Entry(root,width= 60,bd=5,font=("Ariel",18), textvariable = ph3)
animeAuthorInput = Entry(root,width= 60,bd=5,font=("Ariel",18), textvariable = ph4)
numberOfSeasonsInput = Entry(root,width= 60,bd=5,font=("Ariel",18), textvariable = ph5)


#animeIdInput.grid(row= 3,column=1,columnspan=4,padx=10,pady=0)
animeNameInput.grid(row= 4,column=1,columnspan=4,padx=10,pady=0)
animeGenresInput.grid(row= 5,column=1,columnspan=4,padx=10,pady=0)
animeAuthorInput.grid(row= 6,column=1,columnspan=4,padx=10,pady=0)
numberOfSeasonsInput.grid(row= 7,column=1,columnspan=4,padx=10,pady=0)

spacer = Label(root, text=None, background="#2f2f2f", foreground="#fe6f27")
spacer.grid(row=8, column=0)


addBtn = Button(root,text="Add",padx=25,pady=5,width=5,bd=5,font =
               ('calibri', 17, 'bold',),bg="#ffa67e",foreground="#5a0f2e",borderwidth = '2',command=add)
updateBtn = Button(root,text="Update",padx=25,pady=5,width=5,bd=5,font =
               ('calibri', 17, 'bold',),bg="#ffa67e",foreground="#5a0f2e",borderwidth = '2',command=update)
deleteBtn = Button(root,text="Delete",padx=25,pady=5,width=5,bd=5,font =
               ('calibri', 17, 'bold',),bg="#ffa67e",foreground="#5a0f2e",borderwidth = '2',command=delete)
selectBtn = Button(root,text="Select",padx=25,pady=5,width=5,bd=5,font =
               ('calibri', 17, 'bold',),bg="#ffa67e",foreground="#5a0f2e",borderwidth = '2',command=select)
resetBtn = Button(root,text="Reset",padx=15,pady=2,width=5,bd=5,font =
               ('calibri', 17, 'bold',),bg="#220070",foreground="#ffffff",borderwidth = '2',command=returnInitialState)

addBtn.grid(row=9,column=1,columnspan=1)
updateBtn.grid(row=9,column=2,columnspan=1)
deleteBtn.grid(row=9,column=3,columnspan=1)
selectBtn.grid(row=9,column=4,columnspan=1)
resetBtn.grid(row=9,column=0,columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

tree['columns'] = ("Anime ID","animeName","animeGenres","animeAuthor","numberOfSeasons")

tree.column("#0", width=0, stretch=NO)
tree.column("Anime ID", anchor=W, width=150)
tree.column("animeName", anchor=W, width=150)
tree.column("animeGenres", anchor=W, width=460)
tree.column("animeAuthor", anchor=W, width=165)
tree.column("numberOfSeasons", anchor=W, width=150)

tree.heading("Anime ID", text="Anime ID", anchor=W)
tree.heading("animeName", text="Anime Name", anchor=W)
tree.heading("animeGenres", text="Genres", anchor=CENTER)
tree.heading("animeAuthor", text="Author", anchor=CENTER)
tree.heading("numberOfSeasons", text="N° Of Seasons", anchor=CENTER)


refreshTable()

root.mainloop()