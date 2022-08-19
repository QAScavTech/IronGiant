# app data IronGiant.py
import os
from re import T # operating system library

import discord 
from dotenv import dotenv_values

import pprint

envdic = dict(dotenv_values('.env'))
# pprint.pprint(envdic, width = 1)

Token = envdic['DISCORD_TOKEN']

Client = discord.Client()

@Client.event
async def on_ready():
    print(f'{Client.user} has connected to Discord!')


Client.run(Token)





# def main():
    # load_dotenv()

    # Token = os.getenv('D_TOKEN')

    # Client = discord.Client()

    # Client.run(Token)

# if __name__ == "__main__":
    # main()