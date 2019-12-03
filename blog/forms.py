from django import forms
from .models import User_Profile
#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['title', 'slug', 'author', 'updated_on',
        'content ', 'created_on',
        'category', 'imgfile',
        #status = models.IntegerField(choices=STATUS, default=0)
        ]