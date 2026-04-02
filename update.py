rules = open('rules').read()
readermode = open('readermode').read()

readermode_sites = [
    'text.npr.org',
    'axios.com',
    'en.wikipedia.org',
]

for site in readermode_sites:
    rules += "\n\n" + readermode.replace('example.com', site)

with open("focus", 'w') as f:
    f.write(rules)
