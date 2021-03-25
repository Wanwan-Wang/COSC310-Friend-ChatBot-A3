from tkinter import *
import socket
import sys
BG_COLOR = "#FFFFFF"
BG_COLOR2 = "#2acaea"
TEXT_COLOR = "#000000"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

soc=socket.socket()
soc.connect(("127.0.0.1",8888))

class ChatBox:
    def __init__(self):
        self.window=Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat Box")
        self.window.resizable(width = False, height = False)
        self.window.configure(width = 500, height = 750, bg = BG_COLOR)
        
        head_label = Label(self.window, bg = BG_COLOR2, fg = TEXT_COLOR, text = "This is a chatbot!!", font = FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        line = Label(self.window, width = 500, bg = BG_COLOR)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        #text
        self.text_widget = Text(self.window, width = 20, height = 2, bg = BG_COLOR, fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow" , state = DISABLED)

        scrollbar = Scrollbar(self.text_widget) 
        scrollbar.place(relheight = 1, relx = 0.974)
        scrollbar.configure(command = self.text_widget.yview)

        bottomLabel = Label(self.window, bg = BG_COLOR2, height = 80)
        bottomLabel.place(relwidth = 1, rely = 0.825)

        #ENTER TEXT
        self.msgEntry = Entry(bottomLabel, bg = BG_COLOR , fg = TEXT_COLOR, font = FONT)
        self.msgEntry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msgEntry.focus()
        self.msgEntry.bind("<Return>", self.enter)

        #botton
        sendButton = Button(bottomLabel, text = "Send", font = FONT_BOLD, width = 20, bg = BG_COLOR, command = lambda: self.enter(None))
        sendButton.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)
    def enter(self, event):
        msg = self.msgEntry.get()
        self.insertMassage(msg, "You")

    def insertMassage(self, msg, sender):
        if not msg:
            return
        
        self.msgEntry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state = DISABLED)
        #response
        soc.sendall(msg.encode("utf-8"))
        rep=soc.recv(2048).decode("utf-8")
        if msg=="bye":
            soc.close()
            sys.exit()
        msg2 = f"Chatbot: {rep}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state = DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatBox()
    app.run()

