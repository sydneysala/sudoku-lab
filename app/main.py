"""HTTP routes for Sudoku Lab."""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from .sudoku import LEVELS, generate, valid

app=FastAPI(title="Sudoku Lab", docs_url="/api/docs", redoc_url=None)
STATIC=Path(__file__).parent/'static'
app.mount('/static',StaticFiles(directory=STATIC),name='static')

class CheckRequest(BaseModel):
    board: list[int] = Field(min_length=81,max_length=81)

@app.get('/')
def home(): return FileResponse(STATIC/'index.html')

@app.get('/api/health')
def health(): return {'status':'ok'}

@app.get('/api/puzzles/{difficulty}')
def puzzle(difficulty:str):
    if difficulty not in LEVELS: raise HTTPException(404,'Unknown difficulty')
    result=generate(difficulty)
    return {k:v for k,v in result.items() if k!='solution'}

@app.post('/api/check')
def check(request:CheckRequest):
    return {'valid':valid(request.board),'complete':valid(request.board) and all(request.board)}
