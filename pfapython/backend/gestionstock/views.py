
from django.contrib import auth
from django.core.checks import messages
from django.shortcuts import render,redirect
from django.views import View 
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login


# Create your views here.
class utilisateurviews(View):
    def get(self,request):
        utilisateurform=utilisateurforms()
        return render(request,"utilisateur_ajout.html",{'form':utilisateurform})
    def post(self,request):
        utilisateurform=utilisateurforms(request.POST,request.FILES)
        #if utilisateurform.is_valid():
        utilisateurform.save()       
        return redirect("utilisateuraffichage")

class utilisateurlistviews(View):
    def get(self,request):
        utilisateurlist=utilisateur.objects.all() 
        return render(request,"list_utilisateur.html",{'utilisateurlist':utilisateurlist })  

class categorieviews(View):
    def get(self,request):
        categorieform=categorieforms()
        return render(request,"ajout_categorie.html",{'form':categorieform})
    def post(self,request):
        categorieform=categorieforms(request.POST,request.FILES)
        if categorieform.is_valid():
            categorieform.save()       
        return redirect("categorieaffichage")        

class categorielistviews(View):
    def get(self,request):
        categorielist=categorie.objects.all() 
        return render(request,"list_categorie.html",{'categorielist':categorielist })  


class articleviews(View):
    def get(self,request):
        articleform=articleforms()
        return render(request,"article_ajout.html",{'form':articleform})
        
    def post(self,request):
        articleform=articleforms(request.POST,request.FILES)
        if articleform.is_valid():
            articleform.save()       
        return redirect("articleaffichage")   

class clientviews(View):
    def get(self,request):
        clientform=clientforms()
        return render(request,"ajout_client.html",{'form':clientform})
    def post(self,request):
        clientform=clientforms(request.POST,request.FILES)
        if clientform.is_valid():
            clientform.save()       
        return redirect("clientaffichage")           

class clientlistviews(View):
    def get(self,request):
        clientlist=client.objects.all() 
        return render(request,"list_client.html",{'clientlist':clientlist })  


class commandeviews(View):
    def get(self,request):
        commandeform=commandeforms()
        return render(request,"commande_ajout.html",{'form':commandeform})
    def post(self,request):
        commandeform=commandeforms(request.POST,request.FILES)
        if commandeform.is_valid():
            commandeform.save()       
        return redirect("commandelist")    

class articlelistviews(View):
    def get(self,request):
        articlelist=article.objects.all().order_by('prix') 
        categ=categorie.objects.all()
        return render(request,"list_articles.html",{'articlelist':articlelist ,'catlist':categ})  

class articlelistid(View):
    def get(self,request,pk):
     
        catename=categorie.objects.get(id=pk)
        articlelist=article.objects.filter(categorie=catename.id)
        return render(request,"list_articles2.html",{'articlelist':articlelist,'catlisttrie':catename})       


def updateutilisateur(request,pk):
    util= utilisateur.objects.get(id=pk)
    form = utilisateurforms(instance=util)
    utilisateurform=utilisateurforms(request.POST,request.FILES,instance=util)
    if utilisateurform.is_valid():
        utilisateurform.save()       
        return redirect("utilisateuraffichage")
    context={'form':form}
    return render(request,'utilisateur_ajout.html',context)    

class commandelistviews(View):
    def get(self,request):
        commandelist=commande.objects.all() 
        return render(request,"list_commandes.html",{'commandelist':commandelist })  


class deleteutilisateur(View):
    def get(self,request,pk):
        return render(request,"supprime_uti.html",{})
    def post(self,request,pk):
        util = utilisateur.objects.get(id=pk)
        util.delete()
        return redirect("utilisateuraffichage") 

class deletecategorie(View):
    def get(self,request,pk):
        return render(request,"supprime_cat.html",{})
    def post(self,request,pk):
        cat = categorie.objects.get(id=pk)
        cat.delete()
        return redirect("categorieaffichage") 

class deletecommande(View):
    def get(self,request,pk):
        return render(request,"supprimer_commande.html",{})
    def post(self,request,pk):
        cat = commande.objects.get(id=pk)
        cat.delete()
        return redirect("/commande") 

class deleteclient(View):
    def get(self,request,pk):
        return render(request,"supprime_cli.html",{})
    def post(self,request,pk):
        cli = client.objects.get(id=pk)
        cli.delete()
        return redirect("clientaffichage")   

class deletefournisseur(View):
    def get(self,request,pk):
        return render(request,"supprimer_fou.html",{})
    def post(self,request,pk):
        fou = fournisseur.objects.get(id=pk)
        fou.delete()
        return redirect("fournisseuraffichage")   


def updatecategorie(request,pk):
    util= categorie.objects.get(id=pk)
    form = categorieforms(instance=util)
    categorieform=categorieforms(request.POST,request.FILES,instance=util)
    if categorieform.is_valid():
        categorieform.save()       
        return redirect("categorieaffichage")
    context={'form':form}
    return render(request,'update_cat.html',context)

def updatearticle(request,pk):
    util= article.objects.get(id=pk)
    form = articleforms(instance=util)
    articleform=articleforms(request.POST,request.FILES,instance=util)
    if articleform.is_valid():
        articleform.save()       
        return redirect("articleaffichage")
    context={'form':form}
    return render(request,'article_ajout.html',context)

class deletearticle(View):
    def get(self,request,pk):
        return render(request,"supprime_art.html",{})
    def post(self,request,pk):
        art = article.objects.get(id=pk)
        art.delete()
        return redirect("articleaffichage") 
    
def updateclient(request,pk):
    util= client.objects.get(id=pk)
    form = clientforms(instance=util)
    clientform=clientforms(request.POST,request.FILES,instance=util)
    if clientform.is_valid():
        clientform.save()       
        return redirect("clientaffichage")
    context={'form':form}
    return render(request,'ajout_client.html',context)    

class fournisseurviews(View):
    def get(self,request):
        fournisseurform=fournisseurforms()
        return render(request,"ajout_fournisseur.html",{'form':fournisseurform})
    def post(self,request):
        fournisseurform=fournisseurforms(request.POST,request.FILES)
        if fournisseurform.is_valid():
            fournisseurform.save()       
        return redirect("fournisseuraffichage")   

class fournisseurlistviews(View):
    def get(self,request):
        fournisseurlist=fournisseur.objects.all() 
        return render(request,"list_fournisseur.html",{'fournisseurlist':fournisseurlist })   

def updatefournisseur(request,pk):
    four= fournisseur.objects.get(id=pk)
    form = fournisseurforms(instance=four)
    fournisseurform=fournisseurforms(request.POST,request.FILES,instance=four)
    if fournisseurform.is_valid():
        fournisseurform.save()       
        return redirect("fournisseuraffichage")
    context={'form':form}
    return render(request,'ajout_fournisseur.html',context)      
    
def loginviews(request):
    username = request.POST.get('login')
    passwordname = request.POST.get("password")

    user = auth.authenticate(login=username,password=passwordname)
    if user is not None:
        auth.login(request,user)
        return redirect("login/")
    else:
        messages.Info(request,'invalid')    


    
def home_page(request):
    return redirect('article/')     

class updatecommandeView(View):
    def get(self,request,pk):
        cmd=commande.objects.get(id=pk)
        cmdform=commandeforms(instance=cmd)
        return render(request,"update_commande.html",{"data":cmdform})
    
    def post(self,request,pk):
        cmd=commande.objects.get(id=pk)
        comdform=commandeforms(request.POST,request.FILES,instance=cmd)
        if comdform.is_valid():
            comdform.save()
        return redirect("/commande")
