import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r") as f:
        return json.load(f)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Refresh listbox
def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in load_contacts():
        contact_list.insert(tk.END, f"{contact['name']} | {contact['phone']} | {contact['email']}")

# Add a contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Missing Info", "Name and Phone are required!")
        return

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    refresh_list()
    clear_entries()
    messagebox.showinfo("Success", f"Contact '{name}' added.")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return

    selected_text = contact_list.get(selected[0])
    name = selected_text.split('|')[0].strip()

    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    save_contacts(new_contacts)
    refresh_list()
    messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# -------- GUI Setup --------
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("400x450")
root.resizable(False, False)

# Title
tk.Label(root, text="Contact Book", font=("Arial", 16, "bold")).pack(pady=10)

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack(fill=tk.X, padx=20)

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack(fill=tk.X, padx=20)

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack(fill=tk.X, padx=20)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, bg="lightgreen").pack(pady=10)
tk.Button(root, text="Delete Selected", command=delete_contact, bg="salmon").pack()

# Contact list
tk.Label(root, text="Saved Contacts").pack(pady=5)
contact_list = tk.Listbox(root, width=50)
contact_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Load existing contacts on startup
refresh_list()

# Run the app
root.mainloop()
