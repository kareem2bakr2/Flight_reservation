from tkinter import *
from tkinter import ttk

class Home:
    def __init__(self,master):
        self.frame = Frame(master)  
        self.bodyFrame()
    def bodyFrame(self):
        self.headbody()
        self.footbody()
    def headbody(self):
        welcome_msg=Label(self.frame,text='Welcome to FlySky Reservations',pady=15,font=('arial',20,'bold'),fg='#075985')
        welcome_msg.pack()
        descripe_msg=Label(self.frame,text='Book your flights and manage your reservations with our simple and intuitive system.',pady=5,font=('arial',13,'bold'))
        descripe_msg.pack()
    def footbody(self):
        self.plane_img=PhotoImage(file=r"D:\\U\\python\\Project\\assets\\plane.png")
        self.resize_palne=self.plane_img.subsample(5,5)
        self.history_img=PhotoImage(file=r"D:\\U\\python\\Project\\assets\\history.png")
        self.resize_history=self.history_img.subsample(5,5)
        container_frame=Frame(self.frame)
        container_frame.pack()
        book_flight_frame=Frame(container_frame,bg='#e2e6ea',height=300,width=300,pady=20,bd=3,relief='solid')
        book_flight_frame.pack(side=RIGHT,padx=10)
        history_frame=Frame(container_frame,bg='#e2e6ea',height=300,width=300,pady=20,bd=3,relief='solid')
        history_frame.pack(side=LEFT,padx=10)
        plane_img_View=Label(book_flight_frame,image=self.resize_palne,bg='#E0F2FE',pady=5)
        plane_img_View.pack()
        Book_a_Flight_head=Label(book_flight_frame,text='Book a Flight',bg='#e2e6ea',pady=5,font=('arial',15,'bold'),fg='#0369A1')
        Book_a_Flight_head.pack()
        Book_a_Flight_msg=Label(book_flight_frame,bg='#e2e6ea',text='Reserve your next flight by providing your details and flight information.',wraplength=300,pady=5,font=('arial',10,'bold'))
        Book_a_Flight_msg.pack()
        Book_A_flight_btn=Button(book_flight_frame,text='BOOK A FLIGHT',bg='#0284C7',fg='white',command=self.book_flight_btn)
        Book_A_flight_btn.pack(fill=X)
        history_img_View=Label(history_frame,image=self.resize_history,bg='#E0F2FE',pady=5)
        history_img_View.pack()
        history_head=Label(history_frame,text='View Reservations',bg='#e2e6ea',pady=5,font=('arial',15,'bold'),fg='#0369A1')
        history_head.pack()
        history_msg=Label(history_frame,text='Manage your existing reservations, view details, edit or cancel if needed.',bg='#e2e6ea',wraplength=300,pady=5,font=('arial',10,'bold'))
        history_msg.pack()
        history_btn=Button(history_frame,text='View Reservations',bg='#0284C7',fg='white',command=self.view_reservation_btn)
        history_btn.pack(fill=X)
    def set_reservation_page(self,page):
        self.view_reservation_page=page
    def set_book_flight_page(self,page):
        self.book_flight_page=page
    def view_reservation_btn(self):
        self.hide()
        self.view_reservation_page.show()
    
    def book_flight_btn(self):
        self.hide()
        self.book_flight_page.show()
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)
    def hide(self):
        self.frame.pack_forget()