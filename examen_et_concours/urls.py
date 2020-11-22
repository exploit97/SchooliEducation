from django.urls import path, include
from  examen_et_concours import views

app_name = 'examen_et_concours'
urlpatterns = [
    path('', views.home,name='home'),
    path('concours/liste', views.TousLesConcours.as_view(),name='touslesconcours'),
    path('concours/description/<int:pk>/', views.ConcoursDescription.as_view(),name='concours_description'),
    path('concours/liste/<str:cats>', views.SameConcours,name='SameConcours'),
    path('examens/sujets/search', views.examenSearchForm,name='Searchform'),
    path('concours/sujets/<str:name>', views.concoursSubjectForm,name='concours_subjects_form'),
    path('concours/sujets/description/<int:id>', views.ConcoursSubjectDescription,name='subject_description'),
    path('concours/sujets/examens/search/', views.searchExam,name='searchExam'),
    path('examens/sujets/search/result',views.searchConcours , name='search_concours'),
    path('examens/sujets/addsubject',views.AddSubjectView.as_view() , name='add_subject'),
    path('examens/sujets/add_category',views.addCategory.as_view(), name='add_category'),
    path('examens/sujets/add_solution',views.addSolution.as_view(), name='add_solution'),
    path('examens/sujets/add_year',views.addYear.as_view(), name='add_year'),
    path('examens/sujets/add_country',views.addCountry.as_view(), name='add_country'),
    path('examens/sujets/add_level',views.addLevel.as_view(), name='add_level'),
    path('examens/sujets/add_matter',views.addMatter.as_view(), name='add_matter'),
    path('examens/sujets/add_etablissement',views.addEtablissement.as_view(), name='add_etablissement'),
    path('examens/sujets/add_examen',views.addConcours.as_view(), name='add_examen'),
    path('ajax/load-levels/', views.load_levels, name='ajax_load_levels'), # AJAX
    path('ajax/load-matters/',views.load_matters, name='ajax_load_matters'), # AJAX


]


