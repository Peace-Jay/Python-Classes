system_username = 'Admin'
system_password = '123456'

username = input('请输入用户名 Enter System Username：')


if username == system_username:
    password = input('请输入密码 Enter System Password：')
    if password == system_password:
        print('登录成功 Login Success')
    else:
        print('密码错误 Invalid Details')
else:
    pass