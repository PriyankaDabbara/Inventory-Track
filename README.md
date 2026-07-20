# FastAPI Product API with React Frontend

This project combines a FastAPI backend with a React frontend. The backend exposes CRUD endpoints for `Product` data and stores records in PostgreSQL via SQLAlchemy. The frontend runs from the `frontend/` folder and is configured to proxy API requests to the FastAPI server.

## Project structure

- `main.py` - FastAPI application and CRUD endpoints
- `database.py` - SQLAlchemy engine and session configuration
- `database_models.py` - SQLAlchemy database models
- `models.py` - Pydantic request/response models
- `frontend/` - React application
- `.gitignore` - ignores local env files, virtualenv, Node modules, build output, and editor/OS artifacts

## Requirements

- Python 3.10+
- PostgreSQL database
- Node.js and npm for frontend
- Virtual environment is recommended

## Setup

1. Activate the Python virtual environment:

```powershell
cd C:\Users\Desktop\FastAPI-Project
& .\myenv\Scripts\Activate.ps1
```

2. Install backend dependencies:

```powershell
pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
```

3. Install frontend dependencies:

```powershell
cd frontend
npm install
```

4. Configure your database connection:

The current database URL is in `database.py`:

```python
db_url = "postgresql://postgres"  enter your db_url
```

For production or shared repositories, do not commit credentials. Use environment variables or a `.env` file and keep them out of Git.

## Run the app

Start the backend:

```powershell
cd C:\Users\Desktop\FastAPI-Project
uvicorn main:app --reload
```

Start the frontend:

```powershell
cd C:\Users\Desktop\FastAPI-Project\frontend
npm start
```

The frontend is configured to proxy API requests to `http://localhost:8000`.

## API Endpoints

- `GET /products` - list all products
- `GET /products/{id}` - get a single product by ID
- `POST /products` - create a product
- `PUT /products/{id}` - update a product
- `DELETE /products/{id}` - delete a product

