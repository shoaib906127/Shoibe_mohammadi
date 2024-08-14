import tkinter as tk
from tkinter import filedialog, messagebox

# Function to save content to a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", tk.END))  # Get all text from the text widget
            messagebox.showinfo("Info", f"File saved successfully as {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

# Function to load content from a file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)  # Clear current content
                text_area.insert(tk.END, content)  # Insert new content
            messagebox.showinfo("Info", f"File loaded successfully from {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

# Create the main application window
root = tk.Tk()
root.title("using GUI appliction to save our unvircity homework")

# Create a text widget for writing
text_area = tk.Text(root, wrap='word', height=160, width=240)
text_area.pack(padx=10, pady=10)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
root.geometry("600x600")
# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=load_file)
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()