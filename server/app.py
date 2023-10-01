from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from server.routes.openai import router as OpenAIRouter

app = FastAPI()
origin = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origin,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']

)

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
def form_post(request: Request):
  return templates.TemplateResponse(
    'index.html', context={'request': request, 'result': 'hi there'}
  )



app.include_router(OpenAIRouter, tags=['openai'], prefix='/openai')
