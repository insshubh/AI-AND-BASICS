import telebot
import math

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6402365297:AAE7zKH4qHPBzO_p6ufju54FyI6K1l0dbd0')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = "Welcome to the Math Bot!\n\n" \
                      "You can send me a number to find its factors, multiples, or check if it's prime."
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: True)
def process_message(message):
    try:
        num = int(message.text)
        factors = [i for i in range(1, num+1) if num % i == 0]
        multiples = [i for i in range(num, num*10+1, num)]
        prime_check = is_prime(num)

        response = f"Factors of {num}: {factors}\n" \
                   f"Multiples of {num}: {multiples}\n" \
                   f"{num} is {'prime' if prime_check else 'not prime'}."

        bot.reply_to(message, response)
    except ValueError:
        bot.reply_to(message, "Please provide a valid integer.")



if __name__ == "__main__":
    bot.polling()
