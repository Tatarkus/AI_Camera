from django.conf.urls import url
from . import views

urlpatterns = [
	url (r'^home/', views.index, name='home'),
	url(r'^entrenar/',views.entrenar, name='entrenar'),

]