word = input("入力")
count=0
for boin in word.lower():
    if boin in "aiueo":
        count+=1
print("出力:母音数:",count,"回")
