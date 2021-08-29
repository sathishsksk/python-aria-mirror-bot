from pyrogram import Client

API_KEY = int(input("Enter API KEY: 1677067"))
API_HASH = input("Enter API HASH: 0d8c8aabe36b01db6a26a7f2780fa660")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
