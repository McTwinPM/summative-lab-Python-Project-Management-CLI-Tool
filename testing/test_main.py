import sys
import os
import pytest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main
from models.Classes import User, Project, Task

def setUp():
    """Clear all data before each test."""
    User.all_users.clear()
    Project.all_projects.clear()
    Task.all_tasks.clear()

def test_add_user():
    user = User("Test User", "testuser@example.com")
    assert user.name == "Test User"
    assert user.email == "testuser@example.com"

def test_add_project():
    project = Project("Test Project", "A project for testing", "2024-12-31")
    assert project.title == "Test Project"
    assert project.description == "A project for testing"
    assert project.due_date == "2024-12-31"

def test_add_task():
    task = Task("Test Task", status="todo")
    assert task.title == "Test Task"
    assert task.status == "todo"

def test_assign_task_to_user():
    user = User("Assignee", "assignee@example.com")
    task = Task("Test Task", status="todo")
    task.assign_to(user)
    assert task.assignee == user
    
def test_mark_task_complete():
    task = Task("Complete Task", status="done")
    assert task.status == "done"

def test_list_users():
    user1 = User("User One", "user1@example.com")
    user2 = User("User Two", "user2@example.com")
    users = [user1, user2]
    assert len(users) == 2
    assert users[0].name == "User One"
    assert users[1].name == "User Two"

def test_list_projects():
    project1 = Project("Project One", "First project", "2024-11-30")
    project2 = Project("Project Two", "Second project", "2024-12-31")
    projects = [project1, project2]
    assert len(projects) == 2
    assert projects[0].title == "Project One"
    assert projects[1].title == "Project Two"

def test_list_tasks():
    task1 = Task("Task One", status="todo")
    task2 = Task("Task Two", status="in-progress")
    tasks = [task1, task2]
    assert len(tasks) == 2
    assert tasks[0].title == "Task One"
    assert tasks[1].title == "Task Two"

def test_remove_user():
    user = User("Removable User", "removable@example.com")
    user.remove()
    assert user not in User.all_users

def test_remove_project():
    project = Project("Removable Project", "To be removed", "2024-10-31")
    project.remove()
    assert project not in Project.all_projects

def test_remove_task():
    task = Task("Removable Task", status="done")
    task.remove()
    assert task not in Task.all_tasks
    