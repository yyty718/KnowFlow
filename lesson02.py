#任务一：成绩等级判断
score = int(input("请输入成绩："))
if score > 100 or score < 0:
    print("成绩输入错误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

#任务二：计算1~100的累加和
total=0
for i in range(1,101):
    total+=i
print(total)

#任务三：KnowFlow登录模拟
correct_username = "admin"
correct_password = "123456"

chance = 0

while chance < 3:
    intname = input("请输入用户名：")
    intpass = input("请输入密码：")

    if intname == correct_username and intpass == correct_password:
        print("登录成功！")
        break
    else:
        chance += 1
        print(f"用户名或密码错误，还剩 {3 - chance} 次机会")

if chance == 3:
    print("尝试次数过多，账号暂时锁定！")
