from kdimb_bot.core import bot
from kdimb_bot.questions.questcore import poll_manager, build_keyboard

def register_handlers():
    
    @bot.message_handler(commands=['question'])
    def cmd_question(message):
        start_quiz(message.chat.id, message.from_user.id,
                   message.from_user.first_name, message.chat.type)
        
    @bot.message_handler(func=lambda m: m.text and m.text.lower().strip() == 'кики')
    def kiki_trigger(message):
        start_quiz(message.chat.id, message.from_user.id,
                   message.from_user.first_name, message.chat.type)
        
    def start_quiz(chat_id: int, user_id: int, user_name: str, chat_type: str):
        print(f"[QUIZ] Запрос от {user_name} в чате {chat_id} (тип: {chat_type})")
        
        question = poll_manager.get_question_giver(strategy="quiz").give()
        
        sent_msg = bot.send_message(
            chat_id,
            f"{question.text}",
            reply_markup=build_keyboard(question, prefix='qz')
        )
        
        poll_manager.create_poll(
            chat_id = chat_id,
            user_id = user_id,
            user_name = user_name,
            message_id = sent_msg.message_id,
            strategy = "quiz",
            on_timeout=lambda cid, uid, uname, msgid: timeout_quiz(cid, uid, uname, msgid)
        )
        
    @bot.callback_query_handler(func=lambda call: call.data.startswith("qz_"))
    def handle_quiz_answer(call):
        is_correct, poll = poll_manager.check_answer(
            call.message.chat.id,
            call.from_user.id,
            int(call.data.split("_")[2])
        )
        
        if not poll:
            bot.answer_callback_query(call.id, "Вопрос уже не актуален")
            return
        
        poll_manager.remove_poll(call.message.chat.id, call.from_user.id)
        
        if is_correct:
            msg_giver = poll_manager.get_message_giver("quiz")
            right_msg = msg_giver.give_right(call.from_user.first_name)
            bot.edit_message_text(
                f"{right_msg}",
                call.message.chat.id,
                call.message.message_id
            )
            print(f"[QUIZ] {call.from_user.first_name} ответил правильно")
            
        else:
            correct_text = poll.question.options[poll.question.correct_option_id]
            msg_giver = poll_manager.get_message_giver("quiz")
            wrong_msg = msg_giver.give_wrong(call.from_user.first_name)
            
            bot.edit_message_text(
                f"{wrong_msg}\n\n Правильный ответ: *{correct_text}*",
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown'
            )
            print(f"[QUIZ] {call.from_user.first_name} ошибся (правильно: {correct_text})")
            
    def timeout_quiz(chat_id: int, user_id: int, user_name: str, message_id: int):
        msg_giver = poll_manager.get_message_giver("quiz")
        timeout_msg = msg_giver.give_timeout(user_name)
        
        try:
            bot.edit_message_text(
                f"{timeout_msg}",
                chat_id,
                message_id
            )
            print(f"[QUIZ] Таймаут для {user_name}")
        except Exception as e:
            print(f"[QUIZ] Ошибка таймаута: {e}")
