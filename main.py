import Tkinter
import tkMessageBox

window = Tkinter.Tk()

def buttonCallBack():
    tkMessageBox.showinfo("Ultimate Bravery: Hybrid Pentatration", "Item set created!")

createItemSetButton = Tkinter.Button(window, text = "Ultimate Bravery Me!", command = buttonCallBack)

createItemSetButton.pack()
window.mainloop()
