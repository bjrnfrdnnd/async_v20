import asyncio
import os
import inspect
from async_v20 import OandaClient
from pathlib import Path
from async_v20.definitions.definitions import ROOT_DIR
import logging
import logging.config

# set up logging
logging_ini_path = os.path.join(ROOT_DIR, 'config', 'logging.ini')
logging.config.fileConfig(logging_ini_path, disable_existing_loggers=False)

logger = logging.getLogger('async_v20')

client = OandaClient()

async def get_account():
    async with OandaClient() as client:
        return await client.account()

loop = asyncio.get_event_loop()
account = loop.run_until_complete(get_account())

# pandas Series
print(account.series())

# HTTP response state
print(account)

# JSON data in python dictionary format
print(account.dict())

loop.run_until_complete(client.close())