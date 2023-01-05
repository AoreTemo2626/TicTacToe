from screen import *

root.title('Mamka')
root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.resizable(False,False)

message = Label(root, text = 'aboba')
message.pack();

root.mainloop();
