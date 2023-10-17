import math
def paint_calc(height,width,cover):
    num_of_can=math.ceil((test_h*test_w)/coverage)
    print(f"You'll need {num_of_can} cans of paint.") 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)