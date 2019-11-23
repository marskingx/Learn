#讀取檔案
data = []
with open('food.txt', 'r') as f:
    for line in f:
        print(line.strip())
        data.append(line.strip())
print(data)

