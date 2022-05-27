import re

import sys

src =sys.argv[1]

pattern = re.compile('.{2}')

print('0x'+', 0x'.join(pattern.findall(src)))