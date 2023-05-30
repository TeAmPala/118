import tkinter
from tkinter import ttk


#работа с файлами
comp2 = []
sotr2 = []
z = []
q = []
sotr1 = open("sotr.txt", "r", encoding="utf-8")
comp1 = open("comp.txt", "r", encoding="utf-8")
# приведение к нормальным спискам
def qq():
    companies = q
def zz():
    sotr = z


def comps():
    for i in comp1:
        c = ""
        a = 0
        for o in i:
            a += 1
        a -= 1
        for g in i:
            if a != 0:
                c += g
                a -= 1
        comp2.append(c)
    w = 0
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    for i in range(len(comp2)):
        if w == 0:
            a = comp2[i]
            w += 1
        elif w == 1:
            b = comp2[i]
            w += 1
        elif w == 2:
            c = comp2[i]
            w += 1
            q.append((int(a), b, int(c)))
            w = 0


def sotrs():
    for i in sotr1:
        c = ""
        a = 0
        for o in i:
            a += 1
        a -= 1
        for g in i:
            if a != 0:
                c += g
                a -= 1
        sotr2.append(c)
    w = 0
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    for i in range(len(sotr2)):
        if w == 0:
            a = sotr2[i]
            w += 1
        elif w == 1:
            b = sotr2[i]
            w += 1
        elif w == 2:
            c = sotr2[i]
            w += 1
        elif w == 3:
            d = sotr2[i]
            w += 1
        elif w == 4:
            e = sotr2[i]
            w = 0
            z.append((int(a), b, int(c), int(d), e))

sotr = z
companies = q
comps()
sotrs()
#win1
window = tkinter.Tk()
window.title("Контрагенты и сотрудники")
window.geometry('1800x1200')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Сотрудники')
tab_control.pack(expand=1, fill='both')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Контрагенты')


#1 поиск сотрудников
def serch1():
    table1.delete(*table1.get_children())
    for serch in sotr:
        if fio_entry1.get() == serch[1] or int(inn_entry1.get()) == serch[3]:
            table1.insert('', tkinter.END, values=serch)
        elif fio_entry1.get() == "" and inn_entry1.get() == "":
            table1.delete(*table1.get_children())
            for clear in sotr:
                table1.insert('', tkinter.END, values=clear)
def clear1():
    table1.delete(*table1.get_children())
    for clear in sotr:
        table1.insert('', tkinter.END, values=clear)

#2 поиск контрагентов
def serch2():
    table2.delete(*table2.get_children())
    for serch in companies:
        if cont_entry2.get() == "" and int(inn_entry2.get()) == "":
            for row3 in companies:
                table2.insert('', tkinter.END, values=row3)


        elif fio_entry1.get() == serch[1] or int(inn_entry2.get()) == serch[2]:
            table2.insert('', tkinter.END, values=serch)


def clear2():
    table2.delete(*table2.get_children())
    for clear in companies:
        table2.insert('', tkinter.END, values=clear)


#Добавление 1
def add11():
    def add12():
        sotr1 = open("sotr.txt", "a", encoding="utf-8")
        sotr1.write(str(len(sotr) + 1)+"\n")
        sotr1.write(f_entry3.get() + " " + i_entry3.get() + " " + o_entry3.get() + "\n")
        sotr1.write(cn_entry3.get() + "\n")
        sotr1.write(inn_entry3.get() + "\n")
        sotr1.write(con_entry3.get() + "\n")
        sotr1 = open("sotr.txt", "r", encoding="utf-8")
        sotr.clear()
        z.clear()
        sotr2.clear()
        for i in sotr1:
            c = ""
            a = 0
            for o in i:
                a += 1
            a -= 1
            for g in i:
                if a != 0:
                    c += g
                    a -= 1
            sotr2.append(c)
        w = 0
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        for i in range(len(sotr2)):
            if w == 0:
                a = sotr2[i]
                w += 1
            elif w == 1:
                b = sotr2[i]
                w += 1
            elif w == 2:
                c = sotr2[i]
                w += 1
            elif w == 3:
                d = sotr2[i]
                w += 1
            elif w == 4:
                e = sotr2[i]
                w = 0
                z.append((int(a), b, int(c), int(d), e))


        table1.delete(*table1.get_children())
        for clear in sotr:
            table1.insert('', tkinter.END, values=clear)
    window2 = tkinter.Tk()
    window2.title("Добавление сотрудников")
    window2.geometry('1200x200')
    frame = tkinter.Frame(window2)
    frame.pack()

    # добавление контрагентов
    f_label3 = tkinter.Label(frame, text="Фамилия")
    f_label3.grid(row=0, column=0)
    f_entry3 = tkinter.Entry(frame)
    f_entry3.grid(row=1, column=0)

    i_label3 = tkinter.Label(frame, text="Имя")
    i_label3.grid(row=0, column=1)
    i_entry3 = tkinter.Entry(frame)
    i_entry3.grid(row=1, column=1)

    o_label3 = tkinter.Label(frame, text="Отчество")
    o_label3.grid(row=0, column=2)
    o_entry3 = tkinter.Entry(frame)
    o_entry3.grid(row=1, column=2)

    cn_label3 = tkinter.Label(frame, text="Снилс Сотрудника")
    cn_label3.grid(row=0, column=3)
    cn_entry3 = tkinter.Entry(frame)
    cn_entry3.grid(row=1, column=3)

    inn_label3 = tkinter.Label(frame, text="ИНН Сотрудника")
    inn_label3.grid(row=0, column=4)
    inn_entry3 = tkinter.Entry(frame)
    inn_entry3.grid(row=1, column=4)

    con_label3 = tkinter.Label(frame, text="Контрагент")
    con_label3.grid(row=0, column=5)
    con_entry3 = tkinter.Entry(frame)
    con_entry3.grid(row=1, column=5)

    add_button3 = tkinter.Button(frame, text="Добавить", command=add12)
    add_button3.grid(row=1, column=6, sticky="news", padx=0)

#Добавление 2
def add21():
    def add22():
        comp1 = open("comp.txt", "a", encoding="utf-8")
        comp1.write((str(len(companies) + 1) + "\n"))
        comp1.write((ip_entry4.get()) + "\n")
        comp1.write((inn_entry4.get()) + "\n")
        comp1 = open("comp.txt", "r", encoding="utf-8")
        companies.clear()
        q.clear()
        comp2.clear()
        for i in comp1:
            c = ""
            a = 0
            for o in i:
                a += 1
            a -= 1
            for g in i:
                if a != 0:
                    c += g
                    a -= 1
            comp2.append(c)
        w = 0
        a = ""
        b = ""
        c = ""
        for i in range(len(comp2)):
            if w == 0:
                a = comp2[i]
                w += 1
            elif w == 1:
                b = comp2[i]
                w += 1
            elif w == 2:
                c = comp2[i]
                w = 0
                q.append((int(a), b, int(c)))
        table2.delete(*table2.get_children())
        for add in companies:
            table2.insert('', tkinter.END, values=add)

    window3 = tkinter.Tk()
    window3.title("Добавление контрагентов")
    window3.geometry('400x100')
    frame2 = tkinter.Frame(window3)
    frame2.pack()

    # добавление контрагентов
    ip_label4 = tkinter.Label(frame2, text="ИП контрагента")
    ip_label4.grid(row=0, column=0)
    ip_entry4 = tkinter.Entry(frame2)
    ip_entry4.grid(row=1, column=0)

    inn_label4 = tkinter.Label(frame2, text="ИНН контрагента")
    inn_label4.grid(row=0, column=4)
    inn_entry4 = tkinter.Entry(frame2)
    inn_entry4.grid(row=1, column=4)

    add_button4 = tkinter.Button(frame2, text="Добавить", command=add22)
    add_button4.grid(row=1, column=6, sticky="news", padx=0)

# таблица
heads1 = ["№", "ФИО сотрудника", "Снилс сотрудника", "ИНН сотрудника", "Контрагент"]
table1 = ttk.Treeview(tab1, show='headings')
scr_p1 = ttk.Scrollbar(tab1, command=table1.yview)
table1 = ttk.Treeview(tab1, show='headings', yscrollcommand=scr_p1.set)
table1.configure(yscrollcommand=scr_p1.set)
scr_p1.grid(row=2, column=3, sticky='ns')
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

sot_label1 = tkinter.Label(tab1, text="ФИО сотрудника")
sot_label1.grid(row=0, column=1)

inn_label1 = tkinter.Label(tab1, text="ИНН сотрудника")
inn_label1.grid(row=0, column=0)

fio_entry1 = tkinter.Entry(tab1)
fio_entry1.grid(row=1, column=1)

inn_entry1 = tkinter.Entry(tab1)
inn_entry1.grid(row=1, column=0)

confirm_button1 = tkinter.Button(tab1, text="Применить", command=serch1)
confirm_button1.grid(row=0, column=2, sticky="news", padx=30)

reset_button1 = tkinter.Button(tab1, text="Сбросить", command=clear1)
reset_button1.grid(row=1, column=2, sticky="news", padx=30)

add_button1 = tkinter.Button(tab1, text="Добавить", command=add11)
add_button1.grid(row=1, column=4, sticky="news", padx=0)

heads2 = ['№', 'Наименование контрагента', 'ИНН контрагента']
table2 = ttk.Treeview(tab2, show='headings')
scr_p2 = ttk.Scrollbar(tab2, command=table2.yview)
table2 = ttk.Treeview(tab2, show='headings', yscrollcommand=scr_p2.set)
table2.configure(yscrollcommand=scr_p2.set)
scr_p2.grid(row=2, column=4, sticky="ns")
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

company_label2 = tkinter.Label(tab2, text="Наименование контрагента")
company_label2.grid(row=0, column=0)

inn_label2 = tkinter.Label(tab2, text="ИНН контрагента")
inn_label2.grid(row=0, column=1)

cont_entry2 = tkinter.Entry(tab2)
cont_entry2.grid(row=1, column=0)

inn_entry2 = tkinter.Entry(tab2)
inn_entry2.grid(row=1, column=1)

confirm_button2 = tkinter.Button(tab2, text="Применить", command=serch2)
confirm_button2.grid(row=0, column=2, sticky="news", padx=0)

reset_button2 = tkinter.Button(tab2, text="Сбросить", command=clear2)
reset_button2.grid(row=1, column=2, sticky="news", padx=0)

add_button2 = tkinter.Button(tab2, text="Добавить", command=add21)
add_button2.grid(row=1, column=6, sticky="news", padx=0)

table1['columns'] = heads1
table2['columns'] = heads2

for header1 in heads1:
    table1.heading(header1, text=header1, anchor="center")
    table1.column(header1, anchor="center")

for row1 in sotr:
    table1.insert('', tkinter.END, values=row1)

for header2 in heads2:
    table2.heading(header2, text=header2, anchor="center")
    table2.column(header2, anchor="center")

for row2 in companies:
    table2.insert('', tkinter.END, values=row2)

table1.grid(row=2, column=0, columnspan=3)
table2.grid(row=2, column=0, columnspan=3)

window.mainloop()
