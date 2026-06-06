from dataclasses import dataclass, field
import random

@dataclass
class Message:
    text: str
    
    def insert(self, user_name: str = "") -> str:
        return self.text.format(name=user_name)

@dataclass
class MessageSet:
    right_messages: list[Message]
    wrong_messages: list[Message]
    timeout_messages: list[Message]
    old_callback_messages: list[Message]

@dataclass
class MessageGiver:
    messageset: MessageSet
    
    def give_right(self, user_name: str = "") -> str:
        return random.choice(self.messageset.right_messages).insert(user_name)
    
    def give_wrong(self, user_name: str = "") -> str:
        return random.choice(self.messageset.wrong_messages).insert(user_name)
    
    def give_timeout(self, user_name: str = "") -> str:
        return random.choice(self.messageset.timeout_messages).insert(user_name)
    
    def give_old(self, user_name: str = "") -> str:
        return random.choice(self.messageset.old_callback_messages).insert(user_name)