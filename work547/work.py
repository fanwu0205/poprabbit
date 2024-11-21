import tkinter as tk
from PIL import Image, ImageTk

def update_count():
    global click_count
    click_count += 1
    count_label.config(text=f"吃小蛋糕次數: {click_count}")

def on_click(event):
    rabt_la.config(image=open_mouth_image)
    window.after(200, lambda: rabt_la.config(image=closed_mouth_image))
    update_count()

def reset_count():
    global click_count
    click_count = 0
    count_label.config(text=f"吃小蛋糕次數: {click_count}")

# 建立主視窗
window = tk.Tk()
window.title("Pop537 一呀蛤~")
window.geometry("400x500")
click_count = 0

# 加載圖片
closed_mouth_image = ImageTk.PhotoImage(Image.open("v2close.jpg").resize((300, 300)))
open_mouth_image = ImageTk.PhotoImage(Image.open("v2open.jpg").resize((300, 300)))

# 建立圖片 Label
rabt_la = tk.Label(window, image=closed_mouth_image)
rabt_la.pack(pady=20)
rabt_la.bind("<Button-1>", on_click)

# 建立次數顯示 Label
count_label = tk.Label(window, text="吃小蛋糕次數: 0", font=("Arial", 18))
count_label.pack(pady=10)

# 建立重置按鈕
reset_button = tk.Button(window, text="重置", command=reset_count, font=("Arial", 14), bg="lightblue")
reset_button.pack(pady=10)

# 運行主循環
window.mainloop()
