from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm, TravelPackageForm, DestinationForm, PackageForm
from .models import TravelPackage, Destination, Package, Package

# Home view
def home(request):
    return render(request, 'base/home.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create user but don't save it yet
            user = form.save(commit=False)
            # Set the password
            user.set_password(form.cleaned_data['password'])
            # Save the user
            user.save()

            # Log the user in after signup
            auth_login(request, user)

            # Redirect to a success page (e.g., home page)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignupForm()

    return render(request, 'base/signup.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please fill in both email and password.')
            return redirect('login')

        # Fetch all users with the provided email
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()  # Get the first matching user

            # Authenticate using the username and password
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'No account found with this email.')

    return render(request, 'base/login.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

# About view
def about(request):
    return render(request, 'base/about.html')

# View to display all travel packages
def travel_packages(request):
    packages = TravelPackage.objects.all()
    return render(request, 'base/travel_packages.html', {'packages': packages})

# View to add a new travel package
def add_travel_package(request):
    if request.method == 'POST':
        form = TravelPackageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the package to the database
            return redirect('travel_packages')  # Redirect to the travel packages list
    else:
        form = TravelPackageForm()

    return render(request, 'base/add_package.html', {'form': form})

def packages_view(request):
    return render(request, 'base/travel_packages.html')

# View to display all destinations
def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'base/destinations.html', {'destinations': destinations})

# View to add a new destination
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the destination to the database
            return redirect('destinations')  # Redirect to the destinations list
    else:
        form = DestinationForm()

    return render(request, 'base/add_destination.html', {'form': form})

def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')  # Redirect to the package list view
    else:
        form = PackageForm()
    
    return render(request, 'base/add_package_1.html', {'form': form})

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'base/package_list.html', {'packages': packages})

def package_detail(request,pk):
    package = get_object_or_404(Package, pk = pk)
    return render(request, 'base/package_detail.html', {'package': package})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk = pk)
    return render(request, 'base/destination_detailS.html', {'destination': destination})

def Luxury(request):
    #Luxury = get_object_or_404(Luxury, pk = pk)
    return render(request, 'base/Luxury.html')

def restaurant_page(request):
    return render(request, 'base/restaurants.html')

def budget_friendly(request):
    return render(request, 'base/budget.html')

'''def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user  # Set the current user
            itinerary.save()
            return redirect('view_itinerary', pk=itinerary.pk)  # Redirect to the new itinerary's page
    else:
        form = ItineraryForm()

    return render(request, 'base/create_itinerary.html', {'form': form})'''

'''def add_destinations(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    
    if request.method == 'POST':
        form = ItineraryDestinationForm(request.POST)
        if form.is_valid():
            itinerary_destination = form.save(commit=False)
            itinerary_destination.itinerary = itinerary
            itinerary_destination.save()
            return redirect('view_itinerary', pk=itinerary.id)  # Redirect to the itinerary view
    else:
        form = ItineraryDestinationForm()

    return render(request, 'base/add_destinations.html', {'form': form, 'itinerary': itinerary})'''

'''def view_itinerary(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    itinerary_destinations = ItineraryDestination.objects.filter(itinerary=itinerary).order_by('day')
    
    return render(request, 'base/view_itinerary.html', {
        'itinerary': itinerary,
        'itinerary_destinations': itinerary_destinations
    })'''

'''def view_itinerary_list(request):
    itineraries = Itinerary.objects.all()  # Adjust query as needed
    return render(request, 'view_itinerary_list.html', {'itineraries': itineraries})'''

def delete_destination(request, pk):
    if request.method == "POST":
        destination = get_object_or_404(Destination, pk=pk)
        destination.delete()
        return redirect('destinations')
    
def update_destination(request, pk):
    # Logic for updating the destination (render form, handle POST)
    pass

def update_package(request, pk):
    package = get_object_or_404(Package, pk=pk)

    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm(instance=package)

    return render(request, 'base/package_form.html', {'form': form, 'package': package})

# Delete a package
def delete_package(request, pk):
    package = get_object_or_404(Package, pk=pk)

    if request.method == 'POST':
        package.delete()
        return redirect('package_list')

    return render(request, 'base/package_confirm_delete.html', {'package': package})

def search_destinations(request):
    query = request.GET.get('q','')
    results = Destination.objects.filter(name__icontains=query)
    return render(request, 'base/search_results.html', {'query' : query, 'results' : results})