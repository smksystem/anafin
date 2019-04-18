import logging

class mylog():
	def __init__(self):



		formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s')

		console = logging.StreamHandler()
		console.setFormatter(formatter)

		myconsole = logging.getLogger("console")
		myconsole.setLevel(logging.DEBUG)
		myconsole.addHandler(console)
		
		
		# handler = logging.handlers.RotatingFileHandler(
  #             LOG_FILENAME, maxBytes=20, backupCount=5)

  		# default is a append , w is for overwritten
		fh = logging.FileHandler('applog.log',mode='w')
		fh.setFormatter(formatter)

		applog = logging.getLogger(__name__)
		applog.setLevel(logging.DEBUG)
		applog.addHandler(fh)


		self.log={"applog":applog,
				"console":myconsole,
				}


