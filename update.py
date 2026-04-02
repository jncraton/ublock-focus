rules_text = open("rules").read()
readermode = open("readermode").read()

readermode_sites = [
    'axios.com',
    'cnn.com',
    'edu',
]

for site in readermode_sites:
    rules_text += "\n\n" + readermode.replace("example.com", site)

# strip blank lines and comment lines beginning with !
filtered_lines = []
for line in rules_text.splitlines():
    s = line.strip()
    if not s:
        continue
    if s.startswith("!"):
        continue
    filtered_lines.append(line)

output = "\n".join(filtered_lines) + "\n"

with open("focus", "w") as f:
    f.write(output)
