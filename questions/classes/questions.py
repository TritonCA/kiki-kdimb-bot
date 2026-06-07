from dataclasses import dataclass, field
import random

@dataclass
class Question:
    text: str
    correct_option_id: int | list[int]
    options: list[str] = field(default_factory=list)
    
    def check(self, answer_id: int) -> bool:
        if type(self.correct_option_id) == list:
            return answer_id in self.correct_option_id
        return self.correct_option_id == answer_id
    
    @property
    def keyboard_data(self) -> list[tuple[str, int]]:
        return [(opt, i) for i, opt in enumerate(self.options)]

@dataclass
class QuestionSet:
    questions: list[Question]

@dataclass
class QuestionGiver:
    questionset: QuestionSet
    
    def give(self) -> Question:
        return random.choice(self.questionset.questions)