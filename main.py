from tkinter import *
from home import Home
from booking import Booking
from reservations import Reservation
from edit_reservation import EditReservation


root =Tk()
root.minsize(800,600)
root.title('FlySky')
########################
#body Frame Init
body = Frame(root)
home_page = Home(body)
Booking_page=Booking(body)
EditReservation_page=EditReservation(body)
Reservation_page=Reservation(body,EditReservation_page)
Reservation_page.set_book_new_flight(Booking_page)
EditReservation_page.set_reservation_page(Reservation_page)
home_page.set_book_flight_page(Booking_page)
home_page.set_reservation_page(Reservation_page)
Booking_page.set_home_page(home_page)

def show_frame(page):
    home_page.hide()
    Reservation_page.hide()
    Booking_page.hide()
    EditReservation_page.hide()
    page.show()

####################

#Header Frame Init
header=Frame(height="70",bg='#0284C7')
header.pack(fill=X)
#left header components
plane_img=PhotoImage(file=r"D:\\U\\python\\Project\\assets\\plane.png")
resize_palne=plane_img.subsample(5,5)
flysky_button=Button(header,text="FlySky Reservations",padx=10,image=resize_palne,activebackground='#A8C7DA',compound=LEFT,bg='#0284C7',font=("arial",10,"bold"),command=lambda:show_frame(home_page))
flysky_button.place(x=30,y=10)
#right header components
home_button=Button(header,text='Home',activebackground='#A8C7DA',bg='#0284C7',font=("arial",10,"bold underline"),command=lambda:show_frame(home_page))
home_button.place(x=500,y=20)

book_flight_button=Button(header,text='Book Flight',activebackground='#A8C7DA',bg='#0284C7',font=("arial",10,'bold'),command=lambda:show_frame(Booking_page))
book_flight_button.place(x=555,y=20)

view_resrevation_button=Button(header,text='View Reservation',activebackground='#A8C7DA',bg='#0284C7',font=("arial",10,'bold'),command=lambda:show_frame(Reservation_page))
view_resrevation_button.place(x=650,y=20)


body.pack(fill=BOTH, expand=True)

home_page.show()

root.mainloop()