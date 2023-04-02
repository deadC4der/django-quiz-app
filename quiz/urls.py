from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('quizzes/', views.QuizListView.as_view(), name='quiz_index'),
    path('category/', views.CategoriesListView.as_view(), name='quiz_category_list_all'),
    path('category/<slug:category_name>/', views.ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    path('progress/', views.QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/', views.QuizMarkingList.as_view(), name='quiz_marking'),
    path('marking/<int:pk>/', views.QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    path('<slug:slug>/', views.QuizDetailView.as_view(), name='quiz_start_page'),
    path('<slug:quiz_name>/take/', views.QuizTake.as_view(), name='quiz_question'),
]