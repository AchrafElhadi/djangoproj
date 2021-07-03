from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('utilisateur/create', views.utilisateurviews.as_view(),name="utilisateurcreate"),
    path('utilisateur/', views.utilisateurlistviews.as_view(),name="utilisateuraffichage"),
    path('categorie/create', views.categorieviews.as_view(),name="categoriecreate"),
    path('categorie/', views.categorielistviews.as_view(),name="categorieaffichage"),
    path('article/create', views.articleviews.as_view(),name="articlecreate"),
    path('client/create', views.clientviews.as_view(),name="clientcreate"),
    path('client/', views.clientlistviews.as_view(),name="clientaffichage"),
    path('commande/create', views.commandeviews.as_view(),name="commandecreate"),
    path('article/', views.articlelistviews.as_view(),name="articleaffichage"),
    path('utilisateur/updateutilisateur/<str:pk>/', views.updateutilisateur,name="utilisateurupdate"),
    path('utilisateur/deleteutilisateur/<str:pk>/',views.deleteutilisateur.as_view(),name="utilisateurdelete"),
    path('article/updatearticle/<str:pk>/', views.updatearticle,name="articleupdate"),
    path('article/deletearticle/<str:pk>/',views.deletearticle.as_view(),name="articledelete"),
    path('client/updateclient/<str:pk>/', views.updateclient,name="clientupdate"),
    path('commande/deleteclient/<str:pk>',views.deletecommande.as_view(),name="deletecommande"),
    path('fournisseur/create', views.fournisseurviews.as_view(),name="fournisseurform"),
    path('fournisseur/', views.fournisseurlistviews.as_view(),name="fournisseuraffichage"),
    path('fournisseur/updatefournisseur/<str:pk>/', views.updatefournisseur,name="fournisseurupdate"),
    path('login/',views.loginviews,name="loginuser"),
    path('categorie/deletecategorie/<str:pk>/',views.deletecategorie.as_view(),name="categoriedelete"),
    path('categorie/updatecategorie/<str:pk>/', views.updatecategorie,name="categorieupdate"),
    path('client/deleteclient/<str:pk>/',views.deleteclient.as_view(),name="clientdelete"),
    path('fournisseur/deletefournisseur/<str:pk>/',views.deletefournisseur.as_view(),name="clientdelete"),
    path('',views.home_page,name="home"),
    path('commande/',views.commandelistviews.as_view(),name="commandelist"),
    path('article/<str:pk>/',views.articlelistid.as_view(),name="articles"),
    path('commande/updateclient/<str:pk>/',views.updatecommandeView.as_view(),name="updatecommande"),


    


]