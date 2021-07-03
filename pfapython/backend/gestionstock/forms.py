from .models import *
from django import forms

class utilisateurforms(forms.ModelForm):
    class Meta:
        model=utilisateur
        fields='__all__'

class clientforms(forms.ModelForm):
    class Meta:
        model=client
        fields='__all__'

class fournisseurforms(forms.ModelForm):
    class Meta:
        model=fournisseur
        fields='__all__'

class categorieforms(forms.ModelForm):
    class Meta:
        model=categorie
        fields='__all__'        

class articleforms(forms.ModelForm):
    class Meta:
        model=article
        fields='__all__'

class commandeforms(forms.ModelForm):
    class Meta:
        model=commande
        fields='__all__'

class factureforms(forms.ModelForm):
    class Meta:
        model=facture
        fields='__all__'        
