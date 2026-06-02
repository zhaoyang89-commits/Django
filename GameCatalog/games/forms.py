from django import forms
from .models import Game
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 0 or rating > 10:
            raise forms.ValidationError('Rating must be between 0 and 10')
        return rating