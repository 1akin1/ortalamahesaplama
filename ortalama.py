from tkinter import *


def calculate_average():
    total_kredi = 0
    toplam_not_kredi = 0

    for i in range(int(num_of_courses_entry.get())):
        not_entry = not_entries[i].get()
        kredi_entry = kredi_entries[i].get()
        if not_entry != "" and kredi_entry != "":
            notu = float(not_entry)
            kredisi = float(kredi_entry)
            toplam_not_kredi += notu * kredisi
            total_kredi += kredisi

    if total_kredi > 0:
        result = toplam_not_kredi / total_kredi
        result_label.config(text=f"Ortalama: {result:.2f}")
    else:
        result_label.config(text="Lütfen not ve kredi değerlerini girin.")


def create_course_fields():
    for widget in fields_frame.winfo_children():
        widget.destroy()

    num_of_courses = int(num_of_courses_entry.get())

    global not_entries, kredi_entries
    not_entries = []
    kredi_entries = []

    for i in range(num_of_courses):
        not_label = Label(fields_frame, text=f"{i+1}. Ders Notu:")
        not_label.grid(row=i, column=0)

        not_entry = Entry(fields_frame)
        not_entry.grid(row=i, column=1)
        not_entries.append(not_entry)

        kredi_label = Label(fields_frame, text=f"{i+1}. Ders Kredisi:")
        kredi_label.grid(row=i, column=2)

        kredi_entry = Entry(fields_frame)
        kredi_entry.grid(row=i, column=3)
        kredi_entries.append(kredi_entry)

    calculate_button.config(state=NORMAL)


window = Tk()
window.title("Ortalama Hesaplama")
window.geometry("400x300")

num_of_courses_label = Label(window, text="Ders Sayısı:")
num_of_courses_label.pack()

num_of_courses_entry = Entry(window)
num_of_courses_entry.pack()

create_fields_button = Button(window, text="Alanlar Oluştur", command=create_course_fields)
create_fields_button.pack()

fields_frame = Frame(window)
fields_frame.pack()

calculate_button = Button(window, text="Ortalama Hesapla", command=calculate_average, state=DISABLED)
calculate_button.pack()

result_label = Label(window, font=('Arial', 20, 'bold'))
result_label.pack()

window.mainloop()
