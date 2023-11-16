import requests
import sqlite3

if __name__ == "__main__":
    path = input("输入数据库文件路径: ").strip("\"")
    connection = sqlite3.connect(path)
    result = connection.execute("select sid, cid from StudentNet order by sid asc")
    # 获取参数
    params = requests.get("http://www.msftconnecttest.com/redirect").url.split("?")[1]
    # 检查参数
    if ("wlanuserip" not in params):
        input("请检查当前网络, 可能处于以下状态:\n1. 目前在线\n2. 非校园网wifi\n\n按任意键结束...")
        exit()
    # 尝试登录
    for row in result:
        post_data = {
            "loginName": row[0],
            "loginPwd": row[1],
            "queryString": params,
            "vmode": "1"
        }
        rep = requests.post("http://10.254.0.42:8081/ibillingportal/LoginAction_login.do", data=post_data).json()        
        print(rep["respMsg"] + f"\n账号:{row[0]}\n密码:{row[1]}\n")
        connection.execute(f"update StudentNet set status = '{rep["respMsg"]}' where sid = '{row[0]}'")
        connection.commit()
        if (rep["respCode"] == "0"):
            break