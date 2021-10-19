import os
import re
from collections import Counter

with open(os.path.join(os.path.expanduser('~'), '.zsh_history')) as f:
    history = f.readlines()

command_count = Counter()

for line in history:
    m = re.search(';(.*$)', line)
    try:
        command = m.group(1).split(' ')[0]
        command_count[command] += 1
    except:
        pass

for k, v in reversed(sorted(command_count.items(), key=lambda pair: pair[1])):
    print(f'{k} {v}')
