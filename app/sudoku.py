"""Pure-Python Sudoku generation and validation."""
import random

LEVELS = {"easy": 36, "medium": 32, "hard": 28, "expert": 25, "master": 22}

def candidates(board, index):
    if board[index]:
        return set()
    row, col = divmod(index, 9)
    used = set(board[row*9:row*9+9])
    used.update(board[col::9])
    br, bc = (row//3)*3, (col//3)*3
    used.update(board[r*9+c] for r in range(br,br+3) for c in range(bc,bc+3))
    return set(range(1,10))-used

def valid(board):
    if len(board)!=81 or any(type(n) is not int or n<0 or n>9 for n in board):
        return False
    groups = [[board[r*9+c] for c in range(9)] for r in range(9)]
    groups += [[board[r*9+c] for r in range(9)] for c in range(9)]
    groups += [[board[r*9+c] for r in range(br,br+3) for c in range(bc,bc+3)] for br in (0,3,6) for bc in (0,3,6)]
    return all(len([n for n in g if n])==len(set(n for n in g if n)) for g in groups)

def solve(board, limit=1, randomized=False):
    """Return up to `limit` solutions; MRV backtracking."""
    if not valid(board):
        return []
    work=board.copy()
    results=[]
    def visit():
        if len(results)>=limit:
            return
        empty=[i for i,n in enumerate(work) if not n]
        if not empty:
            results.append(work.copy()); return
        index=min(empty,key=lambda i:len(candidates(work,i)))
        options=list(candidates(work,index))
        if randomized: random.shuffle(options)
        else: options.sort()
        for value in options:
            work[index]=value
            visit()
            work[index]=0
            if len(results)>=limit: return
    visit()
    return results

def generate(level):
    if level not in LEVELS: raise ValueError('Unknown difficulty')
    solution=solve([0]*81,randomized=True)[0]
    puzzle=solution.copy()
    cells=list(range(81)); random.shuffle(cells)
    for index in cells:
        if sum(bool(n) for n in puzzle)<=LEVELS[level]: break
        original=puzzle[index]; puzzle[index]=0
        if len(solve(puzzle,limit=2))!=1: puzzle[index]=original
    return {"puzzle":puzzle,"solution":solution,"difficulty":level,"clues":sum(bool(n) for n in puzzle)}
