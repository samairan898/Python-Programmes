import random
when = ['A few years ago', 'Yesterday', 'Last night', 'On 17th may']
who = [' a rabbit', ' a snake', ' a rat', ' an iguana']
name = ['Daniel', 'samaira', 'Cleo', 'Emma', 'Katherine']
residence = ['Oslo', 'Vienna', 'Peru', 'Cambodia']
went = ['theatre', 'univeristy', 'Amusement Park']
happened = ['Eats an apple.', 'made alot of new friends.', 'Travelled to many countries.', 'Found a secret pirate ship.']
print(random.choice(when) + ',' + random.choice(who) + ' that lived in '  + random.choice(residence) + ' went to the ' + random.choice(went) + ' and ' + random.choice(happened))