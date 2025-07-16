from aiogram import Bot
import asyncio

from src.database.queries import get_all_users, update_user_deadlines, get_users_with_upcoming_deadlines
from src.parser.scraper import parse_deadlines_from_lk
from src.utils.crypto import decrypt_data

async def update_all_deadlines():
    """
    Задача для полного обновления дедлайнов для всех пользователей.
    """
    print("SCHEDULER: Запуск задачи обновления дедлайнов...")
    users = await get_all_users()
    for user in users:
        # Проверяем, что у пользователя есть сохраненные учетные данные
        if not user.encrypted_login_lk or not user.encrypted_password_lk:
            continue
        
        # Расшифровываем данные
        login = decrypt_data(user.encrypted_login_lk)
        password = decrypt_data(user.encrypted_password_lk)
        
        # Запускаем парсер
        loop = asyncio.get_event_loop()
        deadlines = await loop.run_in_executor(None, parse_deadlines_from_lk, login, password)
        
        if deadlines is not None:
            # Если парсинг прошел успешно, обновляем дедлайны в БД
            await update_user_deadlines(user.telegram_id, deadlines)
            print(f"SCHEDULER: Дедлайны для пользователя {user.telegram_id} успешно обновлены.")
        else:
            print(f"SCHEDULER: Не удалось обновить дедлайны для {user.telegram_id} (ошибка парсера).")
        
        await asyncio.sleep(5) # Небольшая задержка, чтобы не перегружать сайт ЛК

    print("SCHEDULER: Задача обновления дедлайнов завершена.")


async def send_deadline_notifications(bot: Bot):
    """
    Задача для отправки уведомлений о дедлайнах.
    """
    print("SCHEDULER: Запуск задачи отправки уведомлений...")
    # О каких дедлайнах мы хотим уведомлять (за сколько дней)
    notification_days = [1, 3, 7]

    for days_left in notification_days:
        users_to_notify = await get_users_with_upcoming_deadlines(days=days_left)
        
        for user, deadline in users_to_notify:
            text = (
                f"🔔 <b>Напоминание о дедлайне!</b>\n\n" 
                f"📚 <b>Предмет:</b> {deadline.course_name}\n" 
                f"📝 <b>Задание:</b> {deadline.task_name}\n\n"
                f"🗓️ <u>Осталось дней</u>: <b>{days_left}</b>"
            )
            try:
                await bot.send_message(chat_id=user.telegram_id, text=text, parse_mode="HTML")
                print(f"SCHEDULER: Отправлено уведомление пользователю {user.telegram_id}.")
            except Exception as e:
                # Обработка случая, если бот заблокирован пользователем
                print(f"SCHEDULER: Не удалось отправить уведомление {user.telegram_id}. Ошибка: {e}")
            
            await asyncio.sleep(1) # Небольшая задержка между отправками
    
    print("SCHEDULER: Задача отправки уведомлений завершена.")