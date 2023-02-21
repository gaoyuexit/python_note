from django.db import models

# Create your models here.

"""
1。定义模型类 
2。模型迁移 
    2.1: 生成成迁移文件(不会在数据库中生成表, 只会创建一个数据表和模型的对应关系)
        2.1.1: 先在settings.py的INSTALLED_APPS中注册该App ("book.apps.BookConfig")
        2.1.2: 执行python manage.py makemigrations, 生成0001_initial.py
    2.2: 再迁移(会在数据库中生成表)
        迁移: 执行python manage.py migrate
3。操作數据库 

在哪里定义模型 models.py
模型继承自谁就可以 models.Model
ORM对应的关系
    表--＞类 
    宇段--＞属性
    
    sql> create table t_book(id int primary key, nane varchar(10) ->) charset utf8;
    
    图书: 书名
    人物: 名称, 性别, 外键(图书)
    
    图书:
        西游记: 孙悟空(男), 如来(男)
        水浒传: 花荣(男), 孙二娘(女)
"""


class BookInfo(models.Model):
    """
    这个类就是t_book表
    1: 主键, 当前会自动生成
    2: 属性复制过来就可以
    """
    name = models.CharField(max_length=10)


class PeopleInfo(models.Model):

    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


