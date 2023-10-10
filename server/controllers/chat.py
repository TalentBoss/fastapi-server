from bson.objectid import ObjectId

from server.utils.db_connect import (
  client
)


if client is not None:
  chat_db = client.chat
  chat_collection = chat_db.get_collection('chat_collection')



def chat_helper(chat) -> dict:
  return {
    "id": str(chat['_id']),
    "fullname": chat['fullname'],
    "email": chat['email'],
    "content": chat['content']
  }


async def retrieve_chats():
  chats = []
  async for chat in chat_collection.find():
    chats.append(chat_helper(chat))
  return chats

async def add_chat(chat_data: dict) -> dict:
  chat = await chat_collection.insert_one(chat_data)
  new_chat = await chat_collection.find_one({'_id': chat.inserted_id})
  return chat_helper(new_chat)

