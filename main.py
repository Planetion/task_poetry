from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def name():
    return {"surname": "Меньшаков", "name": "Борис", "patronymic": "Юрьевич"}

@app.get('/tools')
async def skills():
    return "Начинающий"

@app.get('/users')
async def number():
    return "89130825741"
