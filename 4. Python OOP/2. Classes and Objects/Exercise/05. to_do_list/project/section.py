from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = 0
        for tasks in self.tasks.copy():
            if tasks.completed:
                self.tasks.remove(tasks)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        task_list = []
        for tasks in self.tasks:
            task_list.append(f'Name: {tasks.name} - Due Date: {tasks.due_date}\n')
        return f"Section {self.name}:\n{''.join(task_list)}"
