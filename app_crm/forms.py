# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms

# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(label='',
#                                     max_length=20,
#                                     widget=forms.TextInput(
#                                         attrs={'class':'form-control',
#                                                 'placeholder':'First Name'}))
#     last_name = forms.CharField(label='',
#                                     max_length=20,
#                                     widget=forms.TextInput(
#                                         attrs={'class':'form-control',
#                                                 'placeholder':'Last Name'}))
#     username = forms.CharField(label='', 
#                                 max_length=150,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control', 
#                                             'placeholder':'Username'}))
#     email = forms.EmailField(label='',
#                                 max_length=100,
#                                 widget=forms.EmailInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Email Address'}))
#     address = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Address'}))
#     city = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'City'}))
#     state = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'State'}))
#     zipcode = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Zipcode'}))
#     internet_provider = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Internet Provider'}))
#     internet_speed = forms.CharField(label='',
#                                 max_length=100,
#                                 widget=forms.TextInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Internet Speed'}))
#     password1 = forms.CharField(label='',
#                                 max_length=20,
#                                 widget=forms.PasswordInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Password'}))
#     password2 = forms.CharField(label='',
#                                 max_length=20,
#                                 widget=forms.PasswordInput(
#                                     attrs={'class':'form-control',
#                                             'placeholder':'Confirm Password'}))

#     class Meta:
#         model = User
#         fields = [
#             'first_name', 'last_name', 'username', 'email',
#             'address', 'city', 'state', 'zipcode',
#             'internet_provider', 'internet_speed',
#             'password1', 'password2']
    
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)

#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#             self.fields[field].label = ''
        
#         self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
#         self.fields['username'].widget.attrs['placeholder'] = 'Username'
#         self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
#         self.fields['address'].widget.attrs['placeholder'] = 'Address'
#         self.fields['city'].widget.attrs['placeholder'] = 'City'
#         self.fields['state'].widget.attrs['placeholder'] = 'State'
#         self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
#         self.fields['internet_provider'].widget.attrs['placeholder'] = 'Internet Provider'
#         self.fields['internet_speed'].widget.attrs['placeholder'] = 'Internet Speed'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
#         self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
#         self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
#         self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	