import tkinter as tk
from tkinter import ttk

class ItemListFrame(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=100, height=100,
                        borderwidth=1, relief=tk.GROOVE)
        
        #ウィジェット配置
        self.place_widget()
        
    def place_widget(self):
        
        #Canvas作成
        canvas = tk.Canvas(master=self, width=300, height=200, bg='white')
        canvas.grid(row=0, column=0)
        
        #スクロールバー
        vbar = ttk.Scrollbar(master=self, orient=tk.VERTICAL) #縦方向
        vbar.grid(row=0, column=1, sticky=tk.NS)
        
        #スクロールバーの制御をCanvasに通知する処理
        vbar.config(command=canvas.yview)
        
        #Canvasの可動域をスクロールバーに通知する処理
        canvas.config(yscrollcommand=vbar.set)
        
        #スクロール可動域
        canvas.config(scrollregion=(0,0, 300, 5000))
        
        #Frameを作成しcanvasに配置
        frame = tk.Frame(master=canvas, bg='white')
        canvas.create_window((0,0), window=frame, anchor=tk.NW, width=canvas.cget('width'))
        
        self.vars = []
        for i in range(50):
            var = tk.BooleanVar()
            self.vars.append(var)
            check_button = tk.Checkbutton(master=frame, text=i, variable=var)
            check_button.grid(row=i, column=0)
            
root = tk.Tk()
frame = ItemListFrame(root)
frame.pack()
root.mainloop()

#出典
#https://ja.stackoverflow.com/questions/89895/tkinter%E3%81%A7%E3%82%B9%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%BCscrollbar%E3%81%AE%E6%9C%89%E5%8A%B9%E7%AF%84%E5%9B%B2%E3%82%92%E5%BA%83%E3%81%92%E3%81%9F%E3%81%84