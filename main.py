from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
                filtered_students.append(student)
        return filtered_students
    return data

@app.get('/stats')
async def get_stats():
    stats = {}

    for student in data:
        pref = student['pref']
        if pref in stats:
            stats[pref] += 1
        else:
            stats[pref] = 1

        programme = student['programme']
        if programme in stats:
            stats[programme] += 1
        else:
            stats[programme] = 1
        
    return stats

