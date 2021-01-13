from django.urls import path
from .views import SilnikList
from .views import ModeleList
from .views import SilnikDetail
from .views import ModeleDetail
from .views import UserDetail
from .views import UserList
from .views import ApiRoot

urlpatterns = [
    path('silniks',SilnikList.as_view(), name=SilnikList.name),
    path('modeles',ModeleList.as_view(), name=ModeleList.name),
    path('silnik/<int:pk>', SilnikDetail.as_view(), name=SilnikDetail.name),
    path('modele/<int:pk>', ModeleDetail.as_view(), name=ModeleDetail.name),
    path('users', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
]