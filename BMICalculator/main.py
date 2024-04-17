import tkinter

window = tkinter.Tk()

window.title("BMI Calculator")

window.config(padx=30, pady=30)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Lütfen kilonuzu veya boynuzu giriniz")
    else:
        try:

            bmi = float(weight) / (float(height)/100) ** 2

            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Lütfen kilonuzun veya boynuzun değerlerini düzgün giriniz")


#ui

weight_input_label = tkinter.Label(text="Lütfen Ağırlık giriniz (kg cinsinden)")

weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Lütfen Boyunuzu  giriniz (cm cinsinden)")

height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Hesapla", command=calculate_bmi)
calculate_button.pack()


result_label = tkinter.Label()

result_label.pack()

def write_result(bmi):
    result_string = f" Sizin BMI değeriniz: {round(bmi, 2)}'dır. Siz "

    if bmi <= 16:
        result_string += "Aşırı Zayıfsınız!!!"
    elif 16 < bmi <= 17:
        result_string += "Oldukça Zayıfsınız"
    elif 17 < bmi <= 18.5:
        result_string += "Hafifsiniz"
    elif 18.5 < bmi <= 25:
        result_string += "Normalsiniz"
    elif 25 < bmi <= 30:
        result_string += "Şişmansınız"
    elif 30 < bmi <= 35:
        result_string += "Obez Sınıf I"
    elif 35 < bmi <= 40:
        result_string += "Obez Sınıf II"
    else:
        result_string += "Obez Sınıf III"

    return  result_string

window.mainloop()