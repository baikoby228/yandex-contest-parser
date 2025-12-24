class Person:
    def __init__(self):
        self.name = ""
        self.tasks_count = 0
        self.points = []
        self.total_points = 0

    def __str__(self):
        return f'{self.name} - {self.points} - {self.total_points}'
