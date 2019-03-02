import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test#指定数据库
collection=db.students#制定集合
student={
    'id':'20170101',
    'name':'Bob',
    'age':20,
    'gender':'male'
}
result=collection.insert(student)
print(result)
result=collection.find_one({'name':'Bob'})
print(result)