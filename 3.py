def is_palindrome(s):
    return s ==s[::-1]
word = input("文字列を入力してください")
if is_palindrome(word):
    print("回文です")
else:
    print("回文ではありません")
