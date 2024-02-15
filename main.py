import tkinter as tk
import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("650x450")
        self.title("TXT EDITOR")

        self.TextFrameWidth = 475
        self.TextFrameHeight = 450

        # below is the left side bar, with pack_propagate is being used to keep its own size and not surround shit
        self.HomeBar = ctk.CTkFrame(self, height=450)
        self.HomeBar.pack_propagate(False)
        self.HomeBar.pack(side="left")

        self.label = ctk.CTkLabel(self.HomeBar, text="Text Editor", font=("calibri", 30, "bold"))
        self.label.pack(side="top")

        # The frame contains the text Content and other stuff
        self.ContentFrame = ctk.CTkScrollableFrame(self,height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.ContentFrame.pack(side="right")

        self.entry = ctk.CTkTextbox(self.ContentFrame, height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.entry.pack(side="left")
    # the function below is activated when the Save button is pressed
    def Write(self):
        pass

window = Window()
window.mainloop()