import tkinter as tk

import customtkinter as ctk
from tkinter import filedialog

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("650x450")
        self.title("TXT EDITOR")

        self.tab_to_filename = {}

        self.text_boxes = {}

        self.tabs = []
        self.tabs_names = []
        self.filecontent = []

        self.Counter = 0

        self.TextFrameWidth = 475
        self.TextFrameHeight = 450

        # below is the left sidebar, with pack_propagate is being used to keep its own size and not surround shit
        self.HomeBar = ctk.CTkFrame(self, height=450, fg_color="#242424")
        self.HomeBar.pack_propagate(False)
        self.HomeBar.pack(side="left")

        self.label = ctk.CTkLabel(self.HomeBar, text="Text Editor", font=("calibri", 30, "bold"))
        self.label.pack(side="top", pady=10)

        self.WriteButton = ctk.CTkButton(self.HomeBar, text="Write", command=self.Write)
        self.WriteButton.pack(side="bottom", pady=20)

        self.OpenButton = ctk.CTkButton(self.HomeBar, text="Open", command=self.Open)
        self.OpenButton.pack(side="bottom", pady=20)
        # The frame contains the text Content and other stuff
        self.ContentFrame = ctk.CTkTabview(self,height=self.TextFrameHeight, width=self.TextFrameWidth)
        self.ContentFrame.pack_propagate(False)
        self.ContentFrame.pack(side="right")

        self.FileNewButton = ctk.CTkButton(self.HomeBar, text="New File", command=self.TabSystem)
        self.FileNewButton.pack(side="bottom", pady=20)

    # the function below is activated when the Save button is pressed.

    def TabSystem(self):
        def e():
            self.TabFileName = str(self.promptentry.get())
            self.tab_to_filename[self.new_tab] = self.TabFileName
            self.tabs.append(self.TabFileName)
            self.prompt.destroy()

        self.Counter += 1
        self.TabFileName = None
        self.new_tab = self.ContentFrame.add("Tab " + str(self.Counter))

        self.tabs_names.append(self.ContentFrame.get())

        self.ContentFrame.set("Tab " + str(self.Counter))

        # prompt instantly disappears?

        #self.open_windows = []

        #self.open_windows.append(self.prompt)


        self.entry = ctk.CTkTextbox(self.new_tab, width=self.TextFrameWidth, height=self.TextFrameHeight)
        self.entry.pack(side="left")

        self.text_boxes[self.new_tab] = self.entry

        self.prompt = ctk.CTkToplevel(self)
        self.prompt.geometry("350x150")
        # IGNORE
        self.prompt.transient(self)

        self.promptframe = ctk.CTkFrame(self.prompt, fg_color="transparent")
        self.promptframe.pack()

        self.promptlabel = ctk.CTkLabel(self.promptframe, text="New file's name: ")

        self.promptentry = ctk.CTkEntry(self.promptframe)

        self.promptbutton = ctk.CTkButton(self.prompt, text="Next", command=e)

        self.promptlabel.pack(side="left", pady=30)
        self.promptentry.pack(side="left", padx=10)
        self.promptbutton.pack(side="bottom", pady=10, padx=10)

    def Write(self):
        self.FileType = ".txt"
        for tab_name, text_box in self.text_boxes.items():
            content = text_box.get(1.0, ctk.END)
            if "#include" in content:
                self.FileType = ".cpp"
            # Create a unique filename for each tab
            filename = f"{self.tab_to_filename[tab_name]}{self.FileType}"
            # Save the content to a file
            with open(filename, "w") as file:
                file.write(content)

    def Open(self):
        path = filedialog.askopenfilename(filetypes=[("All Files", "*")])
        if path:
            with open(path, "r") as file:
                self.entry.delete("1.0", ctk.END)
                self.entry.insert(ctk.END, file.read())


window = Window()
window.mainloop()