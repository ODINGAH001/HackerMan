#python3

import re
for _ in range(int(input())):
    if re.match(r"^[-+]?[0-9]*\.+[0-9]+\Z", input()):
        print(True)
    else:
        print(False)
