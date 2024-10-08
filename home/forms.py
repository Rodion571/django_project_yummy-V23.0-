from django import forms
from .models import Reservation
import datetime


class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Your Name',
                                                                                      'class': 'form-control',
                                                                                      'id': 'name',
                                                                                      'data-rule': 'minlen:4',
                                                                                      'data-msg': 'Please enter at least 4 chars'}))
    phone = forms.CharField(max_length=20, label='Phone', widget=forms.TextInput(attrs={'placeholder': 'Your Phone',
                                                                                        'class': 'form-control',
                                                                                        'id': 'phone',
                                                                                        'data-rule': 'minlen:4',
                                                                                        'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                            'id': 'email',
                                                                            'data-rule': 'email',
                                                                            'data-msg': 'Please enter a valid email'
                                                                           }))
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'placeholder': 'Date',
                                                                       'class': 'form-control',
                                                                       'id': 'date',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'placeholder': 'Time',
                                                                       'class': 'form-control',
                                                                       'id': 'time',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    people = forms.IntegerField(label='People', widget=forms.NumberInput(attrs={'placeholder': 'People',
                                                                                'class': 'form-control',
                                                                                'id': 'people',
                                                                                'data-rule': 'minlen:1',
                                                                                'data-msg': 'Please enter at least 1 chars'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                                            'class': 'form-control',
                                                                            'id': 'message',
                                                                            'data-rule': 'minlen:4',
                                                                            'data-msg': 'Please enter at least 4 chars'}))



    def clean_name(self):
        name = self.cleaned_data['name']
        return f'*{name.title()}*'

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError('Invalid date - reservation in the past')
        return date


    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'time', 'people', 'message')