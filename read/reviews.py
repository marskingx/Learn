#分析留言

data = []
count = 0
with open('/Users/shama/PycharmProjects/file/reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count +1
        if count % 1000000 == 0:
            print(len(data))

print(data[0])
print('------------------')
print((data[1]))
print('檔案讀完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)
print('平均是',sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆留言小於100個單字")