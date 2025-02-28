from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Navire


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
            return Response({"reponse": 0}, status=200)
        else:
            thing = Id
            Id = 0
            return Response({"reponse": thing}, status=200)
            

# def ma_vue(request):
#     data = {'message': 'Bonjour depuis l\'API Django !'}
#     return JsonResponse(data)



def accueil(request):
    return render(request, "home.html") 

def database(request):
    all_Nav = Navire.objects.all()
    return render(request, "database.html", context={"all_Nav": all_Nav})