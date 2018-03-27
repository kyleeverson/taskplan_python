class TaskItem:
    def __init__(self, name, parent, id):
        self.id = id
        self.name = name
        self.parent = parent

    def __str__(self):
        return "TaskItem {}".format(self.name)