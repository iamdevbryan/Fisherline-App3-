from django.contrib import admin
from .models import Navire, Historique

# Pour le modèle Navire
class NavireAdmin(admin.ModelAdmin):
    list_display = ('id', 'entreprise')  # Afficher ces champs dans la liste
    search_fields = ('id', 'entreprise')  # Ajouter une barre de recherche pour ces champs
    list_filter = ('entreprise',)  # Ajouter un filtre pour le champ entreprise

# Pour le modèle Historique
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('navire', 'etat', 'date', 'temps')  # Afficher ces champs dans la liste
    search_fields = ('navire__id',)  # Rechercher par l'id du navire
    list_filter = ('etat', 'date')  # Ajouter des filtres pour les champs etat et date
    list_per_page = 20  # Nombre de lignes à afficher par page

# Enregistrer les modèles avec leurs classes d'administration
admin.site.register(Navire, NavireAdmin)
admin.site.register(Historique, HistoriqueAdmin)
