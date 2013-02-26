#!/usr/bin/python

# highlights a string with the given color
def highlight(fg = None, bg = None):
	# adjust the fg color to the correct escape code
	if fg != None:
		if fg > 7:
			fg_esc = fg + 82
		else:
			fg_esc = fg + 30

	# adjust the bg color to the correct escape code
	if bg != None:
		if bg > 7:
			bg_esc = bg + 92
		else:
			bg_esc = bg + 40

	if bg == None: # print a fg and blank bg
		return '\033[%dm %2d/   \033[0m' % (fg_esc, fg)

	if fg == None: # print a bg as a fg
		return '\033[%dm   /%2d \033[0m' % (bg_esc - 10, bg)

	# print a fg and bg
	return '\033[%dm\033[%dm %2d/%2d \033[0m' % (fg_esc, bg_esc, fg, bg)

def print_palette(offset = 0):
	# header
	row = '       '
	for b in range(8):
		row += highlight(bg = b + offset)
	print row

	# palette
	for f in range(16):
		row = ''
		row += highlight(fg = f)
		for b in range(8):
			row += highlight(fg = f, bg = b + offset)
		print row

	print ''

def main():
	print_palette(0)
	print_palette(8)

if __name__ == '__main__':
	main()
