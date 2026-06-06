from questions.classes.questions import Question, QuestionSet, QuestionGiver

ANTISPAM_QUESTIONS = QuestionSet([
    Question(
        "Кто сгинул в тумана молоке в одном белье?",
        correct_option_id=3,
        options=["Таня", "Саша", "Сью", "Кики"]
    ),
    Question(
        "Что в девичьих руках как знак?",
        correct_option_id=1,
        options=["Ласточка", "Маслёнка", "Хлеб", "Сухой цветок"]
    ),
    Question(
        "У кого в спальне попугаи, в кухне серпентаи, а в душе крокодил?",
        correct_option_id=2,
        options=["У Кики", "У Саши Фроловой", "У Ханны", "У Ларисы"]
    ),
    Question(
        "Когда в нас наделали дыр",
        correct_option_id=3,
        options=["Едва отец ушёл к другой", "В день, когда ты умерла", "Утром солнечного дня", "Ещё до рождения"]
    ),
    Question(
        "Когда странно немеет сердце",
        correct_option_id=1,
        options=["С февраля", "В последнее лето детства", "В последнюю летнюю ночь", "Завтра"]
    ),
])
QUIZ_QUESTIONS = QuestionSet([
    Question(
        "Кто сгинул в тумана молоке в одном белье?",
        correct_option_id=3,
        options=["Таня", "Саша", "Сью", "Кики"]
    ),
    Question(
        "Что в девичьих руках как знак?",
        correct_option_id=1,
        options=["Ласточка", "Маслёнка", "Хлеб", "Сухой цветок"]
    ),
    Question(
        "У кого в спальне попугаи, в кухне серпентаи, а в душе крокодил?",
        correct_option_id=2,
        options=["У Кики", "У Саши Фроловой", "У Ханны", "У Ларисы"]
    ),
    Question(
        "Когда в нас наделали дыр",
        correct_option_id=3,
        options=["Едва отец ушёл к другой", "В день, когда ты умерла", "Утром солнечного дня", "Ещё до рождения"]
    ),
    Question(
        "Когда странно немеет сердце",
        correct_option_id=1,
        options=["С февраля", "В последнее лето детства", "В последнюю летнюю ночь", "Завтра"]
    ),
])


antispam_question_giver = QuestionGiver(ANTISPAM_QUESTIONS)
quiz_question_giver = QuestionGiver(QUIZ_QUESTIONS)