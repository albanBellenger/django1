from django.contrib.auth.models import User
from django import forms
from polls.models import Question, Choice
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(max_length=200, help_text="Add you question oK?")
    pub_date = forms.DateField(widget=forms.HiddenInput(),initial=datetime.date.today)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Question


class ChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(max_length=200, help_text="And your choices (just one now)?")
    votes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #question = Question

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Choice