from questions.classes.messages import Message, MessageSet, MessageGiver

ANTISPAM_MESSAGES = MessageSet(
    right_messages = [
        Message("{name}, конечно, будет рядом"),
        Message("{name} хочет остаться там, где оказался"),
        Message("{name} делал всё так, как они говорят"),
        Message("{name} будет пытаться согреться и полюбить это место"),
        Message("{name}, а в группе холод без тебя"),
        Message("{name} попал к нам на скамью"),
        Message("{name}, волшебная Лариса собирает людей"),
        Message("{name}, мы славим небеса, с такими как ты"),
        Message("{name}, глубже забирайся в толпу"),
        Message("С {name} встреча неизбежна"),
        Message("Только {name} знает тропы, как меня отыскать"),
        Message("{name} в лиге хмурых взрослых"),
    ],

    timeout_messages = [
        Message("{name}, твоё положение тебя не спасло"),
        Message("{name}! Ты не можешь просто стоять на этой вечеринке!"),
        Message("{name} слишком давно стоит вот так"),
        Message("Вещи собраны, но {name} опоздал"),
        Message("Здравствуй город, прости, {name} не говорит"),
        Message("{name} - дурак, он не пробовал олова"),
        Message("Для {name} вокруг одни незнакомцы"),
        Message("{name} уснул в лесу, очнулся тут"),
        Message("{name} тут всё неизвестно, {name} не хочет в это место"),
        Message("{name} не любит сомневаться"),
        Message("{name} решил остановить голову, но и сердце не включать"),
        Message("{name} не ответил, решил отказаться, но это парные танцы"),
        Message("Страшно признаться, что {name} для меня только сон"),
        Message("Сегодня {name} прикинулся мрачным"),
        Message("{name}, я так люблю и ненавижу вас"),
        Message("Стой на ногах, тихий {name}"),
        Message("Когда {name} пуста, спасайся, сестра"),
        Message("{name} бросил наш приход и уехал в Помпеи"),
        Message("Для {name}, видимо, невидимым стать самое то"),
        Message("{name}, ну что ты молчишь"),
        Message("{name} прилёг на час, а спит три дня"),
        Message("{name} струсил дёрнуть за курок"),
        Message("{name} укололся веретеном"),
        Message("{name} боится людей"),
        Message("{name} что застыл, что за стыд?"),
    ],

    wrong_messages = [
        Message("Как жаль, что {name} ушёл, вам было хорошо"),
        Message("{name} не нашёл себя здесь"),
        Message("Но этот дом - не дом {name}"),
        Message("{name} выгнан. В моей большой песочнице нет места никому"),
        Message("{name} ошибся и удалён. Удачи легко, неудачи сложно"),
        Message("Нет, не пущу {name} в солнечный город"),
        Message("{name} с пустой головой, в пустой кабинет"),
        Message("Наверное, {name} ненужный друг"),
        Message("Мне кажется, {name} всё. У нас с тобою всё"),
        Message("{name} теперь уже один будет слушать Аквариум"),
        Message("{name}, я тебя увидела, и меня понесло"),
        Message("{name} ничего не понимает. Его нетрудно победить"),
        Message("Я хотела бы быть с {name}, но он дикий"),
        Message("{name}, не повезло, тебе не повезло"),
        Message("У {name} всё, что может провалиться - проваливается"),
        Message("{name}, уезжай, я останусь здесь до конца"),
        Message("{name}, танцуй и кайся"),
        Message("{name}, играет в кого-то другого"),
        Message("Мы встречаемся с {name} лишь в моём счастливом сне"),
        Message("Но быть с {name} вместе мне снова нельзя"),
        Message("{name}, тут каждой твари по паре, но ты не такой"),
        Message("{name} из тысячи ответов, выбрал тот, что ни при чём"),
    ],

    old_callback_messages= [
        Message("Только что-то не случилось, не произошло"),
        Message("Это всё не спасёт"),
    ]
)

QUIZ_MESSAGES = MessageSet(
    right_messages = [
        Message("Ты ответил правильно!"),
    ],

    timeout_messages = [
        Message("Ты опоздал!"),
    ],

    wrong_messages = [
        Message("Ты ошибся"),
    ],

    old_callback_messages= [
        Message("Опрос уже не актуален"),
    ]
)

antispam_message_giver = MessageGiver(ANTISPAM_MESSAGES)
quiz_message_giver = MessageGiver(QUIZ_MESSAGES)