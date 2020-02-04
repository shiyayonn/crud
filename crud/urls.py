from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
   path('admin/', admin.site.urls),  
   path('carview', views.carview),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('move/<int:id>',views.move),
    path('filter/<str:color>',views.filter)
]
