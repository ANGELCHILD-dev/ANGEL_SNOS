from telethon.sync import TelegramClient
from telethon.tl.functions.account import GetAuthorizationsRequest, ResetAuthorizationRequest
from telethon.tl.types import Authorization
from telethon.sessions import StringSession

api_id = "5"
api_hash = "1c5c96d5edd401b1ed40db3fb5633e2d"

# ключ сессии для абуза защиты Telethon

session_string = input("введи ключ сессии:  ")
client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def remove_all_sessions_except_current():
    authorizations = await client(GetAuthorizationsRequest())

# Сравнение ip адреса с ip адресом клиента

    current_ip = client.session.server_address

# Инфа об сессии и устройстве

    for auth in authorizations.authorizations:
        if isinstance(auth, Authorization):
            print(f"\nID сессии: {auth.hash}\nУстройство: {auth.device_model}\nIP: {auth.ip}\nМестоположение: {auth.country}")

# Выбор
            if auth.ip != current_ip:
                confirm = input(f"Удалить эту сессию? (y/n): ").strip().lower()
                if confirm == 'y':
                    await client(ResetAuthorizationRequest(auth.hash))
                    print(f"Сессия с ID {auth.hash} удалена.")
                else:
                    print("Сессия не удалена.")
            else:
                print("Текущая сессия, пропускаем.")

    print("Процесс завершен.")

# Завершение работы при нажатии ctrl+z

async def main():
    await client.start()
    await remove_all_sessions_except_current()

# Бесконечный While

with client:
    client.loop.run_until_complete(main())
