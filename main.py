import tkinter as tk
import customtkinter as ctk

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

        # The frame contains the text Content and other stuff
        self.ContentFrame = ctk.CTkScrollableFrame(self,height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.ContentFrame.pack(side="right")

        self.entry = ctk.CTkTextbox(self.ContentFrame, height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.entry.pack(side="left")

    # the function below is activated when the Save button is pressed.
    def Write(self):
        self.TextContent = str(self.entry.get(1.0, "end"))
        self.DefaultFileType = ".txt"
        self.FileName = "file"
        if self.TextContent.find("#include") != -1:
            self.DefaultFileType = ".cpp"

        with open(self.FileName+self.DefaultFileType, "w") as file:
            file.write(self.TextContent)

window = Window()
window.mainloop()