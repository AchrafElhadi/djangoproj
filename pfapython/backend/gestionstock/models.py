from django.db import models

# Create your models here.
class utilisateur(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField(max_length=100)
    ville=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    cin=models.CharField(max_length=100)
    img=models.ImageField(upload_to="images/")
    login=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class client(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField(max_length=100)
    ville=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    site=models.URLField(max_length=100)
    def __str__(self): 
        return self.nom
    
class fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField(max_length=100)
    ville=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    site=models.URLField(max_length=100)

class categorie(models.Model):
    nom=models.CharField(max_length=100)
    def __str__(self): 
        return self.nom
    description=models.TextField()
    


class article(models.Model):
    nom=models.CharField(max_length=100)
    prix=models.FloatField()
    description=models.TextField()
    nbstock=models.IntegerField()
    img=models.ImageField(upload_to="images/")
    categorie=models.ForeignKey(categorie,on_delete=models.CASCADE)
    taille=models.FloatField()
    def __str__(self): 
        return self.nom

class commande(models.Model):
    article=models.ForeignKey(article,on_delete=models.CASCADE)
    nbarticle=models.IntegerField()
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    etat=models.CharField(max_length=100,default='non traitée')

class facture(models.Model):
    commande=models.ForeignKey(commande,on_delete=models.CASCADE)
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    tva=models.CharField(max_length=100)
    prix_tva=models.FloatField()



     