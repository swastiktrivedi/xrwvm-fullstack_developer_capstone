from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path(route='register/', view=views.registration, name='register'),

    # Path for login
    path(route='login/', view=views.login_user, name='login'),
    path('login', views.login_user),
    # Path for logout
    path(route='logout/', view=views.logout_request, name='logout'),
    
    # Path for fetching car details
    path(route='get_cars/', view=views.get_cars, name='get_cars'),

    # Path for dealer views
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>/', view=views.get_dealerships, name='get_dealers_state'),
    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),

    # Path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>/', view=views.get_dealer_reviews, name='dealer_reviews'),

    # Path for adding a review
    path(route='add_review/', view=views.add_review, name='add_review'),
    path('add_review', views.add_review,),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
