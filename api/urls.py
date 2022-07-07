from django.urls import path
from . import services


# Routes [URL - Service]
urlpatterns = [
    # Root
    path('', services.root.root, name="root"),

    # Api
    path('routes', services.api.API, name="api"),

    # Models    [cars]
    path('cars/get', services.cars.get, name="cars_get"),
    path('cars/get/<str:id>', services.cars.get_id, name="cars_get_id"),
    path('cars/create', services.cars.create, name="cars_create"),
    path('cars/update/<str:id>', services.cars.update, name="cars_update"),
    path('cars/delete/<str:id>', services.cars.delete, name="cars_delete"),


]