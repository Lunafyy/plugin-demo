import os

for file in [f for f in os.listdir("./plugins")]:
    if file[-3:] == ".py" and file != "plugin.py":
        file = file.rstrip(".py")
        exec(f"from plugins import {file}")

txt = text.Text()

txt.display("Hi")