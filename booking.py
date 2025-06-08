from tkinter import *
from tkcalendar import Calendar
from database import insert_resrervation
class Booking:
    def __init__(self,master):
        self.frame = Frame(master)  
        self.header()
        self.form_fn()
        self.err_label = None 
    def header(self):
        book_flight_head=Label(self.frame,text='Book a Flight',width=50,fg='#075985',font=('arial',15,'bold'))
        book_flight_head.pack()
    def form_fn(self):
        self.form=Frame(self.frame,bg='white',bd=3,height=100,width=200)
        self.form.pack(fill=X)
        self.fullname()
        self.flightnumber()
        self.Departure()
        self.Destination()
        self.date()
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
    def date(self):
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
        Book_btn=Button(self.form,text='Book Flight',bg='#0284C7',command=self.book_btn)
        Book_btn.pack(side=RIGHT,padx=5,pady=3)
        cancel_btn=Button(self.form,text='cancel',command=self.cancel_btn_fb)
        cancel_btn.pack(side=RIGHT,padx=5,pady=3)
    def set_home_page(self,page):
        self.home_page=page
    def set_Reservation_page(self,page):
        self.reservation_page=page
    def book_btn(self):
        if self.err_label is not None:
            self.err_label.destroy()
        name=self.full_name_Entry.get()
        flight_num=self.Flight_Number_Entry.get()
        departure=self.Departure_Entry.get()
        destination=self.Destination_Entry.get()
        date=self.Date_entry.get()
        seat_number=self.Seat_Number_Entry.get()
        return_stat=insert_resrervation(name,flight_num,departure,destination,date,seat_number)
        if return_stat == "Successfully added":
            self.hide()
            self.reservation_page.search_hanndle()
            self.reservation_page.show()
        else:
            self.err_label=Label(self.form,text=f'{return_stat}',fg='red',bg="white",font=('arial',10,'bold'))
            self.err_label.pack(fill=X,pady=3,padx=5)
    def cancel_btn_fb(self):
        self.hide()
        self.home_page.show()
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)
    def hide(self):
        self.frame.pack_forget()

