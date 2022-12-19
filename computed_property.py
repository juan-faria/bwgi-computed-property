from functools import wraps, update_wrapper

class computed_property(object):

    def __init__(self, *args, **kwargs):
        self.arg_keys = []
        for arg in args:
            self.arg_keys.append(arg)

    def __get__(self, obj, objcls):
        @wraps(self.func)
        def wrapper (obj):
            computed_property_name = "computed_property_" + self.func.__name__

            #if has chached value
            if (computed_property_name in obj.__dict__.keys()):
                for key in self.arg_keys:
                    if (key in obj.__dict__.keys()):
                        #if change has happened on any observed key
                        if(obj.__dict__["old_" + str(key)] != obj.__dict__[key]):
                            self._update_old_values(obj)
                            obj.__dict__[computed_property_name] = self.func(obj)
                            return obj.__dict__[computed_property_name]
                    continue
                return obj.__dict__[computed_property_name]

            self._update_old_values(obj)
            #writes on obj itself to avoid garbage collector references on decorator
            obj.__dict__[computed_property_name] = self.func(obj)
            return obj.__dict__[computed_property_name]
        self.__doc__ = self.func.__doc__
        return wrapper(obj)
    
    def _update_old_values(self, obj):
        for key in self.arg_keys:
            try:
                obj.__dict__["old_" + str(key)] = obj.__dict__[key]
            except(KeyError):
                #ignores if key is set on computed_property argument but not on the object itself
                obj.__dict__["old_" + str(key)] = None

    def __set__(self, obj, value):
        return self.__setter(obj, value)
    
    def __delete__(self, obj):
        return self.__deleter(obj)
    
    def __call__(self, func):
        self.func = func
        return self
    
    def setter(self, setter):
        self.__setter = setter
        return self

    def deleter(self, deleter):
        self.__deleter = deleter
        return self
