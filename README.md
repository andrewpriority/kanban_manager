# kanban_manager - v0.1.0
kanban_manager is a Python API wrapper for the kanbantool.com web v3 API.
kanban_manager allows for a quick integration of the kanbantool.com API into a python project.
The library is intended to be used for simple cases, as it only targets the essential endpoints for the kanbantool.com API.

## Getting Started
### Prerequisites

```bash
pip install requests
```

### Usage

```python
from kanban_manager import kanban_manager

auth_token = 'QWERTY' # This auth token should be replaced with one from the Settings page of kanbantool.com in order to access your boards
subdomain = 'subdomain' # This subdomain should be replaced with the one provided when your kanbantool.com account was created

km = kanban_manager(auth_token, subdomain) # Initializes the class with the according auth_token and subdomain
tasks_response = get_board_tasks(12345) # Returns the body of the request response in JSON format
```

## Features

- Getting user info
- Getting board info
- Getting board tasks
- Creating a new task
- Deleting an existing task
- Updating a task
