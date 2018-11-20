"""
    Create a CRUD application with a GUI interface
"""

import pickle
import tkinter
import tkinter.messagebox


class CrudGUI:
    def __init__(self, master, input):
        self.master = master
        self.master.title('Welcome Menu')
        self.input = input

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radio buttons

        self.look = tkinter.Radiobutton(self.top_frame, text="Look up customer", variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text="Add a customer", variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text="Change customer information", variable=self.radio_var,
                                          value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text="Delete a customer", variable=self.radio_var, value=4)

        # pack radio buttons

        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons

        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.master.destroy)

        # pack buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            look_up = LookGUI(self.master, self.input)
        else:

            tkinter.messagebox.showinfo("Hey Listen", "You have selected something not yet implemented!")


class LookGUI:
    def __init__(self, master, input):
        self.master = master
        self.input = input
        self.look = tkinter.Toplevel(master)
        self.look.title("Search for customer")
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # widget for middle frame
        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.middle_frame, text = 'Results: ')
        self.results = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.results_label.pack(side='left')
        self.results.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.look.destroy)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        try:
            input_file = open(self.input, 'rb')
            customers = pickle.load(input_file)
        except(FileNotFoundError, IOError):
            customers = {}

        self.customers = customers
        name = self.search_entry.get()
        result = self.customers.get(name, 'That name was not found')
        self.value.set(result)



def main():
    input_file = "customer_file.dat"
    root = tkinter.Tk()
    menu_gui = CrudGUI(root, input_file)
    root.mainloop()


main()
