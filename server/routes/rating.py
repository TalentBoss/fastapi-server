import openai
from fastapi import APIRouter, Request, FastAPI
import urllib.parse
import json
from server.controllers.chat import (
    add_chat
)


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
    new_chat = await add_chat(parsed_data)
    print(new_chat)
    # initial_question = [
    #   {
    #     'role': 'bot',
    #     'content': "Please answer about " + parsed_data['content']
    #   }
    # ]
    # completion = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
    #   messages=initial_question,
    #   max_tokens=1024,
    #   temperature=1
    # )
    #
    # print(completion.choices[0].message)
    # return ResponseModel(completion.choices[0].message, "This is set rating")
    return ResponseModel("When I moved to California from Toronto, I didn't know any English. It was tough, and I had to go to remedial classes even though I was good at science and math. I always thought that being in remedial classes meant that I was not smart and would never be able to catch up with my friends in advanced classes. I was really worried about my future and if I could even go to a good college. But one day, I read a book called Ender's Game and it changed how I thought about myself. ", "This is set rating")

