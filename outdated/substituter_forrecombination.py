import sys
import re
for line in open(sys.argv[1], 'r'):
	linesp = line.strip().split()
	for idx in range(0, len(linesp)):
		if re.match('^\\./\\.', linesp[idx]) != None:
			linesp[idx] = '0'
		elif re.match('^0/1', linesp[idx]) != None:
			linesp[idx] = '1'
		elif re.match('^1/1', linesp[idx]) != None:
			linesp[idx] = '1'
		else:
			linesp[idx] = '1'
	print('\t'.join(linesp))
			
		
