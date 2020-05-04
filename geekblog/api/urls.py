from django.urls import path

from geekblog.api.views import api_view

app_name = "users"
urlpatterns = [
    path("test/", view=api_view.ApiList.as_view(), name="api_test"),

]
