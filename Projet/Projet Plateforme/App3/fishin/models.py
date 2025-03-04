from django.db import models


class Navire(models.Model):
    id = models.TextField(max_length=62, unique=True, primary_key=True)  # Si tu veux un id personnalisé
    entreprise = models.TextField(max_length=62)
    image = models.ImageField(upload_to='navire/', null=True, blank=True, max_length=255)


class Historique(models.Model):
    etat = models.BooleanField(default=False)
    navire = models.ForeignKey(Navire, on_delete=models.CASCADE, null=True, blank=True)  # Référence à la classe Navire
    date = models.DateField()
    temps = models.TimeField()
