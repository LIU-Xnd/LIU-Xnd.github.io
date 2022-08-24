# -*- coding: utf-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("TOC生成器(支持中文)")
window.geometry("800x640")
# Main frame.

hint = tk.Label(window,text="复制到下面:")
hint.pack()
entry = tk.Text(window,height=20,width=100) # It's actually a Text object.
entry.pack()
result_text = tk.Text(window)

def kalculate(TEXT): # to show results.
    result_text.delete('1.0','end') #'row[from 1].col[from 0]'
    result = TEXT
    try:
        result_text.insert('end',result)
    except:
        result_text.insert('end',"Invalid Input!")
    return

def get_titles(TXT): # returns [text1,text2,...]
    lines = list(TXT.split("\n"))
    titles = []
    for line in lines:
        if "#" in line:
            titles.append(line)
    return titles

def start_running():
    txt = entry.get("1.0","end")
    titles = get_titles(txt)
    output = ""
    for line in titles:
        c = line.count("#")
        if c == 1:
            cited = line[2:].replace(" ","-").replace(
                    ",","").replace("，","").replace("/","")
            toc_line = "- [" + line[2:] + "](#" + cited + ")\n"
        elif c ==2:
            cited = line[3:].replace(" ","-").replace(
                    ",","").replace("，","").replace("/","")
            toc_line = "  * [" + line[3:] + "](#" + cited + ")\n"
        else:
            cited = line[4:].replace(" ","-").replace(
                    ",","").replace("，","").replace("/","")
            toc_line = "    + [" + line[4:] + "](#" + cited + ")\n"
        output += toc_line
    kalculate(output)

Kal_button = tk.Button(master=window,text="生成TOC",command=start_running)
Kal_button.pack()
result_text.pack()


window.mainloop()