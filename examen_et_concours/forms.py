from django.forms import ModelForm
from .models import Subject, Solution,Etablissement,Level,Year,Country,Concours,Matter,Category
from django import forms

class Searchform(ModelForm):
    class Meta:
        model = Subject
        fields = ['examen','year','matter','level','etablissement',]
        widgets = {
        'examen': forms.Select(attrs={"class":'form-control' ,'name':'title'}),
        'year' : forms.Select(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        'matter' : forms.Select(attrs={'class':"form-control", 'name':"matter", 'cols':"30" ,'rows':"5" }),
        'level' : forms.Select(attrs={'class':"form-control", 'name':"level" }),
        'etablissement' : forms.Select(attrs={'class':"form-control", 'name':"etablissement" }),
        
        } 
    
    
class addSolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['title','solution_file','price','creator',]
       
class addCountryForm(ModelForm):
    class Meta:

        model = Country
        fields = ['name',]
        

class addEtablissementForm(ModelForm):
    class Meta:

        model = Etablissement
        fields = ['name',]
        

class addLevelForm(ModelForm):
    class Meta:

        model = Level
        fields = ['name',]
        

class addMatterForm(ModelForm):
    class Meta:

        model = Matter
        fields = ['name',]
        

class addYearForm(ModelForm):
   class Meta: 

        model = Year
        fields = ['year',]
       

class addConcoursForm(ModelForm):
    class Meta:

        model = Concours
        fields = ['name','description','image','category',]
        
class addCategoryForm(ModelForm):
    class Meta:

        model = Category
        fields = ['name',]
        