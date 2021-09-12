words = []
with open('줄임말1.txt','r', encoding='utf-8') as f:
    info = f.readlines()
    for i in info:
        if i[0] =='[':
            words.append([i])
        else:
            words[-1].append(i)

for w in words:
    print(w)

