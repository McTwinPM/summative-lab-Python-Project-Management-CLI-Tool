# summative-lab-Python-Project-Management-CLI-Tool


Python Management CLI Tool

To begin, make sure the directory is wherever the "summative-lab-Python-Project-Management-CLI-Tool" folder is installed

CLI commands:
Begin all CLI commands with: 

'python3 main.py' 

This will tell the tool to activate the main function (remember to keep spaces between each command)

Here's an example command: "python3 main.py task list" This command will display a list of all tasks, along with itentifying information. This will display a table like this:

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ ID       ┃ Title             ┃ Status      ┃ Assigned To ┃ Project     ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ task-789 │ Create wireframes │ in_progress │ user-123    │ project-456 │
└──────────┴───────────────────┴─────────────┴─────────────┴─────────────┘

This is an example of how the tool should look after entering a correct command. If you ever forget what command you need, you can use the "-h" or "--help" command to show you a list of commands in the directory.
If you ever type a wrong command, read the error message that displays and start over.

For your third command (i.e. the third word) you will type one of three commands, depending on which function you need access to.
    1. user - This will tell the tool to access "User management"
    2. project - This will tell the tool to access "Project management"
    3. task - This will tell the tool to access "Task management"


User Management
The User commands are as follows:
- 'add' (add a User) To add a user, you will need to type the full name of the user, followed by the user's email (both surrounded by quotation marks)

- remove (remove a User) To remove a user, you will need to type the user ID given to the user when the user was added to the system

- list (list all Users) This will display all users in the system

Project Management
The Project commands are as follows:
- add (add a Project) To add a project, you will need to type the Title of the project, a short description of the project (both surrounded by quotation marks), and the due date of the project (in YYYY-MM-DD format)

- remove (remove a Project) To remove a project, you will need to type the user ID given to the project when the project was added to the system

- list (list all Projects) This will display all projects in the system

Task Management
The Task commands are as follows:
- add (add a Task) To add a task, you will need to type the Title of the task,  (both surrounded by quotation marks)

- remove (remove a Project) To remove a project, you will need to type the user ID given to the project when the project was added to the system

- update-status (update the status of a Task) To update the status of a task, you will need the task_id, followed by one of the following: 'todo', 'in_progress', or 'done'

- assign (assign a User to the Task) To assign a user to the task, you will need the task_id, followed by the user_id

- list (list all Tasks) This will display all tasks in the system





