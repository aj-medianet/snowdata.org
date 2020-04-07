from django.conf.urls import url
from .views import SkiAreaRUDView

urlpatterns = [
    url(r"(?P<pk>\d+)/^$", SkiAreaRUDView.as_view(), name="sa_rud")
]
