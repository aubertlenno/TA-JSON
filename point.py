class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

def get_json_str(p):
    jstr = {
        "__class__" : type(p).__name__,
        "x" : p.getX(),
        "y" : p.getY()
    }
    return jstr

def read_json_str(a,b):
    s1 = int(a)
    s2 = int(b)
    g = Point(s1,s2)
    return g

def main():
    p = Point(1,2)
    z = get_json_str(p)
    print(z)

    r = read_json_str(2,1)
    m = get_json_str(r)
    print(m)

main()