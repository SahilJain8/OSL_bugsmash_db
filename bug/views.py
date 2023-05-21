from django.shortcuts import render
from django.http import HttpResponse
from .models import person
import pymysql
from .forms import db_form
# Create your views here.

data = person.objects.all()

def index(request):
    context = {
        'model_data': data,
    }

    
    return render(request, 'index.html', context)


def conn_db(request):
    connection = pymysql.connect(
    host='db-mysql-blr1-69476-do-user-14046288-0.b.db.ondigitalocean.com',
    user='doadmin',
    password='AVNS_YijafuhF4slggX8rKO7',
    database='bugsmash',
    port=25060
)

    if connection:
        return HttpResponse('The server did not connect')



def select(request):
    if request.method == "POST":
        form = db_form(request.POST)
        if form.is_valid():
            column_name = form.cleaned_data['column_name']
            print(column_name)
            field_values = person.objects.values(column_name)
            print(field_values[0])
            return render(request, 'db_form.html', {'field_values': field_values,'col':column_name})

      
    else:
        form = db_form()
    return render(request, "db_form.html", {'form': form})

