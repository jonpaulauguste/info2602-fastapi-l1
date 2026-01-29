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
            if student['pref'] == pref: 
                filtered_students.append(student)
        return filtered_students
    return data

# Exercise 1

@app.get('/stats')
async def get_stats():
    stats = {
        "Chicken": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Fish": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
        "Vegetable": 0
    }

    for student in data:
        pref = student['pref'].strip()
        programme = student['programme'].strip()

        if pref in stats:
            stats[pref] += 1

        if programme in stats:
            stats[programme] += 1

    return stats

# Exercise 2

@app.get('/add/{a}/{b}')
async def add(a: int, b: int):
    return {"result": a + b}

@app.get('/subtract/{a}/{b}')
async def subtract(a: int, b: int):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def multiply(a: int, b: int):
    return {"result": a * b}

@app.get('/divide/{a}/{b}')
async def divide(a: int, b: int):   
    if b == 0:
        return {"error": "Division by zero is not allowed...Please try again."}
    return {"result": a / b}

