"""
[课程内容]: 实现视频下载小软件

[授课老师]: 青灯教育-自游

[开发环境]:
    Python 3.8
    Pycharm

[模块使用]:
    subprocess
    tkinter
    you-get ---> pip install you-get

cmd pyinstaller -F -w 文件名.py
"""
import tkinter as tk
import subprocess  # 进程


root = tk.Tk()
root.title('视频下载小软件')
root.geometry("350x50+150+150")


def download():
    link = f'you-get -o video {key_word.get()}'
    subprocess.run(link, shell=True)

def clear():
    e.delete(0, 'end')

txt = tk.Label(text='输入下载网址:', font=80)
txt.grid(row=0, column=0)

key_word = tk.StringVar()

e = tk.Entry(root, textvariable=key_word)
e.grid(row=0, column=1)

bt = tk.Button(text='下载', command=download)
bt.grid(row=0, column=2)

bt = tk.Button(text='清空', command=clear)
bt.grid(row=0, column=3)

root.mainloop()

