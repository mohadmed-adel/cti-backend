from django.urls import path
from . import views


urlpatterns = [
    path(
        "services",
        views.MainServiceViewSet.as_view(),
    ),
    path(
        "services/<int:main_service_id>",
        views.MainServiceViewSet.as_view(),
    ),
    path("login/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
]
