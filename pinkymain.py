# Django area to start web

import django
import sys
import os

sys.path.append('D:\workspace\anafin')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anafin.settings')

django.setup()


from pinkybot.monitor import pinkybot
# from pinkybot.packsel import packselenium

LoginParams={
					"myuser":"0147500",
					"mypassword":"25191976",
					"mybrokeId":"013",
					}

login= pinkybot()
login.mypinkylogin(LoginParams)

try:

	while True:
		passb
except KeyboardInterrupt:
	pass

