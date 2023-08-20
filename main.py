class Meta(type):
    def __new__(cls, name,base,attrs):
        attrs.update({"Solid":1,"Kovid":2})
        return type.__new__(cls,name,base,attrs)
class Point(metaclass=Meta):
    def get_data(self):
        return (0,0)

pt = Point()
print(pt.Solid)