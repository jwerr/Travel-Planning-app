from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Authentication paths
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about_worcester/', views.about, name='about'),
    path('packages/', views.travel_packages, name='travel_packages'),
    path('add_package/', views.add_travel_package, name='add_travel_package'),
    path('packages/', views.packages_view, name='packages'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('destinations/', views.destinations, name='destinations'),
    path('add_package_1/', views.add_package, name='add_package'),
    path('packages_1/', views.package_list, name='package_list'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    path('package/<int:pk>/update/', views.update_package, name='update_package'),  # Update package URL
    path('package/<int:pk>/delete/', views.delete_package, name='delete_package'),  # Delete package URL

    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('Luxury/', views.Luxury, name='Luxury'),
    path('restaurants/', views.restaurant_page, name='restaurant_page'),
    path('budgets/', views.budget_friendly, name='budget'),  # Comma added here
    #path('itinerary/create/', views.create_itinerary, name='create_itinerary'),
    #path('itinerary/<int:itinerary_id>/add-destinations/', views.add_destinations, name='add_destinations'),
    #path('itinerary/<int:pk>/', views.view_itinerary, name='view_itinerary'),
    #path('itinerary/', views.view_itinerary_list, name='view_itinerary_list'),
    path('destination/<int:pk>/delete/', views.delete_destination, name='delete_destination'),
    path('destination/<int:pk>/update/', views.update_destination, name='update_destination'),
    path('search/', views.search_destinations, name = 'search_destinations'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)