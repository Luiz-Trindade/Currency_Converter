# Simple Currency Conversor Written In Python!
# Created By: Luiz Gabriel Magalhães Trindade!
# Distributed Under The Unlicense(Public Domain).
# Unlicense: https://unlicense.org/

from customtkinter import *
from forex_python.converter import CurrencyRates as CR

cr = CR()

money = ["USD", "BRL", "EUR", "GBP", "JPY", "CHF", "CAD", "AUD", "NZD", "CNY"]


def Main():
    def Convert_Money():
        amount = float(entry.get())
        money1 = optionmenu1.get()
        money2 = optionmenu2.get()
        result = cr.convert(money1, money2, amount)
        result_label.configure(text=f"Result: {result:.2f}")

    app = CTk()
    app.title("Currency🪙 Conversor🔄")
    app.geometry("500x200")
    set_appearance_mode("dark")
    set_default_color_theme("green")


    entry = CTkEntry(master=app, placeholder_text="Value", justify="center", font=("Arial", 15, "bold"))
    entry.grid(row=0, column=1, pady=10, padx=10)

    optionmenu1 = CTkOptionMenu(master=app, values=money, anchor="center")
    optionmenu1.grid(row=1, column=0, pady=10, padx=10)

    button = CTkButton(master=app, text="Convert!", font=("Arial", 15, "bold"), command=Convert_Money)
    button.grid(row=1, column=1, pady=10, padx=10)

    optionmenu2 = CTkOptionMenu(master=app, values=money, anchor="center")
    optionmenu2.grid(row=1, column=2, pady=10, padx=10)

    result_frame = CTkFrame(master=app)
    result_frame.grid(row=2, column=1, pady=10, padx=10)
    result_label = CTkLabel(master=result_frame, text="Result:", justify="center", font=("Arial", 15, "bold"))
    result_label.grid(row=2, column=1, pady=10, padx=10)

    app.mainloop()

if __name__ == "__main__":
    Main()
