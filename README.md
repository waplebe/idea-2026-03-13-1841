# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It includes a backend API built with FastAPI and a basic frontend for creating, reading, updating, and deleting tasks.  The frontend is intentionally minimal to demonstrate the API functionality.

**Why it's useful:**

This project is a good starting point for learning about RESTful API development and frontend integration. It's a practical example of a simple task management system that can be easily extended with more features.

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    *   Create a `.env` file in the root directory and populate it with the following (replace with your actual values):
        ```
        DATABASE_URL=sqlite:///tasks.db
        ```
    *   Run the backend server:
        ```bash
        uvicorn app:app --reload
        ```

3.  **Set up the frontend:**
    *   Open `frontend/index.html` in your web browser.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `GET /tasks/{task_id}`: Retrieves a specific task by ID.
*   `PUT /tasks/{task_id}`: Updates a specific task by ID. Request body should be a JSON object with `title` and/or `description` fields.
*   `DELETE /tasks/{task_id}`: Deletes a specific task by ID.

**Examples:**

*   **Create a task:**
    `POST /tasks`
    Request Body:
    ```json
    {
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread",
      "completed": false
    }
    ```

*   **Get all tasks:**
    `GET /tasks`
    Response:
    ```json
    [
      {
        "id": 1,
        "title": "Grocery Shopping",
        "description": "Buy milk, eggs, and bread",
        "completed": false
      },
      {
        "id": 2,
        "title": "Pay Bills",
        "description": "Pay electricity and internet bills",
        "completed": true
      }
    ]
    ```

**Dependencies:**

*   FastAPI
*   uvicorn
*   SQLAlchemy
*   Pydantic

**License:**

MIT License