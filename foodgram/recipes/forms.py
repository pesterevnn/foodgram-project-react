from django.forms import ModelForm, Textarea

from .models import Recipes


class RecipeCreateForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'tags', 'ingredients', 'cooking_time', 'description', 'image', 'author']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form__input'
#        self.fields['tags'].widget.attrs['class'] = 'form__input'
        self.fields['ingredients'].widget.attrs['class'] = 'form__input'
        self.fields['cooking_time'].widget.attrs['class'] = 'form__input'
        self.fields['description'].widget.attrs['class'] = "form__textarea"
        self.fields['image'].widget.attrs['class'] = 'file'

#    def get_initial(self):
#        # call super if needed
#        return {'author': value}