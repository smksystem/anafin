import logging

class mylog():
	def __init__(self):

		print("initialize mylog")


		applog = logging.FileHandler('applog.log')
		# djangolog = logging.FileHandler('djangolog.log')
		self.applog = logging.getLogger(__name__)
		# self.djangolog = logging.getLogger(__name__)

		# self.applog.Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s')
		formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s')
		applog.setFormatter(formatter)

		# self.djangolog.addHandler(djangolog)
		self.applog.addHandler(applog)

		# self.djangolog.setLevel(logging.INFO)
		self.applog.setLevel(logging.DEBUG)
		# self.applog.setFormatter(formatter)





		# logging.basicConfig(filename='applog.log', filemode='w',format='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
  #   	datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG)

		# f_handler = logging.FileHandler('applog1.log')
		# self.logger = logging.getLogger(__name__)
		# # self.logger = logging.getLogger("mybot")
		# self.logger.addHandler(f_handler)

		# console = logging.StreamHandler()
		# console.setLevel(logging.INFO)
		# logging.getLogger('').addHandler(console)

		# self.logger1 = logging.getLogger('django.request')
		# self.logger1.setLevel(logging.INFO)






	# import logging

	# # set up logging to file - see previous section for more details
	# logging.basicConfig(level=logging.DEBUG,
	#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
	#                     datefmt='%m-%d %H:%M',
	#                     filename='/temp/myapp.log',
	#                     filemode='w')
	# # define a Handler which writes INFO messages or higher to the sys.stderr
	# console = logging.StreamHandler()
	# console.setLevel(logging.INFO)
	# # set a format which is simpler for console use
	# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	# # tell the handler to use this format
	# console.setFormatter(formatter)
	# # add the handler to the root logger
	# logging.getLogger('').addHandler(console)

	# # Now, we can log to the root logger, or any other logger. First the root...
	# logging.info('Jackdaws love my big sphinx of quartz.')

	# # Now, define a couple of other loggers which might represent areas in your
	# # application:

	# logger1 = logging.getLogger('myapp.area1')
	# logger2 = logging.getLogger('myapp.area2')

	# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
	# logger1.info('How quickly daft jumping zebras vex.')
	# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
	# logger2.error('The five boxing wizards jump quickly.')





# import logging

# # set up logging to file - see previous section for more details
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     filename='/temp/myapp.log',
#                     filemode='w')
# # define a Handler which writes INFO messages or higher to the sys.stderr

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)

# # set a format which is simpler for console use

# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# # tell the handler to use this format

# console.setFormatter(formatter)

# # add the handler to the root logger
# logging.getLogger('').addHandler(console)

# # Now, we can log to the root logger, or any other logger. First the root...
# logging.info('Jackdaws love my big sphinx of quartz.')

# # Now, define a couple of other loggers which might represent areas in your
# # application:

# logger1 = logging.getLogger('myapp.area1')
# logger2 = logging.getLogger('myapp.area2')

# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')


