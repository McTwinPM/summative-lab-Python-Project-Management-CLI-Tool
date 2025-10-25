#!/usr/bin/env python3

import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from models.Classes import User, Project, Task, save_to_json, load_from_json
from utils.helperfunctions import validate_email, validate_date, validate_status, validate_complete_task

console = Console()

def display_users():
    # Display users
    if not User.all_users:
        console.print("[yellow]No users found.[/yellow]")
        return
    # Rich table for users
    table = Table(title="Users")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Email", style="green")
    
    for user in User.all_users:
        table.add_row(user.id, user.name, user.email)
    
    console.print(table)

def display_projects():
    # Display projects
    if not Project.all_projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    # Rich table for projects
    table = Table(title="Projects")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="green")
    
    for project in Project.all_projects:
        table.add_row(project.id, project.title, project.description, project.due_date)
    
    console.print(table)

def display_tasks():
    # Display tasks
    if not Task.all_tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    # Rich table for tasks
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Status", style="white")
    table.add_column("Assigned To", style="blue")
    table.add_column("Project", style="green")
    
    for task in Task.all_tasks:
        # Get status color
        status_color = "green" if task.status == "completed" else "yellow" if task.status == "in_progress" else "red"
        status_text = f"[{status_color}]{task.status}[/{status_color}]"
        
        table.add_row(
            task.id, 
            task.title, 
            status_text,
            task.assigned_to_id or "Unassigned",
            task.project_id or "No Project"
        )
    
    console.print(table)

def main():
    load_from_json()
    
    parser = argparse.ArgumentParser(
        description='Project Management CLI Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # User commands
    user_parser = subparsers.add_parser('user', help='User management')
    user_subparsers = user_parser.add_subparsers(dest='user_action')
    
    # Create user
    add_user = user_subparsers.add_parser('add', help='Add a new user')
    add_user.add_argument('name', help='User name')
    add_user.add_argument('email', help='User email')

    # Remove user
    remove_user = user_subparsers.add_parser('remove', help='Remove a user')
    remove_user.add_argument('user_id', help='User ID to remove')

    # List users
    user_subparsers.add_parser('list', help='List all users')
    
    # Project commands
    project_parser = subparsers.add_parser('project', help='Project management')
    project_subparsers = project_parser.add_subparsers(dest='project_action')
    
    # Create project
    add_project = project_subparsers.add_parser('add', help='Add a new project')
    add_project.add_argument('title', help='Project title')
    add_project.add_argument('description', help='Project description')
    add_project.add_argument('due_date', help='Due date (YYYY-MM-DD)')

    # Remove project
    remove_project = project_subparsers.add_parser('remove', help='Remove a project')
    remove_project.add_argument('project_id', help='Project ID to remove')

    # List projects
    project_subparsers.add_parser('list', help='List all projects')
    
    # Task commands
    task_parser = subparsers.add_parser('task', help='Task management')
    task_subparsers = task_parser.add_subparsers(dest='task_action')
    
    # Create task
    add_task = task_subparsers.add_parser('add', help='Add a new task')
    add_task.add_argument('title', help='Task title')
    add_task.add_argument('--status', default='todo', help='Task status')
    add_task.add_argument('--assigned-to', help='User ID to assign task to')
    add_task.add_argument('--project', help='Project ID for the task')

    # Remove task
    remove_task = task_subparsers.add_parser('remove', help='Remove a task')
    remove_task.add_argument('task_id', help='Task ID to remove')

    # List tasks
    task_subparsers.add_parser('list', help='List all tasks')
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'user':
        if args.user_action == 'add':
            if not validate_email(args.email):
                console.print(f"[red]Invalid email format: {args.email}[/red]")
                sys.exit(1)
            user = User(args.name, args.email)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Added user: [bold]{user.name}[/bold] ({user.email})\nID: [cyan]{user.id}[/cyan]",
                title="User Added",
                border_style="green"
            ))
        elif args.user_action == 'remove':
            user_to_remove = next((u for u in User.all_users if u.id == args.user_id), None)
            if not user_to_remove:
                console.print(f"[red]User with ID {args.user_id} not found.[/red]")
                sys.exit(1)
            User.all_users.remove(user_to_remove)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Removed user with ID: [cyan]{args.user_id}[/cyan]",
                title="User Removed",
                border_style="green"
            ))
        elif args.user_action == 'list':
            display_users()
                
    elif args.command == 'project':
        if args.project_action == 'add':
            if not validate_date(args.due_date):
                console.print(f"[red]Invalid date format: {args.due_date}. Use YYYY-MM-DD.[/red]")
                sys.exit(1)
            project = Project(args.title, args.description, args.due_date)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Added project: [bold]{project.title}[/bold]\nID: [cyan]{project.id}[/cyan]",
                title="Project Added",
                border_style="green"
            ))
        elif args.project_action == 'remove':
            project_to_remove = next((p for p in Project.all_projects if p.id == args.project_id), None)
            if not project_to_remove:
                console.print(f"[red]Project with ID {args.project_id} not found.[/red]")
                sys.exit(1)
            Project.all_projects.remove(project_to_remove)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Removed project with ID: [cyan]{args.project_id}[/cyan]",
                title="Project Removed",
                border_style="green"
            ))
        elif args.project_action == 'list':
            display_projects()
                
    elif args.command == 'task':
        if args.task_action == 'add':
            task = Task(args.title, args.status, getattr(args, 'assigned_to', None), args.project)
            if not validate_status(task.status):
                console.print(f"[red]Invalid task status: {task.status}. Must be one of 'todo', 'in-progress', 'done'.[/red]")
                sys.exit(1)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Added task: [bold]{task.title}[/bold]\nStatus: [yellow]{task.status}[/yellow]\nID: [cyan]{task.id}[/cyan]",
                title="Task Added",
                border_style="green"
            ))
        elif args.task_action == 'remove':
            task_to_remove = next((t for t in Task.all_tasks if t.id == args.task_id), None)
            if not task_to_remove:
                console.print(f"[red]Task with ID {args.task_id} not found.[/red]")
                sys.exit(1)
            if not validate_complete_task(task_to_remove):
                console.print(f"[red]Cannot remove task with ID {args.task_id} as it is not marked 'done'.[/red]")
                sys.exit(1)
            Task.all_tasks.remove(task_to_remove)
            save_to_json()
            console.print(Panel(
                f"[green]✓[/green] Removed task with ID: [cyan]{args.task_id}[/cyan]",
                title="Task Removed",
                border_style="green"
            ))
        elif args.task_action == 'list':
            display_tasks()
    else:
        console.print("[red]No command provided. Use --help for available commands.[/red]")
        parser.print_help()

if __name__ == "__main__":
    main()