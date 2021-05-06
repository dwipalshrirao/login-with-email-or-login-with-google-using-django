from django import forms
from .models import customUser
from django.utils.translation import ugettext_lazy as _
# class loginForm(forms.form):
#     emai=forms.EmailField()





class registerForm(forms.ModelForm):
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password","required":"True"}))
    
    class Meta:
        model = customUser	 

        fields =('email','first_name','last_name','photo','password','password1')
        
        widgets = {       

            'email': forms.EmailInput(attrs={"class":"form-control","placeholder":"Email","required":"True"}),
            'first_name':forms.TextInput(attrs={"class":"form-control","placeholder":"First Name","required":"True"}),
            'last_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name","required":"True"}),
            'password':forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","required":"True"}),
            'password1':forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password","required":"True"}),
            'password1':forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password","required":"True"}),
            'photo':forms.FileInput(attrs={"class":"form-control","required":"True"}),

        }

    def clean(self):


        super(registerForm, self).clean()
		
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        email=self.cleaned_data.get('email')

        if password !=password1:
            self._errors['password'] = self.error_class([
				'both password must be same'])
		
        ql=customUser.objects.filter(email=email).first()
        if ql:
            self._errors['email'] = self.error_class([
				'user already exist'])

        return self.cleaned_data



class UpdateForm(registerForm):
    password1=None
    password=None
    photo=forms.ImageField(label=_('profile pic'))
    class Meta:
        model = customUser	 

        fields =('email','first_name','last_name','photo')
        
        widgets = {       
            'email': forms.EmailInput(attrs={"class":"form-control-plaintext","placeholder":"None","required":"True","readonly":True}),
            'first_name':forms.TextInput(attrs={"class":"form-control-plaintext","placeholder":"None","required":"True","readonly":True}),
            'last_name':forms.TextInput(attrs={"class":"form-control-plaintext","placeholder":"None","required":"True","readonly":True}),
            'photo':forms.FileInput(attrs={"class":"form-control-plaintext","required":"True"}),

            
        }

    def clean(self):


        super(registerForm, self).clean()
		
        email=self.cleaned_data.get('email')

		
        ql=customUser.objects.filter(email=email).first()
        print(ql)
        if ql and (ql.email != email):

            self._errors['email'] = self.error_class([
				'user already exist'])

        return self.cleaned_data