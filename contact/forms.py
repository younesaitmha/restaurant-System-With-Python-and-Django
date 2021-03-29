from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
