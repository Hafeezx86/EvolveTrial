class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        self.tasks[index].complete()


def display_welcome():
    print("Student Task Tracker")