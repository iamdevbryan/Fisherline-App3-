from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Navire, Historique
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


Id = 0


def index(request):
    return HttpResponse("Hello World")


@csrf_exempt
@api_view(['POST'])
def message_view(request):
    global Id
    data = request.data
    statut = request.data.get('message')
    statut_id = request.data.get('id')
    Id = {'message': statut, 'id': statut_id}
    print(data)
    return Response({"message_recu": data}, status=200)

 
@csrf_exempt
@api_view(['POST'])
def alert_confirm(request):
    global Id
    requete = request.data.get('requete')
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