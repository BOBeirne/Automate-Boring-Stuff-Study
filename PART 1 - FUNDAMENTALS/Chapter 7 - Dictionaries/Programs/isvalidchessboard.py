STARTING_PIECES = {'a8' : 'bR',
						'b8' : 'bN',
						'c8' : 'bB',
						'd8' : 'bQ',
						'e8' : 'bK',
						'f8' : 'bB',
						'g8' : 'bN',
						'h8' : 'bR',
						'a7' : 'bP',
						'b7' : 'bP',
						'c7' : 'bP',
						'd7' : 'bP',
						'e7' : 'bP',
						'f7' : 'bP',
						'g7' : 'bP',
						'h7' : 'bP',
						'a1' : 'wN',
						'b1' : 'wR',
						'c1' : 'wB',
						'd1' : 'wQ',
						'e1' : 'wK',
						'f1' : 'wB',
						'g1' : 'wN',
						'h1' : 'wR',
						'a2' : 'wP',
						'b2' : 'wP',
						'c2' : 'wP',
						'd2' : 'wP',
						'e2' : 'wP',
						'f2' : 'wP',
						'g2' : 'wP',
						'h2' : 'wP',
						}

def are_colors_valid(chessboard):
	WP = 0 # max 16 pieces for white
	BP = 0 # max 16 pieces for black
	for pieces_str in chessboard.values():
		pieces = pieces_str.strip()
	
		if pieces[0] == 'b':
			BP += 1                    
		elif pieces[0] == 'w':
			WP += 1
		else:
			return False, 0, 0
	return True, BP, WP
	
def are_counts_valid(Black, White):
	if White <= 16 and Black <= 16:
		return True
	else: 
		return False    
	
def are_kings_valid(chessboard):
	BK = 0 # max 1 piece and only one piece
	WK = 0 # same as above
	for pieces in chessboard.values():
		if pieces == 'bK':
			BK += 1
		elif pieces == 'wK':
			WK += 1 
	if BK == 1 and WK == 1:
		return True           
	else:
		return False
	
def are_pawns_valid(chessboard):
	BP = 0 # has to have 8 pawns
	WP = 0 # same as above
	for pieces in chessboard.values():
		if pieces == 'bP':
			BP += 1
		elif pieces == 'wP':
			WP += 1 
	if BP <= 8 and WP <= 8:
		return True           
	else:
		return False

def are_positions_valid(chessboard):
	rows = '12345678'
	columns = 'abcdefgh'
	for position in chessboard.keys():
		if len(position) != 2:
			return False
		elif position[1] not in rows:
			return False
		elif position[0] not in columns:
			return False 
	return True


def is_valid_chessboard(chessboard):
	if not are_colors_valid(chessboard):
		return False
	if not are_counts_valid(BP, WP):
		return False
	if not are_kings_valid(chessboard):
		return False
	if not are_pawns_valid(chessboard):
		return False
	if not are_positions_valid(chessboard):
		return False
	return True
		
		
valid_colors, BP, WP = are_colors_valid(STARTING_PIECES)
if valid_colors:
	print("Piece colors are valid.")
else: 
	print("The board has pieces with invalid colors.")
	
valid_counts = are_counts_valid(BP, WP)
if valid_counts:
	print("Black pieces found: %s" % (BP,))
	print("White pieces found: %s" % (WP,))
else:
	print("Invalid counts.")
	
valid_kings = are_kings_valid(STARTING_PIECES)
if valid_kings:
	print('Kings are valid')
else:
	print('Invalid Kings')  
	
valid_pawns = are_pawns_valid(STARTING_PIECES)
if valid_pawns:
	print('pawns are valid')
else:
	print('pawns are invalid!')

valid_positions = are_positions_valid(STARTING_PIECES)
if valid_positions:
	print('positions are valid')
else: 
	print('Invalid positions!')    
	
valid_chessboard = is_valid_chessboard(STARTING_PIECES)
if valid_chessboard:
	print('Chessboard is valid')
else:
	('Invalid chessboard')
	
	