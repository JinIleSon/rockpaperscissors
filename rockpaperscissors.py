import random

com = ['가위', '바위', '보']
me = input('낼 것을 고르세요.\n')
if me == '가위':
    if random.sample(com, 1) == '가위':
        print('컴퓨터는 가위를 냈습니다. 비겼습니다.')
    elif random.sample(com, 1) == '바위':
        print('컴퓨터는 바위를 냈습니다. 졌습니다.')
    else:
        print('컴퓨터는 보를 냈습니다. 이겼습니다.')
elif me == '바위':
    if random.sample(com, 1) == '가위':
        print('컴퓨터는 가위를 냈습니다. 이겼습니다.')
    elif random.sample(com, 1) == '바위':
        print('컴퓨터는 바위를 냈습니다. 비겼습니다.')
    else:
        print('컴퓨터는 보를 냈습니다. 졌습니다.')
elif me == '보':
    if random.sample(com, 1) == '가위':
        print('컴퓨터는 가위를 냈습니다. 졌습니다.')
    elif random.sample(com, 1) == '바위':
        print('컴퓨터는 바위를 냈습니다. 이겼습니다.')
    else:
        print('컴퓨터는 보를 냈습니다. 비겼습니다.')
else:
    print('잘못 입력하였습니다.')
