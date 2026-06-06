import threading

from typing import Optional, Callable
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from dataclasses import dataclass, field

from questions.classes.questions import Question, QuestionGiver
from questions.classes.messages import MessageGiver
from questions.data.question_list import antispam_question_giver, quiz_question_giver
from questions.data.message_list import antispam_message_giver, quiz_message_giver

TIMER_SEC = 60.0

def build_keyboard(question, prefix: str = "q", row_count: int = 1) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width = row_count)
    buttons = [
        InlineKeyboardButton(
            text,
            callback_data=f"{prefix}_{answer_id}"
        )
        for text, answer_id in question.keyboard_data
    ]
    kb.add(*buttons)
    return kb


@dataclass
class Poll:
    question: Question
    chat_id: int
    user_id: int
    user_name: str
    message_id: int
    timer: Optional[threading.Timer] = None
    strategy: str = "antispam" # 'antispam' или 'quiz'
    
class PollManager:
    def __init__(self):
        self._question_givers = {
            'antispam': antispam_question_giver,
            'quiz': quiz_question_giver
        }
        self._message_givers = {
            'antispam': antispam_message_giver,
            'quiz': quiz_message_giver
        }
        
        self._polls: dict[tuple[int, int], Poll] = {} # {(chat_id, user_id): Poll}
        
    def get_question_giver(self, strategy: str) -> QuestionGiver:
        return self._question_givers.get(strategy, self._question_givers['antispam'])
    
    def get_message_giver(self, strategy: str) -> MessageGiver:
        return self._message_givers.get(strategy, self._message_givers['antispam'])    
    
    def create_poll(self, chat_id: int, user_id: int, user_name: str,
                    message_id: int, question: Question, strategy: str = "antispam",
                    on_timeout: Optional[Callable] = None) -> Poll:
        self.remove_poll(chat_id, user_id)
        
        poll = Poll(
            question = question,
            chat_id = chat_id,
            user_id = user_id,
            user_name = user_name,
            message_id = message_id,
            strategy = strategy
        )
        
        timer = threading.Timer(TIMER_SEC, self._timeout_callback, [chat_id, user_id, user_name, message_id, on_timeout])
        timer.daemon = True
        timer.start()
        poll.timer = timer
        
        self._polls[(chat_id, user_id)] = poll
        return poll
    
    def get_poll(self, chat_id: int, user_id: int) -> Optional[Poll]:
        return self._polls.get((chat_id, user_id))
    
    def remove_poll(self, chat_id: int, user_id: int) -> bool:
        poll = self._polls.get((chat_id, user_id))
        if poll and poll.timer:
            poll.timer.cancel()
        return self._polls.pop((chat_id, user_id), None) is not None
    
    def check_answer(self, chat_id: int, user_id: int, answer_id: int) -> tuple[bool, Optional[Poll]]:
        poll = self.get_poll(chat_id, user_id)
        if not poll:
            return False, None
        
        is_correct = poll.question.check(answer_id)
        return is_correct, poll
    
    def _timeout_callback(self, chat_id: int, user_id: int, user_name: str, message_id: int, on_timeout: Callable):
        poll = self.get_poll(chat_id, user_id)
        if not poll:
            return
        self.remove_poll(chat_id, user_id)
        if on_timeout:
            on_timeout(chat_id, user_id, user_name, message_id)
        
    def get_active_count(self) -> int:
        return len(self._polls)
    
poll_manager = PollManager()
