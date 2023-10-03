from fastapi import APIRouter, Request, FastAPI
import urllib.parse
import json



from server.utils.response import (
  ResponseModel
)

app = FastAPI()
router = APIRouter()


@router.get('/')
def root():
    return ResponseModel('Hi ssdsdsd', 'This is a public endpoint')



@router.post('/set-rating')
async def set_response(request: Request):
    question = await request.body()
    decoded_string = urllib.parse.unquote(question)
    parsed_data = json.loads(decoded_string)
    print(parsed_data)
    return ResponseModel("set rating", "This is set rating")

