#!/usr/bin/python
import sys

# highlights a string with the given color
def highlight(text = ' *** ', fg = None, bg = None):
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

	if bg is None: # print a fg and blank bg
		return '\033[%dm%s\033[0m' % (fg_esc, text)

	if fg is None: # print a bg as a fg
		return '\033[%dm%s\033[0m' % (bg_esc - 10, text)

	# print a fg and bg
	return '\033[%dm\033[%dm%s\033[0m' % (fg_esc, bg_esc, text)

def print_short():
	print ''

	for f in range(3):
		row = '  '
		for b in range(8):
			row += highlight(text='    ', fg = b, bg = b)
			row += highlight(text='    ', fg = b + 8, bg = b + 8)
			row += '  '
		print row

	print ''

def print_palette():
	print ''

	row = ' '*5
	for b in range(8):
		row += highlight(text=' %2s ' % b, fg = b)
		row += highlight(text=' %2s ' % (b + 8), fg = b + 8)
		row += '  '
	print row

	row = ' '*5
	for b in range(8):
		row += highlight(text='    ', fg = b, bg = b)
		row += highlight(text='    ', fg = b + 8, bg = b + 8)
		row += '  '
	print row

	for f in range(16):
		row = highlight(text=' %2s  ' % f, fg = f)

		for b in range(8):
			row += highlight(text=' %2s ' % f, fg = f, bg = b)
			row += highlight(text=' %2s ' % f, fg = f, bg = b + 8)
			row += '  '
		print row

	print ''

def main(args):
	if len(args) == 0:
		print_palette()
	elif args[0] in ('-s', '--short'):
		print_short()
	else:
		print 'Usage: ./colors.py [-s|--short]'

if __name__ == '__main__':
	main(sys.argv[1:])
