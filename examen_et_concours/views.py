from django.shortcuts import render, get_object_or_404
from .models import Evaluation, Category, Solution, Subject,Level,Matter,Country,Year,Etablissement
from django.views.generic import ListView, UpdateView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy,reverse
from .forms import addEvaluationForm,addCountryForm,addEtablissementForm,addLevelForm,addSolutionForm,addYearForm,addMatterForm,addCategoryForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

def home(request):
    context = {'djo':'djo'}
    return render(request, 'examen_et_concours/home.html',context )

class TousLesConcours(ListView):
    template_name='examen_et_concours/touslesconcours.html'
    model = Evaluation
    paginate_by = 6

class ConcoursDescription(DetailView):
    template_name='examen_et_concours/concours_description.html'
    model = Evaluation
   
 

def SameConcours(request, cats):                     
    cats = get_object_or_404(Category, name = cats)
    concours = cats.evaluation_set.all()
    context = {'concours':concours} 
    return render(request,'examen_et_concours/SameConcours.html',context)


def examenSearchForm(request):
    level = Level.objects.all()
    matter = Matter.objects.all()
    year = Year.objects.all()
    evaluation = Evaluation.objects.all()
    country = Country.objects.all()
    context = {'level':level,
    'matter':matter,
    'year':year,
    'country':country,
    'evaluation':evaluation, 
    }
    return render(request,'examen_et_concours/examen_search_form.html',context) 

def concoursSubjectForm(request,name):
    level = Level.objects.all()
    matter = Matter.objects.all()
    year = Year.objects.all()
    evaluation = Evaluation.objects.get(name = name )
    country = Country.objects.all()
    context = {'level':level,
    'matter':matter,
    'year':year,
    'country':country,'evaluation':evaluation,
    'name':name }
    return render(request,'examen_et_concours/concours_subjects_form.html',context) 
    



def ConcoursSubjectDescription(request, id):
    
    description = Subject.objects.get(pk=id)
    

    context = {'description' : description}    
    return render(request,'examen_et_concours/subject_description.html',context)
    

def searchExam(request):
    evaluation = request.GET.get('evaluation')
    Niveau = request.GET.get('Niveau')
    matter = request.GET.get('matter')
    country = request.GET.get("country")
    year = request.GET.get("year")
    yearf = request.GET.get("yearf")  
   
  
    sujet = Subject.objects.filter(evaluation=evaluation,level = Niveau,matter = matter,country=country
    ).filter(year__gte = year).filter(
            year__lte = yearf)
        
    

         
    touslessujets = sujet
    title='voici les sujets trouvés : '
    
    if not touslessujets.exists():
        title = "Aucune reponse ne correspond"
    context = {
        'touslessujets': touslessujets,
        'title': title
    }
    return render(request, 'examen_et_concours/sujets.html', context)
    
def searchConcours(request):
    query = request.GET.get('query')
    if not query :
        concours = Evaluation.objects.all()
        
    else:
        # title contains the query is and query is not sensitive to case.
        concours = Evaluation.objects.filter(name__icontains=query)
    
    paginator = Paginator(concours, 6)
    page = request.GET.get('page')
    try:
        concours = paginator.page(page)
    except PageNotAnInteger:
        concours = paginator.page(1)
    except EmptyPage:
        concours = paginator.page(paginator.num_pages)
    
    title = "Resultats pour la réquête %s"%query
    context = {
        'concours_search': concours,
        'title': title,
        'paginate': True
    }
    return render(request, 'examen_et_concours/search_concours.html', context)

class AddSubjectView(CreateView):

    model = Subject
    template_name = 'examen_et_concours/add_subject.html'
    #form_class = AddsubjectForm
    fields = '__all__'
    success_url = reverse_lazy('examen_et_concours:touslesconcours')
     
class addConcours(CreateView):
    model = Evaluation
    form_class=addEvaluationForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addLevel(CreateView):
    model = Level
    form_class=addLevelForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addMatter(CreateView):
    model = Matter
    form_class=addMatterForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addYear(CreateView):
    model = Year
    form_class=addYearForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addCountry(CreateView):
    model = Country
    form_class=addCountryForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addCategory(CreateView):
    model = Category
    form_class=addCategoryForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addSolution(CreateView):
    model = Solution
    form_class=addSolutionForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')


class addEtablissement(CreateView):
    model = Etablissement
    form_class=addEtablissementForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')
    

# AJAX
def load_levels(request):
    evaluation_id = request.GET.get('evaluation')
    levels = Level.objects.filter(evaluation_id=evaluation_id).all()
    return render(request, 'examen_et_concours/dropdown_list_options.html', {'levels': levels})

def load_matters(request):
    level_id = request.GET.get('level')
    matters = Matter.objects.filter(level_id=level_id).all()
    return render(request, 'examen_et_concours/dropdown_list_options.html', {'levels': matters})
   

            
                    
         
       