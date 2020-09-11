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
        "name":"APS1",
        "description":"Aps 1 de Megadados",
        "status":False },
    uuid.uuid4(): {
        "name":"H1",
        "description":"Roteiro de Computacao em Nuvem",
        "status":False },
    uuid.uuid4(): {
        "name":"Entrega 2",
        "description":"Turorial 2 e entraga 2 de SoC Linux",
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
    task_dict = task.dict()
    tasks[id] = task_dict
    return {"id" : id}


@app.patch("/edit/{id}", summary="Edita uma task", tags=["task"])
async def edit_tas(id: uuid.UUID, taskDesc: TaskDescription):
    """
    - **description**: descrição
    """

    if id  not in tasks:
        raise HTTPException(status_code=404, detail="ID not found")

    tasks[id]["description"] = taskDesc.description 
    

    return tasks[id]

@app.patch("/status/{id}", summary="Atualiza a situação de uma task", tags=["task"])
async def edit_tas(id: uuid.UUID, taskStatus: TaskStatus):
    """
    - **status**: Situação da tarefa
    """
    if id  not in tasks:
        raise HTTPException(status_code=404, detail="ID not found")
    tasks[id]["status"] = taskStatus.status
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
            ## Aprendemos como esse FOR funciona pelo https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys 
            ## e mostramos pra algunmas pessoas da sala que estão com duvida em como filtrar o dicionario sem muitos FORs  
            filtered_tasks = {k:v for k,v in tasks.items() if v["status"]}
        else:
            filtered_tasks =  {k:v for k,v in tasks.items() if not v["status"]}
        return filtered_tasks
    
    return tasks

