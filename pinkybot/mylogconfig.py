import logging

class mylog():
	def __init__(self):



		formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s')

		console = logging.StreamHandler()
		console.setFormatter(formatter)

		myconsole = logging.getLogger("console")
		myconsole.setLevel(logging.DEBUG)
		myconsole.addHandler(console)
		
		fh = logging.FileHandler('applog.log')
		fh.setFormatter(formatter)

		applog = logging.getLogger(__name__)
		applog.setLevel(logging.INFO)
		applog.addHandler(fh)


		self.log={"applog":applog,
				"console":myconsole,
				}


