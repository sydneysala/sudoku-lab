from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get('/api/health').json()=={'status':'ok'}
def test_unknown_level(): assert client.get('/api/puzzles/impossible').status_code==404
def test_check():
    assert client.post('/api/check',json={'board':[0]*81}).json()=={'valid':True,'complete':False}
