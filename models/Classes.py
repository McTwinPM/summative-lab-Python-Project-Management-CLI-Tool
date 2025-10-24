import json
import uuid
from datetime import datetime

class User:
    all_users = []
    
    def __init__(self, name, email, user_id=None):
        self.id = user_id or str(uuid.uuid4())
        self.name = name
        self.email = email
        User.all_users.append(self)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['email'], data['id'])
    
    @property
    def projects(self):
        return [project for project in Project.all_projects if self.id in project.user_ids]
    
    @property
    def tasks(self):
        return [task for task in Task.all_tasks if task.assigned_to_id == self.id]
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"


class Project:
    all_projects = []
    
    def __init__(self, title, description, due_date, project_id=None):
        self.id = project_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_ids = []  
        self.task_ids = []  
        Project.all_projects.append(self)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'user_ids': self.user_ids,
            'task_ids': self.task_ids
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(data['title'], data['description'], data['due_date'], data['id'])
        project.user_ids = data.get('user_ids', [])
        project.task_ids = data.get('task_ids', [])
        return project
    
    def __str__(self):
        return f"{self.title} (Due: {self.due_date})"
    
    def __repr__(self):
        return f"Project(id='{self.id}', title='{self.title}', due_date='{self.due_date}')"

class Task:
    all_tasks = []
    
    def __init__(self, title, status, assigned_to_id=None, project_id=None, task_id=None):
        self.id = task_id or str(uuid.uuid4())
        self.title = title
        self.status = status
        self.assigned_to_id = assigned_to_id 
        self.project_id = project_id
        Task.all_tasks.append(self)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'assigned_to_id': self.assigned_to_id,
            'project_id': self.project_id
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['title'], 
            data['status'], 
            data.get('assigned_to_id'),
            data.get('project_id'),
            data['id']
        )
    
    def __str__(self):
        return f"{self.title} [{self.status}]"
    
    def __repr__(self):
        return f"Task(id='{self.id}', title='{self.title}', status='{self.status}')"

# Data persistence functions
def save_to_json(filename='data/objects.json'):
    data = {
        'users': [user.to_dict() for user in User.all_users],
        'projects': [project.to_dict() for project in Project.all_projects],
        'tasks': [task.to_dict() for task in Task.all_tasks]
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_from_json(filename='data/objects.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Clear existing data
        User.all_users.clear()
        Project.all_projects.clear()
        Task.all_tasks.clear()
        
        # Load users
        for user_data in data.get('users', []):
            User.from_dict(user_data)
        
        # Load projects
        for project_data in data.get('projects', []):
            Project.from_dict(project_data)
        
        # Load tasks
        for task_data in data.get('tasks', []):
            Task.from_dict(task_data)
            
    except FileNotFoundError:
        print("No existing data file found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading data file. Starting fresh.")