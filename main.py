# • Criar uma tarefa
#      A tarefa tem uma breve descrição
#      A tarefa começa como não-concluida
# • Alterar a descrição de uma tarefa
# • Marcar uma tarefa como concluida, ou marcá-la novamente como não-concluida
# • Remover uma tarefa
# • Listar as tarefas
#     Deve-se permitir a listagem de tarefas concluidas, não-concluidas, ou todas

from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel
class Task(BaseModel):
    name: str
    description: Optional[str] = None
    status: bool = False


app = FastAPI()

tasks : List[Task] = [
    {
        "name":"nome",
        "description":"abc",
        "status":False
    }
]



#ok
@app.post("/create/")
async def create_task(task: Task):
    tasks.append(task)
    return task

#+/- ok
#arrumar os argumentos que recebe
@app.put("/edit/")
async def edit_task(task: Task):
    
    for i in range(len(tasks)):
        if task.name == tasks[i]["name"]:
            tasks[i]["description"] = task.description
            return task

    return "Error, name does not match with any." 

@app.put("/check/")
async def check_task(task: Task):
    return task

#ok
@app.delete("/delete/")
async def delete_task(task: Task):
    tasks.remove(task)
    return task

#falta as queries
@app.get("/list/")
async def list_task():
    return tasks
