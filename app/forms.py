from django import forms
from .models import Money
from .models import Want

class DateInput(forms.DateInput):
    input_type = 'date'

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ("title","title2","duedate","content","balance")
        widgets = {
            'duedate': DateInput(),
        }

class WantForm(forms.ModelForm):
    class Meta:
        model = Want
        fields = ("memo","yen")
        