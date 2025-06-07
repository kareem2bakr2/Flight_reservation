from tkinter import *
from tkcalendar import Calendar

class Booking:
    def __init__(self,master):
        self.frame = Frame(master)  
        self.header()
        self.form_fn()
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
        full_name_Entry=Entry(self.form)
        full_name_Entry.pack(fill=X,pady=3,padx=5)
    def flightnumber(self):
        Flight_Number_head=Label(self.form,text='Flight Number :',bg='white',font=('arial',10))
        Flight_Number_head.pack(fill=X,pady=3,padx=5)
        Flight_Number_Entry=Entry(self.form)
        Flight_Number_Entry.pack(fill=X,pady=3,padx=5)
    def Departure(self):
        Departure_head=Label(self.form,text='Departure :',width=10,bg='white',font=('arial',10))
        Departure_head.pack(fill=X,pady=3,padx=5)
        Departure_Entry=Entry(self.form,width=40)
        Departure_Entry.pack(fill=X,pady=3,padx=5)
    def date(self):
        def show_calendar():
            # Create a new Toplevel window for the calendar
            top = Toplevel(self.form)
            top.grab_set()  # Make the calendar modal (optional)
            
            cal = Calendar(top, selectmode='day')
            cal.pack(pady=10)

            def select_date():
                selected_date = cal.get_date()
                Date_entry.delete(0, END)
                Date_entry.insert(0, selected_date)
                top.destroy()  # Close the calendar window

            btn_select = Button(top, text="Select Date", command=select_date)
            btn_select.pack(pady=10)
        date_head=Label(self.form,text='Date :',width=10,bg='white',font=('arial',10))
        date_head.pack(fill=X,pady=3,padx=5)
        Date_entry = Entry(self.form, width=20, font=('Arial', 14))
        Date_entry.pack(anchor=CENTER,pady=3,padx=5)
        btn_show = Button(self.form, text="Show Calendar", command=show_calendar)
        btn_show.pack(pady=3,padx=5)
    def Destination(self):
        Destination_head=Label(self.form,text='Destination :',width=10,bg='white',font=('arial',10))
        Destination_head.pack(fill=X,pady=3,padx=5)
        Destination_Entry=Entry(self.form,width=40)
        Destination_Entry.pack(fill=X,pady=3,padx=5)
    def seatnumber(self):
        Seat_Number_head=Label(self.form,text='Seat Number :',width=10,bg='white',font=('arial',10))
        Seat_Number_head.pack(fill=X,pady=3,padx=5)
        Seat_Number_Entry=Entry(self.form,width=40)
        Seat_Number_Entry.pack(fill=X,pady=3,padx=5)
    def buttons(self):
        Book_btn=Button(self.form,text='Book Flight',bg='#0284C7')
        Book_btn.pack(side=RIGHT,padx=5,pady=3)
        cancel_btn=Button(self.form,text='cancel',command=self.cancel_btn_fb)
        cancel_btn.pack(side=RIGHT,padx=5,pady=3)
    def set_home_page(self,page):
        self.set_home_page=page
    def cancel_btn_fb(self):
        self.hide()
        self.set_home_page.show()
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)
    def hide(self):
        self.frame.pack_forget()

