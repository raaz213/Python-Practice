

import json
import os

CONTACT_FILE = "contacts.json"

# 📦 Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r") as file:
        return json.load(file)

# 💾 Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# ➕ Add a contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

# 📄 View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()

# ❌ Delete a contact by name
def delete_contact():
    name = input("Enter name of contact to delete: ").strip()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(contacts) == len(new_contacts):
        print("❌ Contact not found.")
    else:
        save_contacts(new_contacts)
        print(f"🗑️ Contact '{name}' deleted successfully!")

# 🧭 Main menu
def menu():
    while True:
        print("\n📱 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")

# 🚀 Run the app
if __name__ == "__main__":
    menu()
