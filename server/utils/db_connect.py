import motor.motor_asyncio

from server.config.mongodb import (
  MONGO_DETAILS
)

try:
  client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
  print('\n* Connected to MongoDB server successfully!\n')
  
except Exception as e:
  print(f"\n* Failed to connect to MongoDB server: {e} \n")
