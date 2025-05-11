from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250,required=True,label="Username or phone",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=250,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20,widget = forms.PasswordInput,label='password')
    password2 = forms.CharField(max_length=20,widget = forms.PasswordInput,label='repeat_password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone'] 
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('پسورد ها مطابقت ندارد')
        return cd['password2']
    
    #create form do not replay same phone number)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("phone already exists!")
        return phone

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone','date_of_birth','bio','photo','job']

    #create form do not replay same phone number)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError("Phone already exists!")
        return phone
    #create form do not replay same username)
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError("username already exists!")
        return username

class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد','پیشنهاد'),
        ('انتقاد','انتقاد'),
        ('گزارش','گزارش' ),
    )
    message = forms.CharField(widget = forms.Textarea,required = True)
    name = forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={'placeholder':'نام',
                                                                                      'style':'height: 30px;'}))
    email = forms.EmailField()
    phone = forms.CharField(max_length=11,required=True)
    subject = forms.ChoiceField(choices = SUBJECT_CHOICES)