from django import forms

class CommentForm(forms.Form):
    # name = forms.CharField(max_length=200)
    comment = forms.CharField( widget = forms.widgets.Textarea())
    hidden_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    hidden_name = forms.CharField(required=True, widget=forms.HiddenInput())

class PostForm(forms.Form):
	title = forms.CharField();
	article = forms.CharField( widget = forms.widgets.Textarea())