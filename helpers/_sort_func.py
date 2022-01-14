from tkinter import Tk


def main():
    tk = Tk()
    lines = tk.clipboard_get().splitlines()
    funcs = []
    for line in lines:
        if line.startswith(' ' * 5):
            funcs[-1] += f'\n{line}'
        else:
            funcs.append(line)
    funcs.sort()
    tk.clipboard_clear()
    tk.clipboard_append('\n'.join(funcs))
    print(tk.clipboard_get())
    tk.after(500, tk.destroy)
    tk.withdraw()
    tk.mainloop()


if __name__ == '__main__':
    main()
