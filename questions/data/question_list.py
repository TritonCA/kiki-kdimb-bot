from questions.classes.questions import Question, QuestionSet, QuestionGiver

ANTISPAM_QUESTIONS = QuestionSet([
    Question(
        "Кто сгинул в тумана молоке в одном белье?",
        correct_option_id=3,
        options=["Таня", "Саша", "Сью", "Кики"]
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
        "В самых чёрных буднях",
        correct_option_id=2,
        options=["Я твоя погибель", "Я твоё светило", "Я твой верный спутник", "Я твоё отражение"]
    ),
    Question(
        "Бесполезно, как и прежде",
        correct_option_id=1,
        options=["Губить свою юность", "Прятать снежный ком", "Искать Кики", "Бить хлесткую плитку"]
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
    Question(
        "Музыкальная секта",
        correct_option_id=0,
        options=["Никогда не спит", "Погибала от любви", "Растворялась в дожде", "Спрятала снежный ком"]
    ),
    Question(
        "Кто тебя держит?",
        correct_option_id=0,
        options=["Никто!", "Лариса", "Ханна", "Таня, Саша и Сью"]
    ),
    Question(
        "В самых чёрных буднях",
        correct_option_id=2,
        options=["Я твоя погибель", "Я твоё светило", "Я твой верный спутник", "Я твоё отражение"]
    ),
    Question(
        "Бесполезно, как и прежде",
        correct_option_id=1,
        options=["Губить свою юность", "Прятать снежный ком", "Искать Кики", "Бить хлесткую плитку"]
    ),
])


antispam_question_giver = QuestionGiver(ANTISPAM_QUESTIONS)
quiz_question_giver = QuestionGiver(QUIZ_QUESTIONS)
