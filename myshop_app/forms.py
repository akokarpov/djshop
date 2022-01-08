from django import forms
from .models import Product
from PIL import Image

PATH_IMG_ORIGINALS = 'myshop_app/static/myshop_app/img/originals/'
PATH_IMG_THUMBNAILS = 'myshop_app/static/myshop_app/img/thumbnails/'

class ProductForm(forms.ModelForm):

    file = forms.ImageField()

    class Meta():
        model = Product
        fields = ['title', 'specs', 'image', 'price']
    
    def save_image(self):
        with Image.open(self.cleaned_data['file']) as image:
            image.save(fp=f"{PATH_IMG_ORIGINALS}{self.cleaned_data['file']}")
            image.thumbnail((200, 200))
            image.save(fp=f"{PATH_IMG_THUMBNAILS}{self.cleaned_data['file']}")
    
    def clean(self):
        self.cleaned_data['image'] = self.cleaned_data['file']