import os
path = os.path.join(os.getcwd() , 'UserInfo')
print(path)
if not os.path.isdir('UserInfo'):
    os.mkdir(os.path.join(os.getcwd(),'UserInfo'))
#path = os.path.join(os.getcwd() , 'UserInfo
if not os.path.isfile(path) :
    with open('books.txt','x', encoding='utf-8') as txtfile:
        pass
    with open('books.txt','w', encoding='utf-8') as txtfile:
        txtfile.write('Петрович насрал в штаны')
        pass
