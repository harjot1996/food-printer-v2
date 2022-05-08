G28 U0 F1000;
G01 Z143.5 F1000; move towards tool post
G01 X364.1 Y50 F1000; get near tool post 8
G01 Y15 F1000; engage magnets with new tool
G01 Z158.5 F1000; move upward and pull tool off of post
G01 Y50 F1000; move away from tool post with new tool
G01 Z158.5 F1000; force upward movement to ensure there's no contact with walls
