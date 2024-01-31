from pydantic import BaseModel
from fastapi import FastAPI
from typing import List


app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False


tasks = []


@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return tasks


@app.get("/tasks/{id}", response_model=Task)
async def read_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    return {'error': 'Task not found'}


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put('/tasks/{id}', response_model=Task)
async def update_task(id: int, new_task: Task):
    for i, task in enumerate(tasks):
        if task.id == id:
            tasks[i] = new_task
            return new_task
    return {'error': 'Task not found'}


@app.delete('/tasks/{id}')
async def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task.id == id:
            del tasks[i]
            return {'message': 'Task deleted'}
    return {'error': 'Task not found'}
