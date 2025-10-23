

class User:
    all_users = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.all_users.append(self)
    @property
    def projects(self):
        return [project for project in Project.all_projects if self in project.users]
    
    @property
    def tasks(self):
        return [task for task in Task.all_tasks if task.assigned_to == self]

class Project:
    all_projects = []
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.all_projects.append(self)
    @property
    def users(self):
        return [user for user in User.all_users if user in [task.assigned_to for task in Task.all_tasks if task in Task.all_tasks]]

class Task:
    all_tasks = []
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task.all_tasks.append(self)


