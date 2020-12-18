from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Mirka',
    logic_adapters=[
        'chatterbot.logic.BestMatch']
)

trainer = ListTrainer(bot)
trainer.train([
    'The prediction is.....',
])

print("Welcome to the Bot Service!")
name = input("Mirka: What's your name? ")
an = input('Mirka: Please enter your age, gender, weight and height\n' + name + ': ').split(' ')

user = {}
features = ['age', 'gender', 'weight', 'height']
user['name'] = name

for i in range(len(an)):
    user[features[i]] = an[i]


while True:
    request = input('Mirka: Do you want a prediction?\n '+ name + ': ');
    if request == 'No' or request == 'no':
        print('Mirka: Ok, bye')
        break

    else:
        response = bot.get_response(request)
        print('Mirka: ',response)
