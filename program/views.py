from django.shortcuts import get_object_or_404, redirect, render
from .models import Program, Instruction
# Create your views here.
import pymongo
import xml.etree.ElementTree as ET
#connect to server (localhost)
from django.views.decorators.csrf import csrf_exempt


from django.urls import reverse


from .forms import InstructionForm, ProgramForm, ChooseProgramForm


def base(request):
    context = {}
    return render(request, "base.html", context)





def insert_program(request):
    form = request.POST or None
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/program/type_instruction/')
    else:
        form = ProgramForm()
    
    context = {
        'form': form
    }
    return render(request, "insert_program.html", context)



def type_instruction(request):
    form = request.POST or None
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/program/type_instruction/')
    else:
        form = InstructionForm()
    
    context = {
        'form': form
    }
    return render(request, "type_instruction.html", context)




"""
class ExampleClass(object):
  mycol
  def __init__(self, instance_attr):
    self.instance_attr = instance_attr
"""
import os


#def selectview(request):



@csrf_exempt
def program(request):
    module_dir = os.path.dirname(__file__)
    print(module_dir)
    #write your logic here
    client = pymongo.MongoClient("localhost:27017")
    #database name
    db = client["Employee_XML"]
    #collection name
    mycol = db["employees"]
    print(type(mycol))
    tree = ET.parse('E:/blnk/django_with_mongo/program/employees.xml')
    stud = tree.findall('employee')
    for ep in stud:
        firstname = ep.find('firstname').text
        lastname = ep.find('lastname').text
        room = ep.find('room').text
        stu_dict = [{'firstname': firstname, 'lastname': lastname, 'room': room}]
        try:
            mycol.insert(stu_dict)
        except Exception as e:
            print(e)

    programs  = Program.objects.all() # use filter() when you have sth to filter ;)
    form = request.POST # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
    if request.method == 'POST':
        selected_item = get_object_or_404(Program, pk=request.POST.get('program_id'))
        instructions = selected_item.instruction_set.all()
        for instruction in instructions.iterator():
            input_eval = instruction.inst
            doc = eval(input_eval)
            #doc = eval(input_eval)
            print("before loop")
            for y in doc:   
                print(y["lastname"])
                str = y["lastname"]

    context = {"programs": programs}

    #instructions = Instruction.objects.all()


    #print(loan_estimate)
    #return render_to_response ('select/item.html', {'items':item}, context_instance =  RequestContext(request),)

    return render(request, "program.html", context)



def execute_proram(request):
    instructions = Instruction.objects.get(var='x')
    input_eval = instructions.inst
    doc = eval(input_eval)
    for y in doc:   
        if (y['lastname']) == "Doe":
            loan_estimate = 1000
        else:
            loan_estimate = 5000
    print(loan_estimate)
    context = {}
    return render(request, "execute_proram.html", context)


