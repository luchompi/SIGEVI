from django.urls import path as p
from . import views as v
app_name="Home"

urlpatterns=[
p('',v.index),

]