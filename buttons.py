from forroot import *

for c in range(3): root.columnconfigure(index = c, weight = 1);
for r in range(3): root.rowconfigure(index = r, weight = 1);



for r in range(3):
    for c in range(3):
        btn = ttk.Button()
        btn.grid(row=r, column=c)
 
