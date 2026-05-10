class User:
    def __init__(self, user_id, name, role):
        self.id = user_id
        self.name = name
        self.role = role

    def login(self):
        print(f"👤 {self.name} is now online.")

    def logout(self):
        print(f"👤 {self.name} is offline.")

class Task:
    def __init__(self, task_id, title, status, due_date):
        self.id = task_id
        self.title = title
        self.status = status
        self.due_date = due_date

    def update_status(self, new_status):
        self.status = new_status
        print(f"📝 Task '{self.title}' status updated to: {new_status}")

class Projet:
    def __init__(self, project_id, name, description, created_at):
        self.id = project_id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.members = []
        self.tasks = []
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)
            self.notify(f"Member {user.name} added to {self.name}")

    def add_task(self, task):
        self.tasks.append(task)
        self.notify(f"New task '{task.title}' created in {self.name}")