from django.urls import path
from .views import View,EntryShow
urlpatterns=[
    path('homemade/',View,name='ViewYourWork'),
    path('entryshow/',EntryShow,name='showthe work'),
#    path('savetimer/',)
]