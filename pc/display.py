import customtkinter
import display_coinbase_tests
import asyncio
import threading

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

label_var = None
root = None
label = None
old_price = 0
new_price = 0
product = "BTC-USD"

def get_current_price():
    global old_price
    global new_price
    global product
    global label

    new_price = display_coinbase_tests.get_price(product)

    if old_price > new_price:
        label_var.set(f"{product}\n{new_price}")
        label.configure(fg_color = "red", text_color = "black")

    if old_price <= new_price:
        label_var.set(f"{product}\n{new_price}")
        label.configure(fg_color = "green", text_color = "black")

    root.title(f"{product} {new_price}")

    old_price = new_price

async def callBase():
    while True:
        get_current_price()
        await asyncio.sleep(1)

def start_async_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(callBase())

async def main ():

    global root, label_var, label, new_price, product
    root = customtkinter.CTk()
    root.attributes("-topmost", not root.attributes("-topmost"))
    
    root.geometry('300x50')

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)

    label_var = customtkinter.StringVar()
    label_var.set("price")

    label = customtkinter.CTkLabel(master=frame, textvariable=label_var,font=("Helvetica", 16, "bold"))
    label.pack(fill="both", expand=True)

    async_thread = threading.Thread(target=start_async_loop, daemon=True)
    async_thread.start()

    root.mainloop()

if __name__ == "__main__":
    old_price = 0
    asyncio.run(main())