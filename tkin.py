import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def initialize_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, email):
    """Add a new user to the database."""
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")
    conn.close()
    update_user_list()  # Refresh the user list after adding a user

def delete_user(user_id):
    """Delete a user from the database based on their ID."""
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    if cursor.rowcount:
        messagebox.showinfo("Success", "User deleted successfully!")
    else:
        messagebox.showwarning("Warning", "No user found with that ID.")
    conn.close()
    update_user_list()  # Refresh the user list after deleting a user

def view_users():
    """Fetch all users from the database."""
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_list():
    """Update the Treeview widget to display all users."""
    for row in tree.get_children():
        tree.delete(row)

    users = view_users()
    for user in users:
        tree.insert('', tk.END, iid=user[0], values=(user[0], user[1], user[2], ''))

def on_add_button_click():
    """Callback for Add User button."""
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        add_user(name, email)
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def on_delete_button_click():
    """Callback for Delete User button."""
    user_id = id_entry.get()
    if user_id:
        try:
            user_id = int(user_id)
            delete_user(user_id)
            id_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid ID.")
    else:
        messagebox.showwarning("Input Error", "Please enter an ID.")

def on_refresh_button_click():
    """Callback for Refresh List button."""
    update_user_list()

def on_treeview_click(event):
    """Handle row selection in the Treeview."""
    item = tree.identify_row(event.y)
    if item:
        # Deselect all rows
        for row in tree.get_children():
            current_values = tree.item(row, 'values')
            tree.item(row, values=(current_values[0], current_values[1], current_values[2], ''))
        
        # Select the clicked row
        current_values = tree.item(item, 'values')
        tree.item(item, values=(current_values[0], current_values[1], current_values[2], 'Selected'))
        # Set the ID Entry to the selected ID
        id_entry.delete(0, tk.END)
        id_entry.insert(0, current_values[0])

# Initialize the database
initialize_db()

# Create the main window
root = tk.Tk()
root.title("User Management System")
root.geometry("600x400")

# Create a frame to hold buttons and pack it to the bottom
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10, fill=tk.X)

# Add buttons to the frame
tk.Button(button_frame, text="Add User", command=on_add_button_click).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete User", command=on_delete_button_click).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Refresh List", command=on_refresh_button_click).pack(side=tk.LEFT, padx=5)

# Create and pack widgets
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="ID (for delete):").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack(pady=5)

# Create a Treeview widget for displaying users
tree = ttk.Treeview(root, columns=('ID', 'Name', 'Email', 'Select'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.heading('Select', text='Select')

tree.column('ID', width=50, anchor=tk.CENTER)
tree.column('Name', width=150, anchor=tk.W)
tree.column('Email', width=250, anchor=tk.W)
tree.column('Select', width=100, anchor=tk.CENTER)

tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Bind Treeview click event
tree.bind('<ButtonRelease-1>', on_treeview_click)

# Initial population of the Treeview
update_user_list()

# Start the Tkinter event loop
root.mainloop()
