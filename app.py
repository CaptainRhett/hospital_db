from flask import Flask,request, redirect, flash, url_for, render_template, session
from sqlalchemy import create_engine,text
import config
import pymysql



app = Flask(__name__)
app.config.from_object(config)
engine = create_engine(config.SqlchemyDatabaseUri)

@app.route('/')
def index():
    # if session.get("username"):
    #     return redirect(url_for('home'))
    # else : 
    #     return redirect(url_for('login'))
    return render_template("start.html")

@app.route("/register")
def home():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")
    # 连接数据库
    # connection = pymysql.connect(
    #     host=config.Host,
    #     user=config.Username,
    #     password=config.Password,
    #     database=config.Database,
    #     port=3306,  # 可选，默认为 3306
    #     charset='utf8mb4',  # 可选，指定字符集
    #     )
    # try:
    #     with connection.cursor() as Cursor:
    #         sql = "show tables;"
    #         Cursor.execute(sql)
    #         result = Cursor.fetchall()
    # finally:
    #     connection.close()
    # return str(result)
    with engine.connect() as conn:
        res = conn.execute("show tables;").all()
    return str(res)

@app.route("/register")
def register(engine):
    connection = pymysql.connect(
        host=config.Host,
        user=config.Username,
        password=config.Password,
        database=config.Database,
        port=3306,  # 可选，默认为 3306
        charset='utf8mb4',  # 可选，指定字符集
        )
    Cursor = connection.cursor()
    input_username = str(request.form.get('username'))
    input_password = str(request.form.get('password'))
    input_name = str(request.form.get('name'))
    input_id = str(request.form.get('id'))
    # print("\n\n\n\n"+str(request.form.get('username')))
    # sql = f"select id , name from Doctors where id = {input_password};"
    sql = f"insert into Doctors(id,name,username,pasword) values({input_id},'{input_name}','{input_username}',{input_password});"
    # print("\n\n\n\n\n\n\n\n\n\n"+sql)
    Cursor.execute(sql)
    connection.commit()
    # result = Cursor.fetchall()
    # print(input_password)
    # print(type(input_password))
    # return str(result[0][0])+result[0][1]
    return sql
# @app.route("/register",methods=["POST"])
# register(engine)
# test()
if __name__=='__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
