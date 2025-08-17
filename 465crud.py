


import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["LibraryDB"]
    collection = db["Books"]
except Exception as e:
    messagebox.showerror("Connection Error", f"Could not connect to MongoDB:\n{str(e)}")



def insert_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    status = entry_status.get()

    if title and author and year and status:
        collection.insert_one({"title": title, "author": author, "year": year, "status": status})
        messagebox.showinfo("Success", "Book Inserted!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def read_books():
    text_area.delete("1.0", tk.END)
    records = collection.find()
    for r in records:
        text_area.insert(tk.END, f"Title: {r['title']}, Author: {r['author']}, Year: {r['year']}, Status: {r['status']}\n")

def update_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    status = entry_status.get()

    if title:
        collection.update_one(
            {"title": title},
            {"$set": {"author": author, "year": year, "status": status}}
        )
        messagebox.showinfo("Success", "Book Updated!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter Book Title to Update.")

def delete_book():
    title = entry_title.get()
    if title:
        collection.delete_one({"title": title})
        messagebox.showinfo("Success", "Book Deleted!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter Book Title to Delete.")

def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_status.delete(0, tk.END)



root = tk.Tk()
root.title("Library Management System (465  CRUD with MongoDB)")
root.geometry("1500x1500")


tk.Label(root, text="Book Title").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Label(root, text="Author").pack()
entry_author = tk.Entry(root)
entry_author.pack()

tk.Label(root, text="Year of Publication").pack()
entry_year = tk.Entry(root)
entry_year.pack()

tk.Label(root, text="Status (Available/Issued)").pack()
entry_status = tk.Entry(root)
entry_status.pack()


tk.Button(root, text="Insert", command=insert_book).pack(pady=5)
tk.Button(root, text="Read", command=read_books).pack(pady=5)
tk.Button(root, text="Update", command=update_book).pack(pady=5)
tk.Button(root, text="Delete", command=delete_book).pack(pady=5)


text_area = tk.Text(root, height=15, width=70)
text_area.pack()

root.mainloop()
