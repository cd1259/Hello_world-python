money = float(input('请输入金额>'))
answer = input('是否为会员，y/n >')
if answer == 'y':
    print('VIP\n')
    if money >= 200:
        print('应付金额\n', money * 0.8)
    else:
        print('未达到200,应付\n', money)
elif answer == 'n':
    print('应付金额\n', money)
else:
    print('无效选择\n')
