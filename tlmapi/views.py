from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from django.http import HttpResponse
from .models import *
import datetime
from datetime import timedelta 
import pytz 
import requests
import json


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def index(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def line(request, *args, **kw):
    request_data = request.data
    topic = request_data.get('topic', None)
    print (topic)
    print (request_data)
    return Response("SUCCESS", status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def record(request):
    x=transformer2.objects.get(load='9')
    print (x.load)

    request_data = request.data
    # topic = request_data.get('topic', None)
    # print (topic)
    request_data = request.data
    print (request_data)
    deviceid = request_data.get('deviceid', 'pv001')
    grid = request_data.get('grid', 0.0)
    load = request_data.get('load', 0.0)
    solar= request_data.get('solar', 0.0)
    print ((deviceid))
    print (type(grid))
    print (load)
    print (solar)

    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
    thaitime = pst_now.strftime("%Y-%m-%d %H:%M:%S")

    nowsx = datetime.datetime.now()
    add_data = transformer2(pub_date=thaitime, deviceid='deviceid', grid=grid, load=load, solar=solar)
    add_data.save()
    import time
    time.sleep(0.5)
    
    x=transformer2.objects.get(load='9')
    print (x.load)
    
    return Response(x.load)
    return Response("SUCCESS", status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def gettestrecord(request, *args, **kw):


    p=transformer2.objects.all()
    q = (p.values('pub_date','grid','load','solar'))

    return Response(q)

@csrf_exempt
@api_view(["GET"])
def auto_record(request):
    import json 
    response = requests.get(
            url="https://www.aismagellan.io/api/things/pull/22037ed0-72f1-11e9-810a-f990cf998f9d",
            data=json.dumps({})
        )
    responsemsg = response.content
    
    msg = json.loads(responsemsg)

    tempindoor = round(msg['T1'],3)
    tempoutdoor = round(msg['T2'],3)
    powera = round(msg['WA'],3)
    powerb = round(msg['WB'],3)
    powerc = round(msg['WC'],3)
    powertot = round(float(msg['WA']) + float(msg['WB'])+ float(msg['WC']),3)

    reactivepowera = round(msg['VARA'],3)
    reactivepowerb = round(msg['VARB'],3)
    reactivepowerc = round(msg['VARC'],3)
    reactivepowertot = round(msg['VART'],3)
    voltagea = round(msg['VA'],3)
    voltageb = round(msg['VB'],3)
    voltagec = round(msg['VC'],3)
    kwha = round(msg['kwhA'],3)
    kwhb = round(msg['kwhB'],3)
    kwhc = round(msg['kwhC'],3)
    kwhtot = round(msg['kwhtotal'],3)

    print('tempindoor: {content}'.format(content=tempindoor))
    print('powertot: {content}'.format(content=powertot))

    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
    thaidatetime = pst_now.strftime("%Y-%m-%d %H:%M:%S")
    pub_time = pst_now.strftime("%X")
    
    # nowsx = datetime.datetime.now()
    add_data = transformer(pub_date=thaidatetime,pub_time=pub_time, deviceid='TLM_peac3001',tempindoor = tempindoor,tempoutdoor = tempoutdoor,powera = powera,powerb = powerb ,powerc = powerc,powertot = powertot,reactivepowera = reactivepowera,reactivepowerb = reactivepowerb ,reactivepowerc = reactivepowerc ,reactivepowertot = reactivepowertot,voltagea = voltagea ,voltageb = voltageb,voltagec = voltagec,kwha = kwha,kwhb = kwhb,kwhc = kwhc,kwhtot =  kwhtot )
    add_data.save()

    return Response()
    return Response("SUCCESS", status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET","POST"])
def gettlm(request, *args, **kw):

    request_data = request.data
    datestart = request_data.get('datestart')
    dateend = request_data.get('dateend')
    deviceid = request_data.get('deviceid')

    if deviceid== None :
        deviceid = 'TLM_peac3001'

    if datestart== None or dateend == None:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
        thaidatetime = pst_now.date
        start_date = pst_now.date()
        end_date = pst_now.date()+ timedelta(days=1)

    else:

        datestart_date = ((datestart)[0:2])
        datestart_month = ((datestart)[2:4])
        datestart_year = ((datestart)[4:8])

        dateend_date = ((dateend)[0:2])
        dateend_month = ((dateend)[2:4])
        dateend_year = ((dateend)[4:8])

        start_date = datetime.date(int(datestart_year), int(datestart_month), int(datestart_date))
        end_date = (datetime.date(int(dateend_year), int(dateend_month), int(dateend_date)))+ timedelta(days=1)

    p=transformer.objects.filter(pub_date__range=(start_date, end_date),deviceid='TLM_peac3001')
    q = (p.values('pub_date','pub_time','tempindoor','tempoutdoor','powera','powerb','powerc' ,'powertot' ,'reactivepowera','reactivepowera','reactivepowerb' ,'reactivepowerc' ,'reactivepowertot','voltagea' ,'voltageb' ,'voltagec' ,'kwha','kwhb' ,'kwhc','kwhtot'))

    return Response(q)
    
@csrf_exempt
@api_view(["GET","POST"])
def gettlmqtc(request, *args, **kw):

    request_data = request.data
    datestart = request_data.get('datestart')
    dateend = request_data.get('dateend')
    deviceid = request_data.get('deviceid')

    if deviceid== None :
        deviceid = 'TLM_peac3001'

    if datestart== None or dateend == None:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
        thaidatetime = pst_now.date
        start_date = pst_now.date()
        end_date = pst_now.date()+ timedelta(days=1)

    else:

        datestart_date = ((datestart)[0:2])
        datestart_month = ((datestart)[2:4])
        datestart_year = ((datestart)[4:8])

        dateend_date = ((dateend)[0:2])
        dateend_month = ((dateend)[2:4])
        dateend_year = ((dateend)[4:8])

        start_date = datetime.date(int(datestart_year), int(datestart_month), int(datestart_date))
        end_date = (datetime.date(int(dateend_year), int(dateend_month), int(dateend_date)))+ timedelta(days=1)
    q = ''
    //p=transformer.objects.filter(pub_date__range=(start_date, end_date),deviceid='QTC0001')
    //q = (p.values('pub_date','pub_time','tempindoor','tempoutdoor','powera','powerb','powerc' ,'powertot' ,'reactivepowera','reactivepowera','reactivepowerb' ,'reactivepowerc' ,'reactivepowertot','voltagea' ,'voltageb' ,'voltagec' ,'kwha','kwhb' ,'kwhc','kwhtot'))

    return Response(q)



@csrf_exempt
@api_view(["GET","POST"])
def gettlmpci(request, *args, **kw):

    request_data = request.data
    datestart = request_data.get('datestart')
    dateend = request_data.get('dateend')
    deviceid = request_data.get('deviceid')

    if deviceid== None :
        deviceid = 'TLM_peac3001'

    if datestart== None or dateend == None:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
        thaidatetime = pst_now.date
        start_date = pst_now.date()
        end_date = pst_now.date()+ timedelta(days=1)

    else:

        datestart_date = ((datestart)[0:2])
        datestart_month = ((datestart)[2:4])
        datestart_year = ((datestart)[4:8])

        dateend_date = ((dateend)[0:2])
        dateend_month = ((dateend)[2:4])
        dateend_year = ((dateend)[4:8])

        start_date = datetime.date(int(datestart_year), int(datestart_month), int(datestart_date))
        end_date = (datetime.date(int(dateend_year), int(dateend_month), int(dateend_date)))+ timedelta(days=1)
    q = ''
    //p=transformer.objects.filter(pub_date__range=(start_date, end_date),deviceid='PCI0001')
    //q = (p.values('pub_date','pub_time','tempindoor','tempoutdoor','powera','powerb','powerc' ,'powertot' ,'reactivepowera','reactivepowera','reactivepowerb' ,'reactivepowerc' ,'reactivepowertot','voltagea' ,'voltageb' ,'voltagec' ,'kwha','kwhb' ,'kwhc','kwhtot'))

    return Response(q)



@csrf_exempt
@api_view(["GET","POST"])
def gettlmchi(request, *args, **kw):

    request_data = request.data
    datestart = request_data.get('datestart')
    dateend = request_data.get('dateend')
    deviceid = request_data.get('deviceid')

    if deviceid== None :
        deviceid = 'TLM_peac3001'

    if datestart== None or dateend == None:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
        thaidatetime = pst_now.date
        start_date = pst_now.date()
        end_date = pst_now.date()+ timedelta(days=1)

    else:

        datestart_date = ((datestart)[0:2])
        datestart_month = ((datestart)[2:4])
        datestart_year = ((datestart)[4:8])

        dateend_date = ((dateend)[0:2])
        dateend_month = ((dateend)[2:4])
        dateend_year = ((dateend)[4:8])

        start_date = datetime.date(int(datestart_year), int(datestart_month), int(datestart_date))
        end_date = (datetime.date(int(dateend_year), int(dateend_month), int(dateend_date)))+ timedelta(days=1)
    q = ''
    //p=transformer.objects.filter(pub_date__range=(start_date, end_date),deviceid='CHI0001')
    //q = (p.values('pub_date','pub_time','tempindoor','tempoutdoor','powera','powerb','powerc' ,'powertot' ,'reactivepowera','reactivepowera','reactivepowerb' ,'reactivepowerc' ,'reactivepowertot','voltagea' ,'voltageb' ,'voltagec' ,'kwha','kwhb' ,'kwhc','kwhtot'))

    return Response(q)




import pika, os

def callback(ch, method, properties, body):
    # print(" [x] Received " + str(body))
    # from datetime import datetime
    # current date and time
    # dateTimeObj = datetime.now()
    # print("timestamp =", dateTimeObj)

    import json
    
    msg = json.loads(body)

    print((msg))

    # print (msg['deviceId'])

    deviceid = msg['deviceId']
    tempindoor = round(msg['temp_amb'],3)
    tempoutdoor = round(msg['temp_amb'],3)
    powera = round(msg['powera_A'],3)
    powerb = round(msg['powera_B'],3)
    powerc = round(msg['powera_C'],3)
    powertot = round(msg['powera_tot'],3)
    voltagea = round(msg['voltage_A'],3)
    voltageb = round(msg['voltage_B'],3)
    voltagec = round(msg['voltage_C'],3)


    currenta = round(msg['current_A'],3)
    currentb = round(msg['current_B'],3)
    currentc = round(msg['current_C'],3)

    print('tempindoor: {content}'.format(content=tempindoor))
    print('powertot: {content}'.format(content=powertot))

    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
    thaidatetime = pst_now.strftime("%Y-%m-%d %H:%M:%S")
    pub_time = pst_now.strftime("%X")
    
    # nowsx = datetime.datetime.now()
    add_data = transformer(pub_date=thaidatetime,pub_time=pub_time, deviceid=deviceid,tempindoor = tempindoor,tempoutdoor = tempoutdoor,powera = powera,powerb = powerb ,powerc = powerc,powertot = powertot,currenta = currenta,currentb = currentb ,currentc = currentc ,voltagea = voltagea ,voltageb = voltageb,voltagec = voltagec )
    add_data.save()


    print(">>>   >>>>   >>>  >>>   >>>>   >>>  >>>   >>>>   >>> ")


@csrf_exempt
@api_view(["GET"])
def sample_api2(request):
    data = {'sample_data': 123}

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://tcjzxnnl:YxOy4T9CfhUzjHnW7CbPZdkuXizPnXYs@fish.rmq.cloudamqp.com/tcjzxnnl')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel

    print (channel.is_open)
    channel.close()
    print (channel.is_open)
    channel = connection.channel()
    print (channel.is_open)

    channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()


    return Response(data, status=HTTP_200_OK)

