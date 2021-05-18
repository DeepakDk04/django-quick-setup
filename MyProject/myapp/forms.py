from django.forms import ModelForm


from .models import Product



class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description']

# class updateProfile(ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user','username']


