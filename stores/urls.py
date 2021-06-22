from .views import PizzeriaListView
from django.urls import path
from . import views

urlpatterns =[
    path('',views.PizzeriaListView.as_view(),name='pizzeria_list'),
    path('<int:id>/',views.PizzeriaDetailView.as_view(),name='pizzeria_detail'),
    path('create/',views.PizzeriaCreateView.as_view(),name='pizzeria_create'),
    path('update/<int:id>/',views.PizzeriaRetrieveUpdateAPIView.as_view(),
                name='pizzeria_update'),

    path('delete/<int:id>',views.PizzeriaDeleteView.as_view(),name='pizzeria_delete'),
]

