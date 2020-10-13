from tkinter import Tk, RIGHT, LEFT, CENTER, Frame, TOP, Entry, Checkbutton, Button
from tkinter.ttk import Label


class MainWindow(Tk):
    def __init__(self, screen_name=None, baseName=None, className='Tk',
                 useTk=1, sync=0, use=None):
        super().__init__(screenName=None, baseName=None, className='Tk',
                         useTk=1, sync=0, use=None)
        self.geometry("600x250")
        self.initialize_screen()

    def start_pipper(self):
        pass

    def initialize_screen(self):
        frame1 = Frame(self, height="500", width="700", bg="green")
        frame1.pack_propagate(0)
        frame1.pack(pady=50)

        frame2 = Frame(frame1, height="500", width="700", bg="green")
        frame2.pack_propagate(0)
        frame2.grid(row=1)

        func_label = Label(frame2, text="pip Function:", justify=LEFT, background="green")
        func_label.config(font=("Courier", 14))
        func_label.grid(row=1, column=1)
        func_entry = Entry(frame2, justify=LEFT)
        func_entry.grid(row=1, column=2)

        package_label = Label(frame2, text="Package:", justify=LEFT, background="green")
        package_label.config(font=("Courier", 14))
        package_label.grid(row=1, column=3)
        package_entry = Entry(frame2, justify=LEFT)
        package_entry.grid(row=1, column=4)

        http_label = Label(frame2, text="HTTP Proxy:", justify=LEFT, background="green")
        http_label.config(font=("Courier", 14))
        http_label.grid(row=2, column=1)
        http_entry = Entry(frame2, justify=LEFT)
        http_entry.grid(row=2, column=2)

        https_label = Label(frame2, text="HTTPS Proxy:", justify=LEFT, background="green")
        https_label.config(font=("Courier", 14))
        https_label.grid(row=2, column=3)
        https_entry = Entry(frame2, justify=LEFT)
        https_entry.grid(row=2, column=4)

        upgrade_check_box = Checkbutton(frame1, text="In case of 'install', check if you want to upgrade",
                                        background="green")
        upgrade_check_box.grid(row=2)

        install_button = Button(frame1, text="Install", command=self.start_pipper)
        install_button.config(font=("Courier", 18))
        install_button.grid(rowspan=3)


if __name__ == '__main__':
    MainWindow(screen_name="Pip++").mainloop()
