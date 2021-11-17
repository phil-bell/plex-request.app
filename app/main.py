from subprocess import run as _run
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()

def run(command: str):
    _run(command.split())


@app.post("/torrent/add/")
async def root(magnet: str, path: str):
    run(f'deluge-console add "add -path {path} {magnet}"')
