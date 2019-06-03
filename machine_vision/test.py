import tkinter as tk

main_window = tk.Tk()
main_window.title("mitsushimahikari")
main_window.geometry('800x600')

l = tk.Label(main_window, text='    ',bg='grey')
l.pack()

count = 0


def do_count():
    global count
    l.config(text="do" + str(count))
    count += 1


menubar = tk.Menu(main_window)

file_menu = tk.Menu(menubar, tearoff=0)
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='A', menu=file_menu)
menubar.add_cascade(label='B', menu=edit_menu)

file_menu.add_command(label='a', command=do_count)
file_menu.add_command(label='b', command=do_count)
file_menu.add_command(label='c', command=do_count)
file_menu.add_command(label='Exit', command=main_window.quit)


edit_menu.add_command(label='b', command=do_count)
edit_menu.add_command(label='c', command=do_count)
edit_menu.add_command(label='d', command=do_count)

sub_mune = tk.Menu(file_menu)
file_menu.add_cascade(label='aaa', menu=sub_mune, underline=0)
sub_mune.add_command(label='bbb', command=do_count)

main_window.config(menu=menubar)

main_window.mainloop()
