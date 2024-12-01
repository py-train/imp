from django.shortcuts import render, HttpResponse
from .models import Tips

# Create your views here.
def hello(req):
    return HttpResponse("<h1>hello, world!</h1>")

def tips(req):
    data = list(Tips.objects.all())
    # for item in data:
    #     print(item.total_bill)
    # item = next(data)
    return render(req, "tabletmp.html",
                  {
                      'cols': 'TotalBill Tip Sex Smoker Day Time Size'.split(),
                      'data': data
                  }
                  )