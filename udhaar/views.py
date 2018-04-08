from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def index(request):

    return HttpResponse("Welcome to Udhaar App test Center")

def getQuery(request):

    res = "{\"1\":\"select * from data_server\",\"2\":\"select * from data_server where sms_id in (select sms_id from data_server where (key = 'timestamp' and value > '1509474600') or (key = 'timestamp' and value < '1512844200')) order by sms_id\"}"

    return HttpResponse(res)

def queryCallback(request):

    if request.method == 'POST':
        return HttpResponse(request.POST.get("result"))
    return HttpResponse("No Post Data")

def getRulesVersion(request):
    res = "{\"version\":\"1.0.1\"}"
    return HttpResponse(res)

def getRuleFile(request):
    with open(os.path.join(os.path.abspath('')+'/udhaar/files/','rules.json'),'r+') as file:
        response = HttpResponse(file.read())
        response['content_type'] = 'application/json'
        response['Content-Disposition'] = 'attachment;filename=rules.json'
        return response
    return HttpResponse("No file found")


{
    "summary":"data",
    "summary_version":"summary_version_number"
}

[
    {"query_id_1":"query_result"},
    {"query_id_2":"query_result"}
]
