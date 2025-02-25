try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    print("Error: Tkinter module is not installed. Please install it or use an environment that supports GUI applications.")
    import sys
    sys.exit()

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()
        
        if unit == "Celsius":
            result = f"{temp} C = {celsius_to_fahrenheit(temp):.1f} F, {celsius_to_kelvin(temp):.2f} K"
        elif unit == "Fahrenheit":
            result = f"{temp} F = {fahrenheit_to_celsius(temp):.1f} C, {fahrenheit_to_kelvin(temp):.2f} K"
        elif unit == "Kelvin":
            result = f"{temp} K = {kelvin_to_celsius(temp):.1f} C, {kelvin_to_fahrenheit(temp):.1f} F"
        else:
            result = "กรุณาเลือกหน่วยอุณหภูมิ"
            
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ตัวแปลงอุณหภูมิ")
root.geometry("400x300")
root.configure(bg="lightblue")

# หัวข้อหลัก
title_label = tk.Label(root, text="Temperature 🌡", bg="lightblue", fg="blue", font=("Arial", 16, "bold"))
title_label.pack(pady=5)

# เลือกหน่วยอุณหภูมิ
unit_var = tk.StringVar()
unit_var.set("Celsius")

label2 = tk.Label(root, text="เลือกหน่วยอุณหภูมิ:", bg="lightblue", font=("Arial", 14))
label2.pack(pady=5)

unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12))
unit_menu.pack(pady=5)

# ป้ายข้อความและช่องป้อนค่า
label1 = tk.Label(root, text="ป้อนค่าอุณหภูมิ:", bg="lightblue", font=("Arial", 14))
label1.pack(pady=5)

entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

# ปุ่มแปลงค่า
convert_button = tk.Button(root, text="แปลงค่า", command=convert_temperature, bg="green", fg="white", font=("Arial", 14, "bold"))
convert_button.pack(pady=10)

# แสดงผลลัพธ์
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue")
label_result.pack(pady=10)

# เรียกใช้งานหน้าต่าง
root.mainloop()
