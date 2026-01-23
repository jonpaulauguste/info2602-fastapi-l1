from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student
### End of new function