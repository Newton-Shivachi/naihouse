from django.urls import path
from .views import home,HouseForSale,HouseForRent,Cars,detail,search,cardetail,video

app_name = 'home'

urlpatterns = [
    path('video/',video,name='video'),
    path('search/',search,name='search'),
    path('car/<int:pk>/',cardetail,name='cardetail'),
    path('house/<int:pk>/',detail,name='detail'),
    path('cars/',Cars,name='cars'),
    path('rentals/',HouseForRent,name='houseforrent'),
    path('houses/',HouseForSale,name='houseforsale'),
    path('', home, name='home'),
]
