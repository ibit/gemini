import tkinter as tk
from tkinter import ttk
import google.generativeai as generativeai
from tkinter import messagebox
import requests

def get_entry():
    prompt_text = entry.get()
    if prompt_text.strip():
        display_user_message(prompt_text)
        entry.delete(0, tk.END)
        
        try:
            selected_mode = var.get()
            if selected_mode == "Gemini":
                response_text = generate_ai_response(prompt_text)
                display_ai_message(response_text)
            elif selected_mode == "ChatGPT":
                response_text = generate_ai_response(prompt_text)  # Placeholder, modify as needed
                display_ai_message(response_text)
            elif selected_mode == "Translation":
                translated_text = translate_text(prompt_text)
                display_translation_message(translated_text)
        except Exception as e:
            display_error_message(str(e))
            messagebox.showerror("エラー", "エラーが発生しました。詳細: " + str(e))

def display_user_message(message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {message}\n", "user_message")
    chat_display.config(state=tk.DISABLED)

def generate_ai_response(prompt_text):
    response = gemini_pro.generate_content(prompt_text)
    return response.text

def display_ai_message(message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Gemini: {message}\n\n", "ai_message")
    chat_display.config(state=tk.DISABLED)

def translate_text(prompt_text):
    DEEPL_API_KEY = "YOUR API KEY"
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": prompt_text,
        "target_lang": "EN"
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()["translations"][0]["text"]
    else:
        raise Exception("翻訳に失敗しました")

def display_translation_message(message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Translation: {message}\n\n", "ai_message")
    chat_display.config(state=tk.DISABLED)

def display_error_message(message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"エラー: {message}\n\n", "error_message")
    chat_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title('Gemini')
root.geometry('600x450')

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.pack(fill=tk.BOTH, expand=True)

entry = ttk.Entry(mainframe, width=50)
entry.grid(column=0, row=0, padx=10, pady=10)

button = ttk.Button(mainframe, text='送信', command=get_entry)
button.grid(column=1, row=0, padx=10, pady=10)

chat_display = tk.Text(mainframe, height=15, width=70)
chat_display.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
chat_display.config(state=tk.DISABLED)

style = ttk.Style()
style.configure("user_message", foreground="blue")
style.configure("ai_message", foreground="green")
style.configure("error_message", foreground="red")

var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(root, text="Gemini", variable=var, value="Gemini")
radiobutton2 = ttk.Radiobutton(root, text="Translation", variable=var, value="Translation")

radiobutton1.pack()
radiobutton1.place(x=520, y=120)
radiobutton2.pack()
radiobutton2.place(x=520, y=140)

GOOGLE_API_KEY = "YOUR API KEY"
generativeai.configure(api_key=GOOGLE_API_KEY)

gemini_pro = generativeai.GenerativeModel("gemini-pro")

root.mainloop()
