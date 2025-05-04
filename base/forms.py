from django import forms
from django.contrib.auth.models import User
from .models import TravelPackage, Destination, Package

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
class TravelPackageForm(forms.ModelForm):
    class Meta:
        model = TravelPackage
        fields = ['name', 'destination', 'price', 'duration', 'description', 'start_date', 'end_date', 'available_slots']
    
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'location', 'description', 'attractions', 'visit_hours', 'best_time',
                  'duration', 'shopping', 'restaurants', 'hotels', 'image', 'video']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'attractions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter attractions'}),
            'visit_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 9:00 AM - 5:00 PM'}),
            'best_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Spring, Summer'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 3-5 days'}),
            'shopping': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Popular shopping spots'}),
            'restaurants': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Recommended restaurants'}),
            'hotels': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Nearby hotels'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'price', 'destinations']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter package name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter package description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'destinations': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
