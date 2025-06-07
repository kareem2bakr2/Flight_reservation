from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
from database import EDIT_reservation
class EditReservation:
    def __init__(self,master):
        self.frame = Frame(master)  
        self.name=None
        self.oldflight=None
        self.header()
        self.form_fn()
    def Fill_data(self,data):
        self.data_row=data
        if data!=None:
            self.departure=data[3]
            self.destination=data[4]
            self.date=data[5]
            self.Seatnumber=data[6]
            self.name=data[1]
            self.oldflight=data[2]
            self.full_name_Entry.delete(0,END)
            self.Flight_Number_Entry.delete(0,END)
            self.Departure_Entry.delete(0,END)
            self.Destination_Entry.delete(0,END)
            self.Date_entry.delete(0,END)
            self.Seat_Number_Entry.delete(0,END)
            self.full_name_Entry.insert(0,self.name)
            self.Flight_Number_Entry.insert(0,self.oldflight)
            self.Departure_Entry.insert(0,self.departure)
            self.Destination_Entry.insert(0,self.destination)
            self.Date_entry.insert(0,self.date)
            self.Seat_Number_Entry.insert(0,self.Seatnumber)
    def set_reservation_page(self,page):
        self.reservation_page=page
    def header(self):
        Edit_reservation_head=Label(self.frame,text='Edit_reservation',width=50,fg='#075985',font=('arial',15,'bold'))
        Edit_reservation_head.pack()
    def form_fn(self):
        self.form=Frame(self.frame,bg='white',bd=3,height=100,width=200)
        self.form.pack(fill=X)
        self.fullname()
        self.flightnumber()
        self.Departure()
        self.Destination()
        self.date_fn()
        self.seatnumber()
        self.buttons()
    def fullname(self):
        Full_Name_head=Label(self.form,text='Full Name :',width=50,bg='white',font=('arial',10))
        Full_Name_head.pack(fill=X,pady=3,padx=5)
        self.full_name_Entry=Entry(self.form)
        self.full_name_Entry.pack(fill=X,pady=3,padx=5)
    def flightnumber(self):
        Flight_Number_head=Label(self.form,text='Flight Number :',bg='white',font=('arial',10))
        Flight_Number_head.pack(fill=X,pady=3,padx=5)
        self.Flight_Number_Entry=Entry(self.form)
        self.Flight_Number_Entry.pack(fill=X,pady=3,padx=5)
    def Departure(self):
        Departure_head=Label(self.form,text='Departure :',width=10,bg='white',font=('arial',10))
        Departure_head.pack(fill=X,pady=3,padx=5)
        self.Departure_Entry=Entry(self.form,width=40)
        self.Departure_Entry.pack(fill=X,pady=3,padx=5)
    def date_fn(self):
        def show_calendar():
            # Create a new Toplevel window for the calendar
            top = Toplevel(self.form)
            top.grab_set()  # Make the calendar modal (optional)
            
            cal = Calendar(top, selectmode='day')
            cal.pack(pady=10)

            def select_date():
                selected_date = cal.get_date()
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(0, selected_date)
                top.destroy()  # Close the calendar window

            btn_select = Button(top, text="Select Date", command=select_date)
            btn_select.pack(pady=10)
        date_head=Label(self.form,text='Date :',width=10,bg='white',font=('arial',10))
        date_head.pack(fill=X,pady=3,padx=5)
        self.Date_entry = Entry(self.form, width=20, font=('Arial', 14))
        self.Date_entry.pack(anchor=CENTER,pady=3,padx=5)
        btn_show = Button(self.form, text="Show Calendar", command=show_calendar)
        btn_show.pack(pady=3,padx=5)
    def Destination(self):
        Destination_head=Label(self.form,text='Destination :',width=10,bg='white',font=('arial',10))
        Destination_head.pack(fill=X,pady=3,padx=5)
        self.Destination_Entry=Entry(self.form,width=40)
        self.Destination_Entry.pack(fill=X,pady=3,padx=5)
    def seatnumber(self):
        Seat_Number_head=Label(self.form,text='Seat Number :',width=10,bg='white',font=('arial',10))
        Seat_Number_head.pack(fill=X,pady=3,padx=5)
        self.Seat_Number_Entry=Entry(self.form,width=40)
        self.Seat_Number_Entry.pack(fill=X,pady=3,padx=5)
    def buttons(self):
        Update_Reservation_btn=Button(self.form,text='Update Reservation',bg='#0284C7',command=self.update_reservation)
        Update_Reservation_btn.pack(side=RIGHT,padx=5,pady=3)
        cancel_btn=Button(self.form,text='cancel',command=self.cancel_btn_fn)
        cancel_btn.pack(side=RIGHT,padx=5,pady=3)
    def cancel_btn_fn(self):
        self.hide()
        self.reservation_page.show()
    def update_reservation(self):
        departure=self.Departure_Entry.get()
        destination=self.Destination_Entry.get()
        date=self.Date_entry.get()
        Seatnumber=self.Seat_Number_Entry.get()
        name=self.full_name_Entry.get()
        flight_num=self.Flight_Number_Entry.get()
        EDIT_reservation(self.data_row[0],name,flight_num,departure,destination,date,Seatnumber)
        self.hide()
        self.reservation_page.search_hanndle()
        self.reservation_page.show()
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)
    def hide(self):
        self.frame.pack_forget()

