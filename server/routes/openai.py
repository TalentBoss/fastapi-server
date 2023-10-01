import openai
from fastapi import APIRouter, Request, FastAPI
import urllib.parse
import json

from server.config.api_key import (
  api_key
)

from server.utils.response import (
  ResponseModel
)

openai.api_key = api_key

app = FastAPI()
router = APIRouter()


@router.get('/')
def root():
    return ResponseModel('Hi guy', 'This is a public endpoint')


@router.post('/get-response')
async def get_response(request: Request):
    question = await request.body()
    decoded_string = urllib.parse.unquote(question)
    parsed_data = json.loads(decoded_string)
    print(parsed_data)

    initial_question = [
      {
        'role': 'system',
        'content': "Please write two 250-650 word essays. " +
                   "The first should be an example of a strong personal statement with " + parsed_data['strong_attribute'] + " for a college application, labeled 'Strong Essay', " +
                   "and the second should be a weak personal statement with " + parsed_data['weak_attribute'] + " for a college application, labeled 'Weak Essay'. " +
                   "Please use the following information to inform both essays: A student that is a " + parsed_data['identity'] + " and " + parsed_data['wildcard'] +
                   " And use the below prompt: " + parsed_data['common_prompt']
      }
    ]
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=initial_question,
      max_tokens=1024,
      temperature=1
    )

    print(completion.choices[0].message)

    return ResponseModel(completion.choices[0].message, "This is a response")
    
