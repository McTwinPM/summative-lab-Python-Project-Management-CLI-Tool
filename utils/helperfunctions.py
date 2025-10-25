import os
import json
from datetime import datetime
from typing import Optional, List
from models.Classes import User, Project, Task

def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_date(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def validate_status(status: str) -> bool:
    """Validate task status."""
    valid_statuses = {'todo', 'in-progress', 'done'}
    return status in valid_statuses

def validate_complete_task(task: Task) -> bool:
    """Check if a task can be marked as complete."""
    return task.status == 'done'