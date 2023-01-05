from forroot import *
from screen import *

b = True;

def mf(event):
	global b;
	button = event.widget;
	if b:
		button['text'] = 'X';
	else:
		button['text'] = 'O';

	b = not b;

for c in range(3): frame.columnconfigure(index = c, weight = 1);
for r in range(3): frame.rowconfigure(index = r, weight = 1)
for r in range(3):
    for c in range(3):
        btn = Button(frame, text = ' ', width = 16, height = 8, font = ("Arial", 30))
        btn.grid(row=r, column=c)
        btn.bind("<Button-1>", mf)





