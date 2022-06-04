from django.http import JsonResponse, HttpResponse
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
import json
from user import models
from user.models import User

@csrf_exempt
def inscription(request):
    if request.method == 'POST':
        # create one person
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        email = json_data['email']
        pwd = json_data['pwd']
        ex = getPersonByEmail(email)
        if ex==None:
            try:
                user = User(name=name, age=age, email=email, password=pwd)
                user.save()
                response = {
                    "uid": user.u_id,
                    "name": user.name,
                    "email": user.email,
                    "pwd": user.password
                }
                return JsonResponse(response)
            except Exception as e:
                print(e)
                response = {"error":"error occured while adding user"}
                return JsonResponse(response, safe=False)
        else:
            response = {"error": "User with this email already exists"}
            return JsonResponse(response, safe=False)

    #if request.method =='GET':
     #   response = HttpResponse('Hello World', content_type="text/plain")
      #  return response
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            # create one person
            json_data = json.loads(request.body)
            email = json_data['email']
            pwd = json_data['pwd']
            ex = getPersonByEmail(email)
            #email exists case
            if ex!=None:
                    userPwd = pwdCheck(email,pwd)
                    #email exists and correct pwd
                    if userPwd != None:
                        response = {
                            "uid": userPwd.u_id,
                            "name": userPwd.name,
                            "email": userPwd.email,
                            "pwd": userPwd.password
                        }
                        return JsonResponse(response)
                    #incorrect pwd
                    else:
                        response = {"error": "incorrect password"}
                        return JsonResponse(response, safe=False)
            #email doesn't exist case
            else:
                response = {"error": "there's no user with this email"}
                return JsonResponse(response, safe=False)
        except Exception as e:
            print(e)
            response = {"error": "error occured "}
            return JsonResponse(response, safe=False)


def getPersonByEmail(email):
    try:
        users = User.nodes.all()
        user = User.nodes.get_or_none(email=email)
        return user
    except Exception as e:
        print(e)
        return None

def pwdCheck(email,pwd):
    try:
        users = User.nodes.all()
        user = User.nodes.get_or_none(email=email,password=pwd)
        return user
    except Exception as e:
        print(e)
        return None
@csrf_exempt
def updateUser(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        email = json_data['email']
        pwd = json_data['pwd']
        ex = getPersonByEmail(email)
        # email exists case
        if ex != None:
            ex.name = name
            ex.age = age
            ex.password = pwd
            ex.save()
            response = {
                "uid": ex.u_id,
                "name": ex.name,
                "email": ex.email,
                "pwd": ex.password
            }
            return JsonResponse(response)
        else:
            response = {"error": "an error has occurred, please try again later "}
            return JsonResponse(response, safe=False)
@csrf_exempt
def removeUser(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data['email']
        pwd = json_data['pwd']
        user = pwdCheck(email,pwd)
        if user!=None:
            user.delete()
            response = {"error": "user deleted succefully"}
            return JsonResponse(response, safe=False)
        else:
            response = {"error": "error occurred, user not deleted"}
            return JsonResponse(response, safe=False)



'''@csrf_exempt
def getPersonByEmail(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            email = json_data['email']
            users = User.nodes.all()
            user = User.nodes.get_or_none(email=email)
            print(user)
            response = {"error": "NO HH"}
            return JsonResponse(response, safe=False)
        except Exception as e:
            print(e)
            response = {"error": "error occured while fetching"}
            return JsonResponse(response, safe=False)




        users = User.nodes.filter(email=email)
        try:
            user = users.nodes.get(email=email)
            print("l9ayto")
            return user
        except users.DoesNotExist:
            print("mal9aytoch")
            return None
    except Exception as e:
        print(e)
        return None'''





