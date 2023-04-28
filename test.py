import telebot
import json

from telebot.types import Message, User, Chat

# создаем объекты пользователей
user1 = User(id=1, first_name='John', last_name='Doe', username='johndoe', is_bot=False)
user2 = User(id=2, first_name='Jane', last_name='Doe', username='janedoe', is_bot=False)

# создаем объект чата
chat = Chat(id=1, type='group', title='Test Group', username='testgroup')

message = telebot.types.Message(
    message_id=1234,
    from_user=User(),
    date=datetime.now(),
    chat=Chat(),
    content_type='text',
    options=None,
    json_string='{}'
)


message.new_chat_members = [user1, user2]


def test_welcome_new_members():
    message = telebot.types.Message()
    bot = telebot.TeleBot('6033566707:AAGlhH-BNrL0MQVQ26eM859SSv--F7k2PJM')  # создаем объект бота
    welcome_message = 'Здравствуйте🤝\n\n' \
                      '👩‍💼Благодарю за подписку на мой канал @makarova_biz.\n\n' \
                      '👉Вы хотите сделать из своей идеи прибыльный бизнес?\n' \
                      'Если да, то я вам помогу.\n\n' \
                      '✅Новым подписчикам я дарю бесплатную сессию по\n' \
                      '🔻 Стратегии развития вашего бизнеса\n' \
                      '🔻 Масштабированию вашего бизнеса\n' \
                      '🔻 Управлением вашим бизнесом\n\n' \
                      'Нажми да и по ссылке выбери удобное время.'
    expected_markup = telebot.types.InlineKeyboardMarkup()
    expected_markup.add(telebot.types.InlineKeyboardButton(text='Да', url='https://2meetup.in/box-makarova/meet'))

    # Отправляем сообщение в чат
    bot_response = bot.send_message(message.chat.id, welcome_message, reply_markup=expected_markup)

    # Проверяем наличие сообщения в чате
    messages = bot.get_chat_messages(message.chat.id)
    assert len(messages) > 0

    # Проверяем корректность текста сообщения
    assert messages[-1].text == welcome_message

    # Проверяем наличие и корректность inline-клавиатуры
    assert messages[-1].reply_markup.inline_keyboard == expected_markup.inline_keyboard

    assert bot_response.text == welcome_message
    assert bot_response.json['reply_markup']['inline_keyboard'] == expected_markup.to_dict()['inline_keyboard']
