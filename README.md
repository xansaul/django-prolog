## Steps to Run the Project


## Prolog Configuration

Set environment variable on your operating system.

```
SWI_HOME_DIR=C:\\Program Files\\swipl
```

## Django project

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

On Unix-based systems (Linux/macOS):

```bash
source venv/bin/activate
```
On Windows (PowerShell):

```bash
.\venv\Scripts\Activate
```

### 3. Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```
### 4. Perform Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the Development Server

```bash
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/. You can access the application in your web browser.
