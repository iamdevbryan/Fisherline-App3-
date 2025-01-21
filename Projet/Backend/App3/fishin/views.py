from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


Id = 0


def index(request):
    return HttpResponse("Hello World")


class MessageView(APIView):
    def post(self, request):
        texte = request.data.get('texte')
        global Id
        Id = texte
        print(texte)
        print(request.data)
        return Response({"message_recu": texte}, status=200)
    

class AlertConfirm(APIView):
    def post(self, request):
        requete = request.data.get('requete')
        global Id
        if Id == 0:
            print(request.data)
            return Response({"reponse": 0}, status=400)
        else:
            return Response({"reponse": Id}, status=200)

# def ma_vue(request):
#     data = {'message': 'Bonjour depuis l\'API Django !'}
#     return JsonResponse(data)