daria = ['Daria', '24', 'junior developer', '2']

print('Hi, my name is {}'.format(daria[0]))
print('I am {} years old'.format(daria[1]))
print('I am writing to express my interest in the position of {}'.format(daria[2]))
print("I'm living in israel for {} years and looking IT job for the past two years".format(daria[3]))

languages = [
    ['Python', 1],
    ['JavaScrypt', 0.5],
    ['html + css', 1],
    ['MySQL', 1]
    ]
languages.sort(key=lambda row: row[1], reverse=True)
print('My personal experience:')
print()
print('Language     | years')
print('____________________')
for row in languages:
    print('{:<12} | {:>4}'.format(row[0], row[1]))
    print('____________________')

personal_qualities = ['hard work', 'high responsibility', 'stress resistance', 'friendliness', 'ability to listen and convince']
for i in personal_qualities:
    print('Personal qualities:')
    print('-', end='')
    print(i, end='')

contacts = [
    ['Phone', 2**2*77093*3153743],
    ['Email', 'dariaresman@gmail.com'],
    ['Telegram', '@bettercalldaria']
]
print('Please, contact me:')
for a in contacts:
    print('{} : {}'. format(a[0], a[1]))
