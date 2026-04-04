def strip(rules):
    # strip blank lines and comment lines beginning with !
    filtered_lines = []
    for line in rules.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("!"):
            continue
        filtered_lines.append(line)

    return "\n".join(filtered_lines) + "\n"

rules = open("rules").read()
readermode = open("readermode").read()

readermode_sites = [
    'axios.com',
    'cnn.com',
    'news.ycombinator.com',
    'edu',
]

focus = rules

for site in readermode_sites:
    focus += "\n\n" + readermode.replace("example.com", site)

with open("focus", "w") as f:
    f.write(strip(focus))
