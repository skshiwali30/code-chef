click_list = []
noOfTweet, noOfClick = map(int, input().split())
open = 0

for j in range(noOfClick):
    word = input()
    if word == 'CLOSEALL':
        open = 0
        click_list = []
    else:
        word = word[6:]
        if word not in click_list:
            open = open + 1
            click_list.append(word)
        else:
            click_list.remove(word)
            open = open - 1
    print(open)