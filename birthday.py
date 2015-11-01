"""
<3 Dan
Have a Great Day!
happy {0[1]}th birthday {0[0]}
"""

def birthday():	
	leigh = int(__doc__[-6])
	while True:
		leigh += int(__doc__[-22])
		if leigh == ord("\x1E"):
			print chr(len(__doc__.split(
				))).join(__doc__.split(
				chr(len(__doc__.split(
				))))[::-1]).format(
				*locals().items())
			break
birthday()