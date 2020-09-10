# • Criar uma tarefa
#      A tarefa tem uma breve descrição
#      A tarefa começa como não-concluida
# • Alterar a descrição de uma tarefa
# • Marcar uma tarefa como concluida, ou marcá-la novamente como não-concluida
# • Remover uma tarefa
# • Listar as tarefas
#     Deve-se permitir a listagem de tarefas concluidas, não-concluidas, ou todas

from typing import Optional, List
import uuid
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel
class Task(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status:  Optional[bool] = False


app = FastAPI()

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


#ok
@app.post("/create/")
async def create_task(task: Task):
    
    task.id = uuid.uuid4()
    #tasks.append(task)
    tasks[uuid] = task
    return task.id

#ok
@app.patch("/edit/{id}")
async def edit_tas(id: uuid.UUID, task: Task):
    if task.description!= None:
        tasks[id]["description"] = task.description 
            
    return tasks[id]



#ok
@app.delete("/delete/{id}")
async def delete_task(id:UUID):
    del tasks[id]
    return "Success"


#listagem de tarefas concluidas, não-concluidas, ou todas
@app.get("/list/")
async def list_task(q: Optional[bool] = None):
    if q is not None:
        if q:   
            filtered_tasks = {k:v for k,v in tasks.items() if v["status"]}
        else:
            filtered_tasks =  {k:v for k,v in tasks.items() if not v["status"]}
        return filtered_tasks
    
    return tasks






#{k:v fpr k,v in tasks.items() if v.status}