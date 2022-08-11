import re
from django.core.checks import messages
from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from myscrumy.settings import DATABASES
from .models import ChatMessage, Connection
import requests
import boto3

# Create your views here.

# create test view

@csrf_exempt
def test(request):
    return JsonResponse({'message':'Hello Daud'}, status=200)

# Helper function for request object
def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)
    

def _send_to_connection(connection_id, data):
    gatewayapi=boto3.client('apigatewaymanagementapi', endpoint_url='https://mpwzylrgdk.execute-api.us-east-2.amazonaws.com/test/', region_name='us-east-2', aws_access_key_id='AKIAW5VCZOENTS7E4L6C', aws_secret_access_key='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')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))


# connect view

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connection = Connection.objects.create(connection_id=connection_id)
    connection.save()
    return JsonResponse({'message':'Connected Successfully'}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    Connection.objects.filter(connection_id=connection_id).delete()
    return JsonResponse({'message':'Disconnected Successfully'}, status=200)

@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    body = body['body']
    username = body['username']
    content = body['content']
    timestamp = body['timestamp']
    chat = ChatMessage(username=username, message=content, timestamp=timestamp)
    chat.save()
    data = {'messages':[body]}
    for connection in Connection.objects.all():
        _send_to_connection(connection.connection_id, data)
    
    return JsonResponse({'message':'Message sent to all connections successfully'}, status=200)
    

@csrf_exempt
def get_recent_message(request):
    messages = []
    chats = ChatMessage.objects.all().order_by("-id")
    for i in range(len(chats)):
        data = {
                'username': chats[i].username, 
                'message': chats[i].message, 
                'timestamp': chats[i].timestamp
            }

        messages.append(data)
    
    data = {'messages':messages}
    for connection in Connection.objects.all():
        _send_to_connection(connection.connection_id, data)
    return JsonResponse(data, status=200)

