from core import bot
from questions.questcore import poll_manager, build_keyboard

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
        
        old_poll = poll_manager.get_poll(chat_id, user_id)
        if old_poll:
            try:
                bot.edit_message_text("Вопрос устарел", chat_id, old_poll.message_id)
            except Exception as e:
                print(f"[QUIZ] Ошибка замены: {e}")
            poll_manager.remove_poll(chat_id, user_id)
        
        question = poll_manager.get_question_giver("quiz").give()
        
        sent_msg = bot.send_message(chat_id, question.text, reply_markup=build_keyboard(question, prefix='qz'))
        
        poll_manager.create_poll(
            chat_id = chat_id, 
            user_id = user_id, 
            user_name = user_name, 
            message_id = sent_msg.message_id, 
            question = question, 
            strategy = "quiz", 
            on_timeout = lambda cid, uid, uname, msgid: timeout_quiz(cid, uid, uname, msgid)
        )
        
        
    @bot.callback_query_handler(func=lambda call: call.data.startswith("qz_"))
    def handle_quiz_answer(call):
        
        answer_id = int(call.data.split("_")[1])
        
        is_correct, poll = poll_manager.check_answer(call.message.chat.id, call.from_user.id, answer_id)
        
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
            msg_giver = poll_manager.get_message_giver("quiz")
            wrong_msg = msg_giver.give_wrong(call.from_user.first_name)
            
            correct_options = poll.question.correct_option_id
            if type(correct_options) == list:
                corrects = [poll.question.options[correct] for correct in correct_options]
                correct_text = "\n".join(corrects)
                message_text = f"{wrong_msg}\n\nПравильные ответы:\n{correct_text}"
            elif type(correct_options) == int:
                correct_text = poll.question.options[correct_options]
                message_text = f"{wrong_msg}\n\nПравильный ответ:\n{correct_text}"
            else:
                message_text = f"{wrong_msg}\n\nПравильного ответа не было, я тебя обманула"
            
            bot.edit_message_text(
                f"{message_text}",
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown'
            )
            print(f"[QUIZ] {call.from_user.first_name} ошибся")
            
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