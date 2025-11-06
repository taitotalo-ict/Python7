from pathlib import Path
# print(__file__)
SCRIPT_ROOT = Path(__file__).parent

file = open(SCRIPT_ROOT / 'data.csv', 'r', encoding='utf-8')
data = file.read()
print(data)
file.close()
