from django.urls import path
from .views import storeView

urlpatterns=[
    path('store/',storeView.as_view(),name='store')
]