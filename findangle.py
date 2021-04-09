import math
def angle(ab:'int',bc:'int') ->'to_find_a_angle':
    x = math.atan2(ab,bc)
    x = round(math.degrees(x))
    x = str(x)+chr(176)
    return x
if __name__=="__main__":
    ab = int(input())
    bc = int(input())
    x = angle(ab,bc)
    print(x)
