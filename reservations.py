from tkinter import *

class Reservation:
    def __init__(self,master,edit_ref):
        self.frame = Frame(master)  
        self.header()
        self.history_table()
        self.edit_reservation_page=edit_ref
    def edit_reservation_show(self):
        self.hide()
        self.edit_reservation_page.show()
    def history_table(self):
        self.edit_img=PhotoImage(file=r"D:\\U\\python\\Project\\assets\\edit.png")
        self.resized_edit_img=self.edit_img.subsample(10,10)
        self.remove_img=PhotoImage(file=r"D:\\U\\python\\Project\\assets\\remove.png")
        self.resized_remove_img=self.remove_img.subsample(20,20)
        
        table=Frame(self.frame,bg='white')
        table.pack()
        # Headers
        headers = ["Flight Number", "Name", "Departure", "Destination", "Date", "Seat", "Edit","Remove"]
        for col, text in enumerate(headers):
            label = Label(table , text=text, font=('Arial', 10, 'bold'),bg='white' , padx=5, pady=5)
            label.grid(row=0, column=col ,sticky='w')
        # Example data rows
        data_rows = [
            ["22", "md", "gkdkkds", "lon", "2025-06-27", "12", ],
            ["35", "Ali", "Cairo", "Berlin", "2025-07-02", "14A"],
        ]
        for i, row_data in enumerate(data_rows):
            row_index = i + 1 
            for col, value in enumerate(row_data):
                label = Label(table , text=value, font=('Arial', 10),bg='white', padx=5, pady=7)
                label.grid(row=row_index, column=col, sticky="w")
            edit_btn = Button(table , image=self.resized_edit_img, font=('Arial', 10),bg='white', padx=5, pady=7,command=lambda:self.edit_reservation_show())
            edit_btn.grid(row=row_index, column=6, sticky="w")
            remove_btn = Button(table , image=self.resized_remove_img, font=('Arial', 10),bg='white', padx=5, pady=7)
            remove_btn.grid(row=row_index, column=7, sticky="w")

    def header(self):
        header=Frame(self.frame )
        header.pack()
        your_Reservation_label=Label(header,text='Your Reservations',fg='#077298',font=('arial',15,'bold'))
        your_Reservation_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        search_label=Label(header,text='search : ',font=('arial',9,'bold'))
        search_label.grid(row=0, column=6, padx=5, pady=5, sticky='w')

        search_entry=Entry(header)
        search_entry.grid(row=0, column=7, padx=5, pady=5, sticky='w')

        book_flight_btn=Button(header,text='Book New Flight',bg='#077298',fg='white',command=self.book_room)
        book_flight_btn.grid(row=0, column=8, padx=5, pady=5, sticky='w')
    def set_book_new_flight(self,page):
        self.book_new_flight=page
    def book_room(self):
        self.hide()
        self.book_new_flight.show()
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)
    def hide(self):
        self.frame.pack_forget()
