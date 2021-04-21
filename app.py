import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os


root = tk.Tk()
apps = []


def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    if filename:
        if filename in apps:
            messagebox.showerror("Error", "Filename already exists")
        else:
            apps.append(filename)
            label = tk.Label(frame, text=filename)
            label.pack()
            remButton = tk.Button(frame, text="Remove File",
                                  padx=5, pady=2, fg="white", bg="#263d42", command=lambda: remApp(filename))
            remButton.pack()
            print(apps)


def runApps():
    for app in apps:
        os.startfile(app)


def loadApps():
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()
        remButton = tk.Button(frame, text="Remove File",
                              padx=5, pady=2, fg="white", bg="#263d42", command=lambda: remApp(app))
        remButton.pack()


def remApp(app):
    apps.remove(app)
    print(f'remApp {apps}')
    # loadApps()
    for widgets in frame.winfo_children():
        widgets.destroy()
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()
        remButton = tk.Button(frame, text="Remove File",
                              padx=5, pady=2, fg="white", bg="#263d42", command=lambda: remApp(app))
        remButton.pack()


canvas = tk.Canvas(root, height=700, width=700, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263d42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263d42", command=runApps)

runApps.pack()

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        apps = tempApps.split(',')
        apps.pop()
        print(apps)
        # loadApps()
        for app in apps:
            label = tk.Label(frame, text=app)
            label.pack()
            remButton = tk.Button(frame, text="Remove File",
                                  padx=5, pady=2, fg="white", bg="#263d42", command=lambda: remApp(app))
            remButton.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
