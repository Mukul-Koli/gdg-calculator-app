import tkinter as tk
import math

pi = math.pi
sympi = "π"
fsize = 18
font = "consolas"

modes_btnframe_cfg = {
    "light" : {"cfg": {"bg" : "gray80", "bd":0}},
    "dark" : {"cfg": {"bg" : "black", "bd":0}},
}
modes_screen_cfg = {
    "light" : {"cfg": {"bg" : "gray80", "fg" : "black", "font":(font, fsize + 10), "bd":0}},
    "dark" : {"cfg": {"bg" : "gray10", "fg" : "white", "font":(font, fsize + 10), "bd":0}},
}

class Button(tk.Button):
    objlst = []
    maxlen = 0
    current_mode_index = 0
    current_mode = ""

    def __init__(self, master, text="", **cfg):
        self.modes = [
            {
                "name" : "light",
                "cfg": {"bg" : "gray90", "fg" : "black", "font":(font, fsize), "bd":0},
                "properties": {"hover":{"bg" : "gray75", "fg" : "green"}}
            },
            {
                "name" : "dark",
                "cfg": {"bg" : "gray10", "fg" : "white", "font":(font, fsize), "bd":0},
                "properties": {"hover":{"bg" : "gray25", "fg" : "yellow"}}
            }
        ]
        super().__init__(master,text=text,relief="flat")
        Button.objlst.append(self)
        self.modes[Button.current_mode_index]["cfg"].update(cfg)
        self.update_cfg()
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.update_cfg)

        Button.maxlen = len(self.modes)
        Button.current_mode= self.modes[Button.current_mode_index]["name"]

    def _change_mode():
        if Button.current_mode_index >= Button.maxlen -1:
            Button.current_mode_index = 0
        else:
            Button.current_mode_index += 1
        for i in Button.objlst:
            i.config(**i.modes[Button.current_mode_index]["cfg"])
            Button.current_mode = i.modes[Button.current_mode_index]["name"]

    def update_cfg(self,event = None):
        self.config(**self.modes[Button.current_mode_index]["cfg"])

    def on_hover(self, event):
        self.config(**self.modes[Button.current_mode_index]["properties"]["hover"])

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.button_frame=tk.Frame(self,bg="gray80")

        self.buttons=[
            ["C",   "del",  "%",    "^"],
            ["(",   ")",    sympi,  "/"],
            ["7",   "8",    "9",    "*"],
            ["4",   "5",    "6",    "-"],
            ["1",   "2",    "3",    "+"],
            ["Mode","0",    ".",    "="],
        ]

        self.exp = ""
        self.display_var=tk.StringVar()
        self.screen = tk.Entry(self, textvariable=self.display_var, bd = 0, font=(font,fsize),
                               justify="right")

        self.screen.pack(fill="both",expand=1)
        self.button_frame.pack(fill="both",expand=1)
        self.setup_buttons()
        
        self.screen.config(**modes_screen_cfg[Button.current_mode]["cfg"])
        self.button_frame.config(**modes_btnframe_cfg[Button.current_mode]["cfg"])

    def setup_buttons(self):
        frame=self.button_frame
        for r, row in enumerate(self.buttons):
            for c, val in enumerate(row):
                if val in ['', ' ']: continue

                btn = Button(frame, text = val, command = lambda v=val:self.on_btnclick(v))
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2, columnspan=1)
                frame.columnconfigure(c, weight=1)
            frame.rowconfigure(r,weight=1)

    def changetheme(self):
        Button._change_mode()
        self.button_frame.config(**modes_btnframe_cfg[Button.current_mode]["cfg"])
        self.screen.config(**modes_screen_cfg[Button.current_mode]["cfg"])

    def on_btnclick(self, string : str):
        if string=="C":
            self.exp = ""
        elif string == "del":
            self.exp = self.exp[0:-1]
        elif string == "Mode":
            self.changetheme()
        elif string == "=":
            print(string)
            self.exp = self.display_var.get()
            temp_str = self.exp
            temp_str = temp_str.replace("%","*0.01")
            temp_str = temp_str.replace("^","**")
            temp_str = temp_str.replace(sympi, str(pi))

            try:
                self.exp = str(eval(temp_str))
            except:
                self.exp = "ERROR!"
        else:
            if self.exp == "ERROR!":
                self.exp=""
            self.exp += string
        self.display_var.set(self.exp)

if __name__=="__main__":
    app=Calculator()
    app.mainloop()

