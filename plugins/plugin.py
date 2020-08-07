class Plugin(object):
    def __init__(self, name, author, description):
        self.name = name
        self.author = author
        self.description = description

    @property
    def _name(self):
        return self.name
    @property
    def _author(self):
        return self.author
    @property
    def _description(self):
        return self.description
