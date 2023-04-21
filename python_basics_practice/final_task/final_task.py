from tkinter import Radiobutton
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("localhost", "root", "9111617923", "lease_agreements")

def view():
    cursor = connection.cursor()

    if selected.get() == 0:
        cursor.execute(
            "SELECT objects.TerritoryID, object_type.Name, objects.ObjectNumber, objects.Area, lessees.Name, "
            "lease_agreements.Number, lease_agreements.Date, lease_agreements.StartOfRentPayment, "
            "lease_agreements.Expiration, agreement_value.AgreementID "
            "FROM agreement_value, objects,object_type, lessees, lease_agreements "
            "WHERE (agreement_value.ObjectID=objects.ObjectID "
            "AND agreement_value.AgreementID =lease_agreements.AgreementID "
            "AND lessees.LesseeID = lease_agreements.LesseeID AND objects.TypeID=object_type.TypeID)")
    elif selected.get() == 1:
        cursor.execute(
            "SELECT objects.TerritoryID, object_type.Name, objects.ObjectNumber, objects.Area, lessees.Name, "
            "lease_agreements.Number, lease_agreements.Date, lease_agreements.StartOfRentPayment, "
            "lease_agreements.Expiration, agreement_value.AgreementID "
            "FROM agreement_value, objects,object_type, lessees, lease_agreements "
            "WHERE (agreement_value.ObjectID=objects.ObjectID "
            "AND agreement_value.AgreementID =lease_agreements.AgreementID "
            "AND lessees.LesseeID = lease_agreements.LesseeID AND objects.TypeID=object_type.TypeID "
            "AND objects.TerritoryID = 1)")
    elif selected.get() == 2:
        cursor.execute(
            "SELECT objects.TerritoryID, object_type.Name, objects.ObjectNumber, objects.Area, lessees.Name, "
            "lease_agreements.Number, lease_agreements.Date, lease_agreements.StartOfRentPayment, "
            "lease_agreements.Expiration, agreement_value.AgreementID FROM agreement_value, "
            "objects,object_type, lessees, lease_agreements "
            "WHERE (agreement_value.ObjectID=objects.ObjectID "
            "AND agreement_value.AgreementID =lease_agreements.AgreementID "
            "AND lessees.LesseeID = lease_agreements.LesseeID AND objects.TypeID=object_type.TypeID "
            "AND objects.TerritoryID = 2)")
    elif selected.get() == 3:
        cursor.execute(
            "SELECT objects.TerritoryID, object_type.Name, objects.ObjectNumber, objects.Area, lessees.Name, "
            "lease_agreements.Number, lease_agreements.Date, lease_agreements.StartOfRentPayment, "
            "lease_agreements.Expiration, agreement_value.AgreementID "
            "FROM agreement_value, objects,object_type, lessees, lease_agreements "
            "WHERE (agreement_value.ObjectID=objects.ObjectID "
            "AND agreement_value.AgreementID =lease_agreements.AgreementID "
            "AND lessees.LesseeID = lease_agreements.LesseeID AND objects.TypeID=object_type.TypeID "
            "AND objects.TerritoryID = 3)")
    elif selected.get() == 4:
        cursor.execute(
            "SELECT objects.TerritoryID, object_type.Name, objects.ObjectNumber, objects.Area, lessees.Name, "
            "lease_agreements.Number, lease_agreements.Date, lease_agreements.StartOfRentPayment, "
            "lease_agreements.Expiration, agreement_value.AgreementID "
            "FROM agreement_value, objects,object_type, lessees, lease_agreements "
            "WHERE (agreement_value.ObjectID=objects.ObjectID "
            "AND agreement_value.AgreementID =lease_agreements.AgreementID "
            "AND lessees.LesseeID = lease_agreements.LesseeID AND objects.TypeID=object_type.TypeID "
            "AND objects.TerritoryID = 4)")

    lst = cursor.fetchall()
    for data in lst:
        tree.insert("", END, values = data)
    cursor.close()

# главное окно

window = Tk()
window.title("Арендаторы ГК \"Новая Лахта\" ")
window.geometry('1000x450')

main_frame = Frame(window)
main_frame.pack()

left_frame = Frame(main_frame)
left_frame.pack(side=LEFT)

right_frame = Frame(main_frame)
right_frame.pack(side=RIGHT)


# left_frame: выбор базы

label1 = Label(left_frame, text="Выберите базу:")
label1.grid(row=0, column=0)

selected = IntVar()
selected.set(0)
rad1 = Radiobutton(left_frame, text='Все базы', value=0, variable=selected)
rad1.grid(column=0, row=1)
rad2 = Radiobutton(left_frame, text='1 база', value=1, variable=selected)
rad2.grid(column=0, row=2)
rad3 = Radiobutton(left_frame, text='2 база', value=2, variable=selected)
rad3.grid(column=0, row=3)
rad4 = Radiobutton(left_frame, text='3 база', value=3, variable=selected)
rad4.grid(column=0, row=4)
rad5 = Radiobutton(left_frame, text='4 база', value=4, variable=selected)
rad5.grid(column=0, row=5)


# right_frame: окно, в котором отображается запрошенная информация

def sort(col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    l.sort(reverse=reverse)
    for index, (_, k) in enumerate(l):
        tree.move(k, "", index)
    tree.heading(col, command=lambda: sort(col, not reverse))

columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
tree = ttk.Treeview(right_frame, columns=columns, show='headings')
tree.grid(column=0, row=0)
tree.heading("1", text = "База", command=lambda: sort(0, False))
tree.heading("2", text = "Вид объекта")
tree.heading("3", text = "Jбъект")
tree.heading("4", text = "Площадь")
tree.heading("5", text = "Арендатор")
tree.heading("6", text = "Номер договора")
tree.heading("7", text = "Дата договора")
tree.heading("8", text = "Начало аренды")
tree.heading("9", text = "Окончание аренды")
tree.heading("10", text = "ID")
tree.column("1", anchor=CENTER, width=40)
tree.column("2", anchor=CENTER, width=80)
tree.column("3", anchor=CENTER, width=70)
tree.column("4", anchor=CENTER, width=70)
tree.column("5", anchor=CENTER, width=130)
tree.column("6", anchor=CENTER, width=100)
tree.column("7", anchor=CENTER, width=100)
tree.column("8", anchor=CENTER, width=100)
tree.column("9", anchor=CENTER, width=100)
tree.column("10", anchor=CENTER, width=20)

scrollbar = ttk.Scrollbar(right_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')


btn_show = Button(left_frame, text="Показать", command = view())
btn_show.grid(column=0, row=5)


window.mainloop()
