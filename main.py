import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from server.youdao_translator import translate
from server.janome_tokenizer import text2furigana

app = FastAPI()
if pathlib.Path('dist').exists():
    app.mount('/dist', StaticFiles(directory='dist'), name='dist')

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


class Text(BaseModel):
    text: str


@app.post('/api/v1/translate')
async def translate_api(req: Text):
    return await translate(req.text)


@app.post('/api/v1/tokenize')
def tokenize_api(req: Text):
    return text2furigana(req.text)


@app.get('/{path:path}')
def index():
    return FileResponse('dist/index.html', media_type='text/html')
