from pathlib import Path

size = 0
for item in Path(r'C:\Windows').glob('*'):
    if item.is_file():
        size += item.stat().st_size

print(f"{size/1024/1024:.2f} MiB")