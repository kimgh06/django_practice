from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as mysql
import json

db = mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd='1234',
    database="django_p"
)

def selectAll():
    cur = db.cursor()
    query = '''select * from asdf1'''
    cur.execute(query)
    result = cur.fetchall()
    print(dict(result))

    return json.dumps(dict(result))

def index(request):
    result= selectAll()
    return HttpResponse(result)