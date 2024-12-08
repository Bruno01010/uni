def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    # Проверяем корректность email-адресов
    if ("@" not in sender or not sender.endswith(".com") and 
        not sender.endswith(".ru") and not sender.endswith(".net")) or (
            "@" not in recipient or not recipient.endswith(".com") and 
            not recipient.endswith(".ru") and not recipient.endswith(".net")
       ):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре", "urban.info@gmail.com", sender="urban.info@gmail.com")