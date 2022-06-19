from django.urls import path
from . import views


urlpatterns=[
    path('student',views.studentreg,name='student_reg'),
    path('student_details',views.details,name='student_details'),
    path('student_detail/<int:pk>',views.student_detail,name='student_detail'),
    path('studentupdate/<int:id>',views.update,name='student_update'),
    path('student_delete/<int:id>',views.delete,name='student_delete'),
    path('mark/<int:pk>',views.add_mark,name='mark'),
    path('search',views.search,name='search'),
]