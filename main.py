from utils import email_sender

def main():
    try:
        email_sender.send_email(
            recipients=["levaebalzugan@ukr.net", "chipstop2505@gmail.com"],
            mail_body="Хилел",
            mail_subject="Привіт, це дз!",
            attachment='imag1212e.png',
    )
        print(f"Email отправлен {+1} раз(а)")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()