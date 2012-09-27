import time

def mainloop():
	print "Hello World"
	time.sleep(1)
	print "\x1b[2J\x1b[H"
	
try:
	while True:
		mainloop()
except KeyboardInterrupt:
	print "\x1b[2J\x1b[H"
	print "\n"*10,"ByeBye"