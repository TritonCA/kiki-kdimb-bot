from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from core import bot, get_context
from questions.questcore import poll_manager, build_keyboard

def register_handlers():
    
    @bot.message_handler(content_types=['new_chat_members'])
    def welcome(message):
        ctx = get_context(message.chat.id)
        bot_id = ctx['bot_id']
        is_supergroup = ctx['is_supergroup']
        
        for user in message.new_chat_members:
            # Пропуск ботов и себя
            if user.is_bot or user.id == bot_id:
                continue
            
            print(f"[АНТИСПАМ] Новый участник: {user.first_name} (ID: {user.id}) в чате {ctx['title']}")
            
            try:
                # Ограничение прав
                if is_supergroup:
                    bot.restrict_chat_member(
                        message.chat.id,
                        user.id,
                        can_send_messages=False,
                        can_send_media_messages=False,
                        can_send_other_messages=False,
                        can_add_web_page_previews=False
                    )
                    
                # Вопрос
                question = poll_manager.get_question_giver(strategy = "antispam").give()
                
                sent_msg = bot.send_message(
                    message.chat.id,
                    f"{user.first_name}, проверим тебя.\n\n{question.text}",
                    reply_markup=build_keyboard(question, prefix="as")
                )
                
                poll_manager.create_poll(
                    chat_id = message.chat.id,
                    user_id = user.id,
                    user_name = user.first_name,
                    message_id = sent_msg.message_id,
                    question = question,
                    strategy = "antispam",
                    on_timeout = lambda cid, uid, uname, msgid: timeout_user(cid, uid, uname, msgid)
                )
                
            except Exception as e:
                print(f"[АНТИСПАМ] Ошибка при обработке {user.first_name}: {e}")
                if "can't restrict" in str(e):
                    try:
                        bot.kick_chat_member(message.chat.id, user.id)
                        print(f"[АНТИСПАМ] Кикнут из-за невозможности ограничить права: {user.first_name}")
                    except:
                        pass
    
    @bot.callback_query_handler(func=lambda call: call.data.startswith("as_"))
    def handle_answer(call):
        if call.message.chat.type == 'private':
            return
        
        ctx = get_context(call.message.chat.id)
        is_supergroup = ctx['is_supergroup']
        
        is_correct, poll = poll_manager.check_answer(
            call.message.chat.id,
            call.from_user.id,
            int(call.data.split("_")[1])
        )
        
        if not poll:
            msg_giver = poll_manager.get_message_giver("antispam")
            old_msg = msg_giver.give_old(call.from_user.first_name)
            bot.answer_callback_query(call.id, old_msg)
            return
        
        poll_manager.remove_poll(call.message.chat.id, call.from_user.id)
        
        if is_correct:
            try:
                if is_supergroup:
                    bot.restrict_chat_member(
                        call.message.chat.id,
                        call.from_user.id,
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_add_web_page_previews=True
                    )
                
                msg_giver = poll_manager.get_message_giver("antispam")
                right_msg = msg_giver.give_right(call.from_user.first_name)
                bot.edit_message_text(
                    right_msg,
                    call.message.chat.id,
                    call.message.message_id
                )
                print(f"[АНТИСПАМ] {call.from_user.first_name} прошёл проверку")
            
            except Exception as e:
                print(f"[АНТИСПАМ] Ошибка разблокировки {e}")

        else:
            msg_giver = poll_manager.get_message_giver("antispam")
            wrong_msg = msg_giver.give_wrong(call.from_user.first_name)
            bot.answer_callback_query(call.id, wrong_msg, show_alert=True)
            
            try:
                bot.kick_chat_member(call.message.chat.id, call.from_user.id)
                bot.unban_chat_member(call.message.chat.id, call.from_user.id)
                    
                kick_msg = msg_giver.give_wrong(call.from_user.first_name)
                bot.edit_message_text(
                    kick_msg,
                    call.message.chat.id,
                    call.message.message_id
                )
                print(f"[АНТИСПАМ] {call.from_user.first_name} кикнут за неправильный ответ")
                
            except Exception as e:
                print(f"[АНТИСПАМ] Ошибка кика: {e}")

def timeout_user(chat_id: int, user_id: int, user_name: str, message_id: int):
    msg_giver = poll_manager.get_message_giver("antispam")
    timeout_msg = msg_giver.give_timeout(user_name)
    
    try:
        bot.edit_message_text(
            f"{timeout_msg}",
            chat_id,
            message_id
        )
        bot.kick_chat_member(chat_id, user_id)
        bot.unban_chat_member(chat_id, user_id)
        print(f"[АНТИСПАМ] {user_name} кикнут за таймаут")
    except Exception as e:
        print(f"[АНТИСПАМ] Ошибка таймаута: {e}")