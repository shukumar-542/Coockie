from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def setcookie(request):
     respone = render(request,'student/setcookie.html')
     respone.set_cookie('name','shukumar',expires=datetime.utcnow()+timedelta(days=2))
     return respone
def getcookie(request):
      # name = request.COOKIES['name']
      name= request.COOKIES.get('name')
      return render (request, 'student/getcookie.html',{'name':name})

def delcookie(request):
      respone = render(request,'student/delcookie.html')
      respone.delete_cookie('name')
      return respone
