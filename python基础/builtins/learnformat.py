days = 3
seconds = 1800

# 02d 代表两位数字，不足补零
hours = f'{((24 * days) + (seconds // 3600)):02d}'
minutes = f'{((seconds % 3600) // 60):02d}'
seconds = f'{(seconds % 60):02d}'
# 72:30:00
print(f'{hours}:{minutes}:{seconds}')