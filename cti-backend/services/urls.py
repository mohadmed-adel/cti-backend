from django.urls import path
from . import views


urlpatterns = [
    path(
        "categories",
        views.MainServiceViewSet.as_view(),
    ),path(
        "services",
        views.MainServiceViewSet.as_view(),
    ),
    path(
        "services/<int:main_cate_id>",
        views.MainServiceViewSet.as_view(),
    ),
     path(
        "login",
        views.LoginView.as_view()
    ),
     path("user",views.UserRetrieveView.as_view()),
     path("requested_services",views.RequestedServicesListView.as_view()),
    path("comments/<int:requested_services_id>",views.RequestedComments.as_view()),
]
