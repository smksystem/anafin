from django import forms

class RTLoginForm(forms.Form):
	brokeid = forms.CharField(label="BrokeId",initial="013")
	username = forms.CharField(label="Username",initial="0147500")
	password = forms.CharField(label="Password")


class InitValCalForm(forms.Form):
	InitValue = forms.CharField(label='Initial Value',initial='10000')	