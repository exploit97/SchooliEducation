from django.urls import path, include
from  examen_et_concours.views import home,TousLesConcours,ConcoursDescription,addCategory,addConcours, addSolution,addMatter,addLevel,addYear,addCountry,addEtablissement, examenSearchForm, searchConcoursSujects, searchExam,concoursSubjectForm, searchConcours,ConcoursSubjectDescription,SameConcours,AddSubjectView

app_name = 'examen_et_concours'
urlpatterns = [
    path('', home,name='home'),
    path('concours/liste', TousLesConcours.as_view(),name='touslesconcours'),
    path('concours/description/<int:pk>/', ConcoursDescription.as_view(),name='concours_description'),
    path('concours/liste/<str:cats>', SameConcours,name='SameConcours'),
    path('examens/sujets/search', examenSearchForm,name='Searchform'),
    path('concours/sujets/<str:name>', concoursSubjectForm,name='concours_subjects_form'),
    path('concours/sujets/search/result', searchConcoursSujects,name='concours_subjects'),
    path('concours/sujets/description/<int:id>', ConcoursSubjectDescription,name='subject_description'),
    path('concours/sujets/examens/search/', searchExam,name='searchExam'),
    path('examens/sujets/search/result',searchConcours , name='search_concours'),
    path('examens/sujets/addsubject',AddSubjectView.as_view() , name='add_subject'),
    path('examens/sujets/add_category',addCategory.as_view(), name='add_category'),
    path('examens/sujets/add_solution',addSolution.as_view(), name='add_solution'),
    path('examens/sujets/add_year',addYear.as_view(), name='add_year'),
    path('examens/sujets/add_country',addCountry.as_view(), name='add_country'),
    path('examens/sujets/add_level',addLevel.as_view(), name='add_level'),
    path('examens/sujets/add_matter',addMatter.as_view(), name='add_matter'),
    path('examens/sujets/add_etablissement',addEtablissement.as_view(), name='add_etablissement'),
    path('examens/sujets/add_examen',addConcours.as_view(), name='add_examen'),


]


