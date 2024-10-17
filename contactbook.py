import sqlite3

# Database setup
conn = sqlite3.connect('.venv/contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)''')
conn.commit()


# Functions
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    if name and phone:
        c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                  (name, phone, email, address))
        conn.commit()
        print("Contact added successfully!")
    else:
        print("Name and Phone are required fields.")


def view_contacts():
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    for row in rows:
        print(row)


def search_contact():
    search_term = input("Enter name or phone to search: ")
    c.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
              ('%' + search_term + '%', '%' + search_term + '%'))
    rows = c.fetchall()
    for row in rows:
        print(row)


def update_contact():
    contact_id = input("Enter the ID of the contact to update: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")
    c.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
              (name, phone, email, address, contact_id))
    conn.commit()
    print("Contact updated successfully!")


def delete_contact():
    contact_id = input("Enter the ID of the contact to delete: ")
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully!")


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
