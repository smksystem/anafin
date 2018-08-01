from django import forms

class EmailForm(forms.Form):
	brokeid = forms.CharField(label="BrokeId",initial="013")
	username = forms.CharField(label="Username",initial="0147500")
	password = forms.CharField(label="Password")
	