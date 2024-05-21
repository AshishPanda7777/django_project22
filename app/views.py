from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse
from app.models import *
from app.forms import  *
def insert_topic(request):
    ETFO=Topicpage()
    d={'ETFO':ETFO}
    

    if request.method == 'POST':
        TFDO = Topicpage(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['tn']
            TO = TOPIC.objects.get_or_create(topic_name=tn)[0]
            return HttpResponse('Data inserted ')
    return render(request, 'insert_topic.html', d)