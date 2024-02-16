import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("650x450")
        self.title("TXT EDITOR")

        self.TextFrameWidth = 475
        self.TextFrameHeight = 450

        # below is the left sidebar, with pack_propagate is being used to keep its own size and not surround shit
        self.HomeBar = ctk.CTkFrame(self, height=450)
        self.HomeBar.pack_propagate(False)
        self.HomeBar.pack(side="left")

        self.label = ctk.CTkLabel(self.HomeBar, text="Text Editor", font=("calibri", 30, "bold"))
        self.label.pack(side="top", pady=10)

        self.WriteButton = ctk.CTkButton(self.HomeBar, text="Write", command=self.Write)
        self.WriteButton.pack(side="bottom", pady=20)

        self.OpenButton = ctk.CTkButton(self.HomeBar, text="Open", command=self.Open)
        self.OpenButton.pack(side="bottom", pady=25)
        # The frame contains the text Content and other stuff
        self.ContentFrame = ctk.CTkScrollableFrame(self,height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.ContentFrame.pack(side="right")

        self.entry = ctk.CTkTextbox(self.ContentFrame, height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.entry.pack(side="left")

    # the function below is activated when the Save button is pressed.
    def Write(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            with open(path, "w") as file:
                file.write(self.entry.get("1.0", ctk.END))
    
    def Open(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            with open(path, "r") as file:
                self.entry.delete("1.0", ctk.END)
                self.entry.insert(ctk.END, file.read()) 

    
window = Window()
window.mainloop()
