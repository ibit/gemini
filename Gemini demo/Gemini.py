import tkinter as tk
from tkinter import ttk
import google.generativeai as generativeai
#
def get_entry():
    prompt_text = entry.get()
    response = gemini_pro.generate_content(prompt_text)
    response_text = response.text
    print(response_text)

root = tk.Tk()
root.title('Gemini')
root.geometry('600x400')

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text='送信', command=get_entry)
button.pack()

# APIキー
GOOGLE_API_KEY = "YOUR GEMINIS API KEY"
generativeai.configure(api_key=GOOGLE_API_KEY)

# 初期化
gemini_pro = generativeai.GenerativeModel("gemini-pro")

root.mainloop()
