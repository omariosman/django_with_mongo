from django.shortcuts import render
from .models import Program, Instruction
# Create your views here.
import pymongo
import xml.etree.ElementTree as ET
#connect to server (localhost)


import os
def program(request):
    module_dir = os.path.dirname(__file__)
    print(module_dir)
    #write your logic here
    client = pymongo.MongoClient("localhost:27017")
    #database name
    db = client["Employee_XML"]
    #collection name
    mycol = db["employees"]
    tree = ET.parse('E:/blnk/django_with_mongo/program/employees.xml')
    stud = tree.findall('employee')
    for ep in stud:
        firstname = ep.find('firstname').text
        lastname = ep.find('lastname').text
        stu_dict = [{'firstname': firstname, 'lastname': lastname}]
        try:
            mycol.insert(stu_dict)
        except Exception as e:
            print(e)


    instructions = Instruction.objects.get(var='x')
    input_eval = instructions.inst

    doc = eval(input_eval)
    for y in doc:   
        print(y['lastname'])
    
    """
    myquery = { "firstname": "Jane" }
    for y in mycol.find({ "firstname": "Jane" }):
        print(y['lastname'])
    """


    context = {}
    return render(request, "program.html", context)
