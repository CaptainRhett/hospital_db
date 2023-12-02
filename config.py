Dialect = 'mysql'
Driver = 'pymysql'
Username = 'root'
Password = 'Bit1010!'
Host = 'localhost'
Port = '3306'
Database = 'myhospital'
SqlchemyDatabaseUri = f"{Dialect}+{Driver}://{Username}:{Password}@{Host}:{Port}/{Database}?charset=utf8"
SqlchemyTrackModifications = True
SqlchemyEcho = True
SecretKey = "random string"
AllowedExtensions = set(['png','jpg','PNG','JPG','bmp'])
TotalDepartmentNum = 4