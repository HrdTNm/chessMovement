# chessMovement
A Python module that can detect and display chess movement by two-dimensional array. (I'm a student and new to python, if there are any errors in my module, pls tell me)
 


The functions includes in this module:

1.createBoard(): Create a chessboard and return a two-dimensional array representing the board, e.g.: [['BRook', 'BKnight', 'BBishop', 'BQueen', 'BKing', 'BBishop', 'BKnight', 'BRook'], ['BPawn', 'BPawn', 'BPawn', 'BPawn', 'BPawn', 'BPawn', 'BPawn', 'BPawn'], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['WPawn', 'WPawn', 'WPawn', 'WPawn', 'WPawn', 'WPawn', 'WPawn', 'WPawn'], ['WRook', 'WKnight', 'WBishop', 'WKing', 'WQueen', 'WBishop', 'WKnight', 'WRook']], where "B" represents black and "W" represents white.

2.checkPlace(Board, Piece): The Board variable is a two-dimensional array representing the chessboard (created by the createBoard() function), and the Piece variable is a string representing the type of chess piece (possible values: "Pawn", "Rook", "Bishop", "Knight", "Queen", "King"). It will return a two-dimensional array containing the coordinates of the chess pieces, with the first half representing the black pieces and the second half representing the white pieces, e.g.: [[10, 11, 12, 13, 14, 15, 16, 17], [60, 61, 62, 63, 64, 65, 66, 67]].

3.pawnMovement(Board, Colour, Place): The Board variable is as described above. The Colour variable is an integer that can take values 0 or 1, where 0 represents black and 1 represents white. The Place variable represents the coordinates of the chess piece, such as 3 (fourth square in the first row) or 72 (third square in the eighth row) (note that Place has a maximum value of 77 and a minimum value of 0, and the units digit cannot exceed 7). This function will return a one-dimensional array representing all the reachable positions on the chessboard for the given pawn, e.g.: [21, 31].

4.rookMovement(Board, Colour, Place): Similar to pawnMovement, but it checks the movement of a rook.

5.bishopMovement(Board, Colour, Place): Similar to pawnMovement, but it checks the movement of a bishop.

6.queenMovement(Board, Colour, Place): Similar to pawnMovement, but it checks the movement of a queen. It returns a two-dimensional array, where the upper half represents horizontal and vertical movements, and the lower half represents diagonal movements, e.g.: [[35, 36, 37, 33, 32, 31, 30, 44, 54, 64, 24], [45, 56, 67, 23, 43, 52, 61, 25]].

7.knightMovement(Board, Colour, Place): Similar to pawnMovement, but it checks the movement of a knight.

8.kingMovement(Board, Colour, Place): Similar to pawnMovement, but it checks the movement of a king.

9.pieceMovement(Board, P1, P2): P1 and P2 are standard coordinates used in chess notation (e.g., a2, b5). Board is a two-dimensional array created by the createBoard() function. This function combines the functionality of the previous six functions. It returns True if the chess piece at position P1 can move to position P2, and False otherwise.

10.kingCanNotGo(Board, Colour): Board is a two-dimensional array created by the createBoard() function, and Colour indicates the color to be checked (an integer value of 0 or 1, where 0 represents black and 1 represents white). This function returns a one-dimensional array indicating the areas where the king of the specified color cannot move to (i.e., moving to those areas would result in check).

11.checkKing(Board, Colour): Board is a two-dimensional array created by the createBoard() function, and Colour indicates the color to be checked. This function returns a boolean value indicating whether the king of the specified color is in check.

12.castling(Board, P1, P2): This function checks whether the pieces P1 and P2 on the chessboard Board (created by the createBoard() function) can perform a castling move. P1 and P2 are the coordinates of the two pieces, with both the tens and units digits ranging from 0 to 7. It returns a boolean value.

13.pieceMove(Board, P1, P2, C): P1 and P2 are standard coordinates used in international chess notation (e.g., a1, b3). Board is the chessboard created by the createBoard() function. C is same as the variable Colour showed ahead. This function first checks if the colour is right, then check the check king (if the king is in check, it returns "Move your king first"), then checks if the chess piece at P1 can move to position P2 (if not, it returns "Can't move"). If the move is valid, it returns a modified two-dimensional array (Board) representing the updated positions of the chess pieces.

14.hasValidMoves(Board, Colour): Board and Colour are defined as above. This function returns a boolean value. If there are still valid moves for the pieces of the specified color (i.e., no move would result in the king being in check), it returns True; otherwise, it returns False.

15.pawnChange(Board, Colour, Place, Kind): Board, Colour, and Place are defined as above. Kind represents the type of chess piece (possible values: "Pawn", "Rook", "Bishop", "Knight", "Queen", "King"). This function promotes a pawn to a chess piece of the specified Kind if the pawn has reached the opponent's baseline. If the chess piece at Place is not a pawn or has not reached the opponent's baseline, no changes are made. It returns the modified chessboard (Board) after the pawn promotion.

16.gameSituation(Board): Board are defined as above。Show the chess situation at this time，Its possible returns are”White wins”, ”Black wins”, ”Draw” , ”Continue”
