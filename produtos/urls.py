from django.urls import path
from . import views


urlpatterns = [
    path('', views.CadastroProduto, name="cadastroproduto"),
    path('visualizar', views.ViewProduto.as_view(), name="visualizar"),
    path('apagar/<int:pk>/delete', views.DeleteProduto, name="deletar"),
    path('alterar/<int:pk>/alterar', views.AlterarProduto, name="alterar"),

]
