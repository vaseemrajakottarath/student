from django.urls import path
from . import views


urlpatttern=[
    path('student',views.studentreg,name='student_reg'),
    path('student',views.details,name='student_detail'),
    path('studentupdate/<int:id>',views.update,name='student_reg'),
    path('student_delete/<int:id>',views.delete,name='student_reg')
]