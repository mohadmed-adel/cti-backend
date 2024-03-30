from django.urls import path
from . import views


urlpatterns = [
    path(
        "categories",
        views.MainServiceViewSet.as_view(),
    ),
    path(
        "services/<int:main_cate_id>",
        views.MainServiceViewSet.as_view(),
    ),
     
]
