# Project Name

Short project description goes here.

## Prerequisites

- Python 3.x
- Django
- djangorestframework==3.14.0

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-repository.git
   ```
## Install dependencies:

   ```
   pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

### Run the development server:

```
python manage.py runserver
```

## Open your API testing tool and test.

Usage
This project creates an API to create reminders. 

## API Endpoints
### Create Reminder:
Method: POST
Endpoint: 
```
  http://127.0.0.1:8000/create/
```
 Request Body Example:

```
  {
      "date": "2024-03-15",
      "time": "08:00:00",
      "message": "Don't forget to submit the report",
      "reminder_type": "SMS",
      "mobile_number": "1234567890"
  }
```
### List All Reminders:
Method: GET
Endpoint: ``` http://127.0.0.1:8000/reminders/```

### Retrieve a Specific Reminder:
Method: GET
Endpoint: ``` http://127.0.0.1:8000/reminder/<int:pk>/```

### Update a Specific Reminder (Full Update):

Method: PUT 
Endpoint: ```http://127.0.0.1:8000/update/<int:pk>/ ```
Request Body Example:
```bash
{
    "date": "2024-03-20",
    "time": "10:30:00",
    "message": "Submit the final report",
    "reminder_type": "Email",
    "email": "user@example.com"
}
```
### Update a Specific Reminder:
Method: PUT
Endpoint: ```http://127.0.0.1:8000/update/<int:pk>/```
Request Body Example:
```
{
    "message": "Updated message"
}
```
