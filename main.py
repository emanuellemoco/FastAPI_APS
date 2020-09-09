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
    id: int
    name: str
    description: Optional[str] = None
    status: bool = False


app = FastAPI()

tasks : List[Task] = [
    {
        "id":0,
        "name":"nome",
        "description":"abc",
        "status":False
    },
    {
        "id":1,
        "name":"nome1",
        "description":"qqq",
        "status":False
    },
    {
        "id":2,
        "name":"nome2",
        "description":"ff",
        "status":True
    }
]

id = 2


#ok
@app.post("/create/")
async def create_task(task: Task):
    global id
    id+=1
    task.id = id
    tasks.append(task)
    return task

#ok
@app.put("/edit/")
async def edit_task(id: int, description: str):
    
    for i in range(len(tasks)):
        if id == tasks[i]["id"]:
            tasks[i]["description"] = description
            return "Success"

    return "Error, name does not match with any." 

#ok
@app.put("/check/")
async def check_task(status: bool,id: int):
    for i in range(len(tasks)):
        if id == tasks[i]["id"]:
            tasks[i]["status"] = status

    return status

#ok
@app.delete("/delete/")
async def delete_task(task: Task):
    tasks.remove(task)
    return task

#listagem de tarefas concluidas, não-concluidas, ou todas
@app.get("/list/")
async def list_task(q: Optional[bool] = None):
    #if q is not None:
        #if q:
            #filtered_tasks = filtering(tasks,True)
            #filtered_tasks =  [x for x in tasks if x["status"] == True]
        #return n concluídas
        #else:
            #filtered_tasks = filtering(tasks,False)
            #filtered_tasks =  [x for x in tasks if not x["status"] == False]
        
        #return filtered_tasks
    
    
    return tasks

    
            

        
    return tasks
