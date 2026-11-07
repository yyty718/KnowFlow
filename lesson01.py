
# KnowFlow - Python Lesson 01

print("===== KnowFlow 用户信息登记 =====")

# 1. 获取用户信息
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
email = input("请输入你的邮箱：")
height = float(input("请输入你的身高（单位：cm）："))

# 2. 定义项目信息
project_name = "KnowFlow"
version = 1.0
is_learning = True

# 3. 输出用户信息
print("\n===== 登记结果 =====")
print(f"用户姓名：{name}")
print(f"用户年龄：{age}")
print(f"明年年龄：{age + 1}")
print(f"用户邮箱：{email}")
print(f"用户身高：{height/100:.2f}米")

# 4. 输出项目信息
print(f"项目名称：{project_name}")
print(f"项目版本：{version}")
print(f"是否正在开发：{is_learning}")

print("\n登记完成！")

