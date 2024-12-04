from .models import Recipe, Ingredient
from django import forms

class AddRecipeForm(forms.ModelForm):
    ingredients_list = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter ingredients separated by commas (e.g. flour, sugar, eggs)', 'rows': 4}),
        label='Ingredients',
        required=True  
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter cooking instructions', 'rows': 5}),
        label='Instructions',
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'cooking_time', 'servings', 'ingredients_list', 'instructions', 'image_url']
        widgets = {
            'recipe_name': forms.TextInput(attrs={'placeholder': 'Enter recipe name'}),
            'cooking_time': forms.TextInput(attrs={'placeholder': 'Enter cooking time (e.g. 30 minutes/1 hour)'}),
            'servings': forms.TextInput(attrs={'placeholder': 'Enter servings (e.g. 4 servings)'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter image URL'}),
        }

    def save(self, commit=True):
        recipe = super().save(commit=False)
        if commit:
            recipe.save()
            ingredients_list = self.cleaned_data['ingredients_list'].split(',')
            for ingredient_name in ingredients_list:
                ingredient_name = ingredient_name.strip()
                if ingredient_name:
                    ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                    recipe.ingredients.add(ingredient)
            recipe.save()
        return recipe

class CustomUserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    profile_image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(CustomUserEditForm, self).__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'profile'):
            self.fields['phone_number'].initial = self.instance.profile.phone_number
            self.fields['profile_image'].initial = self.instance.profile.profile_image

    def save(self, commit=True):
        user = super(CustomUserEditForm, self).save(commit=False)
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone_number = self.cleaned_data['phone_number']
            profile.profile_image = self.cleaned_data['profile_image']
            profile.save()
        return user