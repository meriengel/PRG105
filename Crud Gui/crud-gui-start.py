import tkinter
import tkinter.messagebox
import pickle


class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')
        self.radio_var = 0
        
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        
        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)
        
        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)
        
        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)
        
        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
    
    def open_menu(self):
        if self.radio_var.get() == 1:
            search = LookGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class LookGUI:
    def __init__(self, master):
        
        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}
        
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')
        
        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)
        
        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)
        
        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')
        
        # middle frame
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)
        
        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')
        
        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)
        
        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')
        
        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
    
    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)
    
    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
