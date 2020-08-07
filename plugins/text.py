from plugins import plugin

class Text(plugin.Plugin):
    def __init__(self):
        super().__init__("Text", "Lunafy", "Put text on the screen")
    
    def display(self, text: str):
        print(text)
