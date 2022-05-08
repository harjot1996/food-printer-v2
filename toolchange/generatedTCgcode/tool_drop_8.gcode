G28 U0 F1000;;
G01 Z160 F1000; retract z to some high position
G01 X364.1 Y50 F1000; get in front of proper tool post
G01 Y15 F1000; set the correct y height in front of tool post 8
G01 Y14 Z159 F1000; move diagonallly downwards in Y and Z direction
G01 Y11 Z155.5 F1000; move diagonallly downwards in Y and Z direction
G01 Z143.5 F1000; set the correct z height in front of tool post by moving back up
G01 Y50 F1000; move back in the y direction from the tool post 8
