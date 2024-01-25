from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('passbook/', views.passbook, name="passbook"),
    path('want', views.want, name="want"),
    path('setting', views.setting, name="setting"),
    path('new', views.new, name="new"),
    path('neww', views.neww, name="neww"),
    # path('<int:id>swap', views.swap, name="swap"),
    path('<int:id>edit', views.edit, name="edit"),
    path('<int:id>edit0', views.edit0, name="edit0"),
    path('<int:id>editi', views.editi, name="editi"),
    path('<int:id>edito', views.edito, name="edito"),
    path('<int:id>update', views.update, name="update"),
    path('<int:id>/delete', views.delete, name="delete"),
    path('new1', views.new1, name="new1"),
    path('<int:id>edit1', views.edit1, name="edit1"),
    path('<int:id>update1', views.update1, name="update1"),
    path('<int:id>/delete1', views.delete1, name="delete1"),
]