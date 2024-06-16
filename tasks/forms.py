from django import forms
from .models import Task
from django.contrib.auth import get_user_model
from statuses.models import Status
from labels.models import Label
from django.utils.translation import gettext_lazy as _


class CreateTaskFrom(forms.ModelForm):
    name = forms.CharField(max_length=150,
                           required=True,
                           label=_('Name'),

                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': _('Name')
                                      }))

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=True,
        label=_('Status'),
        widget=forms.Select(
            attrs={'class': 'form-select',
                   'placeholder': _('Status')
                   })
    )

    executor = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        required=False,
        label=_('Executor'),
        widget=forms.Select(
            attrs={'class': 'form-select',
                   'placeholder': _('Executor')
                   })
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_('Label'),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-select',
                   'placeholder': _('Labels')
                   })
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']

        labels = {
            'description': _('Description'),
            'executor': _('Executor'),
        }

        widgets = {
            'description': forms.Textarea(attrs={
                'cols': '40',
                'rows': '10',
                'class': 'form-control',
                'placeholder': _('Description')
            }),
        }


class UpdateTaskForm(CreateTaskFrom):
    def clean_name(self):
        return self.cleaned_data.get("name")
