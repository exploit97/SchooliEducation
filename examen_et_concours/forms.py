from django.forms import ModelForm
from .models import Subject, Solution,Etablissement,Level,Year,Country,Evaluation,Matter,Category
from django import forms

class Searchform(ModelForm):
    class Meta:
        model = Subject
        fields = ['evaluation','year','matter','level','etablissement',]
        widgets = {
        'evaluation': forms.Select(attrs={"class":'form-control' ,'name':'title'}),
        'year' : forms.Select(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        'matter' : forms.Select(attrs={'class':"form-control", 'name':"matter", 'cols':"30" ,'rows':"5" }),
        'level' : forms.Select(attrs={'class':"form-control", 'name':"level" }),
        'etablissement' : forms.Select(attrs={'class':"form-control", 'name':"etablissement" }),
        
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].queryset = Level.objects.none()

        if 'evaluation' in self.data:
            try:
                evaluation_id = int(self.data.get('evaluation'))
                self.fields['level'].queryset = Level.objects.filter(evaluation_id=evaluation_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['level'].queryset = self.instance.evaluation.level_set.order_by('name') 
    
    
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
       

class addEvaluationForm(ModelForm):
    class Meta:

        model = Evaluation
        fields = ['name','description','image','category',]
        
class addCategoryForm(ModelForm):
    class Meta:

        model = Category
        fields = ['name',]
        