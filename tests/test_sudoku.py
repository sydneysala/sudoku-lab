from app.sudoku import candidates, generate, solve, valid, LEVELS

def test_invalid_duplicate():
    board=[0]*81;board[0]=1;board[1]=1
    assert not valid(board)

def test_solve_known():
    board=[int(c) for c in '530070000600195000098000060800060003400803001700020006060000280000419005000080079']
    result=solve(board)
    assert len(result)==1 and all(result[0]) and valid(result[0])

def test_all_levels_unique():
    for level in LEVELS:
        game=generate(level)
        assert valid(game['puzzle'])
        assert len(solve(game['puzzle'],limit=2))==1
        assert game['clues']>=LEVELS[level]

def test_candidates():
    board=[0]*81;board[0]=5
    assert 5 not in candidates(board,1)
