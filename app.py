from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

DATABASE_URL = "sqlite:///tasks.db"

app = FastAPI()

# Database models
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False

# Database connection
def get_db():
    db = sqlite3.connect(DATABASE_URL)
    db.row_factory = sqlite3.Row
    return db

# API endpoints
@app.get("/tasks", response_model=List[Task])
async def list_tasks():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return [Task(**row) for row in tasks]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    db = get_db()
    db.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task.title, task.description))
    db.commit()
    task.id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    return task

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    db = get_db()
    task = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task(**task)

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    db = get_db()
    db.execute("UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?", (task.title, task.description, task.completed, task_id))
    db.commit()
    updated_task = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return Task(**updated_task)

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return {"message": "Task deleted"}

# Initialize the database table
def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT FALSE
        )
    """)
    db.commit()

if __name__ == "__main__":
    init_db()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)