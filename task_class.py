class Task:
    def __init__(self, owner, importance, task_name):
        self.owner = owner
        self.importance = importance
        self.task_name = task_name

    def edit_task_name(self, task_name):
        self.task_name = task_name


task1 = Task("joe", 4, "hello")

task2 = Task("fluffy", 10, "")

task2.edit_task_name()