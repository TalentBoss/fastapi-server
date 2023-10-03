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

    # initial_question = [
    #   {
    #     'role': 'system',
    #     'content': "Please write two 250-650 word essays. " +
    #                "The first should be an example of a strong personal statement with " + parsed_data['strong_attribute'] + " for a college application, labeled 'Strong Essay', " +
    #                "and the second should be a weak personal statement with " + parsed_data['weak_attribute'] + " for a college application, labeled 'Weak Essay'. " +
    #                "Please use the following information to inform both essays: A student that is a " + parsed_data['identity'] + " and " + parsed_data['wildcard'] +
    #                " And use the below prompt: " + parsed_data['common_prompt']
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
    #
    txt = "Strong Essay: When I moved to California from Toronto, I didn't know any English. It was tough, and I had to go to remedial classes even though I was good at science and math. I always thought that being in remedial classes meant that I was not smart and would never be able to catch up with my friends in advanced classes. I was really worried about my future and if I could even go to a good college. But one day, I read a book called Ender's Game and it changed how I thought about myself. The book is about a young boy who is really smart but people underestimate him. After reading it, I started believing that I could do better. I talked to my teachers and started studying more to get into better classes. I'm still not in the AP classes like some of my friends, but I get good grades and want to be an engineer. Reading that book made me...(con’t scroll) Weak Essay:  In Toronto, where I spent my childhood, the night sky was often eclipsed by skyscrapers and bright city lights. When I moved to Palo Alto at the age of 11, I experienced my first clear view of a starry sky. But adjusting to a new country was like navigating through an unfamiliar galaxy. Not only did I have to learn English, but my limited proficiency also landed me in remedial classes for math and science—subjects in which I had always excelled. Placed in a track I knew didn't represent my abilities, I faced a deep-rooted belief: that remedial classes were a measure of intellectual limitations. This labeling gnawed at me, perpetuating the idea that I would never reach the advanced level courses that my peers took for granted....(con’t on scroll)"
    # return ResponseModel(completion.choices[0].message, "This is a response")
    return ResponseModel(txt, "This is a response")
    
