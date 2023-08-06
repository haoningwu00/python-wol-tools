import tkinter


class TkApp(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(TkApp, self).__init__(*args, **kwargs)
        self.status_text_var = tkinter.StringVar()

        self.__init_ui()

    def __init_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry('300x400')


if __name__ == '__main__':
    app = TkApp()
    app.title('WOL-APP BY Haoning')

    app.mainloop()
