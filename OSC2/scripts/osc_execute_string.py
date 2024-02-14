# me - this DAT.
# 
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.
def safeCast(cell):
	try:
		val = float(cell)
	except ValueError:
		val = str(cell)
		#print(val)
	return val
source = op('out1')
def row_to_osc(row):
	out = op('oscres').sendOSC(source[row, 0].val, [str(source[row,1].val)])
	#print('a')
	#print(row)
	return out


def onTableChange(dat):
	return

def onRowChange(dat, rows):
	for row in range(source.numRows):
		row_to_osc(row)

		#print(x)
		#print('/'+source[row, 0], source[row,1])
	return

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	return

def onSizeChange(dat):
	return
	