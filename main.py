from typing import Optional, List
import uuid
from uuid import UUID
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: str 
    status:  bool = False

class TaskDescription(BaseModel):
    description: str 

class TaskStatus(BaseModel):
    status: bool 
    
app = FastAPI(
    title="Task API",
    description="Task API para APS1 matéria Megadados, 2SEM-2020. Emanuelle e Leonardo",
    version="0.9.0",
)

tasks = {
    uuid.uuid4(): {
        "name":"nome",
        "description":"abc",
        "status":False },
    uuid.uuid4(): {
        "name":"nome1",
        "description":"qqq",
        "status":False },
    uuid.uuid4(): {
        "name":"nome2",
        "description":"ff",
        "status":True}
}


@app.post("/create/", status_code=201,summary="Cria uma task", tags=["task"])
async def create_task(task: Task):
    """
    - **name**: Título da tarefa
    - **description**: Descrição da tarefa
    - **status**: Situação da tarefa
    """
    
    id = uuid.uuid4()
    tasks[id] = task
    return id


@app.patch("/edit/{id}", summary="Edita uma task", tags=["task"])
async def edit_tas(id: uuid.UUID, task: TaskDescription):
    """
    - **description**: descrição
    """

    if id  not in tasks:
        raise HTTPException(status_code=404, detail="ID not found")

    tasks[id]["description"] = task.description 
    

    return tasks[id]

@app.patch("/status/{id}", summary="Atualiza a situação de uma task", tags=["task"])
async def edit_tas(id: uuid.UUID, task: TaskStatus):
    """
    - **status**: Situação da tarefa
    """
    if id  not in tasks:
        raise HTTPException(status_code=404, detail="ID not found")
    tasks[id]["status"] = task.status
    return tasks[id]



@app.delete("/delete/{id}", status_code=204, summary="Deleta uma task", tags=["task"])
async def delete_task(id:UUID):
    """
    - **ID**: ID da tarefa
    """
    if id  not in tasks:
        raise HTTPException(status_code=404, detail="ID not found")

    del tasks[id]


@app.get("/list/", summary="Lista as tasks", tags=["task"])
async def list_task(q: Optional[bool] = None):
    """
    Listar as tarefas:

    - **--**: Todas as tarefas
    - **True**: Tarefas concluídas
    - **False**: Tarefas não-concluídas
    """
    if q is not None:
        if q:   
            filtered_tasks = {k:v for k,v in tasks.items() if v["status"]}
        else:
            filtered_tasks =  {k:v for k,v in tasks.items() if not v["status"]}
        return filtered_tasks
    
    return tasks

