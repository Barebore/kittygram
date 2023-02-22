from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter

from cats.views import APICat, CatDetail, CatList, CatViewSet, cat_list, hello

router = SimpleRouter()

router.register('cats', CatViewSet, basename='tiger')

# urlpatterns = [
#    path('cats/', CatList.as_view()),
#    path('hello/', CatDetail.as_view()),
#    path('gigachad/', CatViewSet.as_view({
#       'get': 'list',
#       'post': 'create'
#    })),
# ]

urlpatterns = [
   path('', include(router.urls)),
]

router = DefaultRouter()

router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
