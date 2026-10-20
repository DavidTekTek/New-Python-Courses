from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


# ---------- PART 1: the main window ----------
window = Tk()
window.title("Letter Writing Application")
window.geometry("600x500")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


# ---------- PART 2: open an existing letter ----------
def open_letter():
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
	if not filepath:
		return

	txt_edit.delete("1.0", END)
	with open(filepath, "r") as input_file:
		txt_edit.insert(END, input_file.read())
	window.title(f"Letter Writing Application - {filepath}")


# ---------- PART 3: save the letter under a new name ----------
def save_letter():
	filepath = asksaveasfilename(defaultextension=".txt")
	if not filepath:
		return

	with open(filepath, "w") as output_file:
		output_file.write(txt_edit.get("1.0", END))
	window.title(f"Letter Writing Application - {filepath}")


# ---------- PART 4: the widgets ----------
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)


# ---------- PART 5: lay it out with grid ----------
btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


# ---------- PART 6: start the program ----------
window.mainloop()
