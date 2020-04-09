import functools

def track(arglist):
    def cacheargs(f):
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in arglist:
                print(key, 'found in cache')
                return arglist[key]
            else:
                wrapper.count += 1
                fval = f(*args, **kwargs)
                arglist[key] = fval
                return fval
        wrapper.count = 0
        return wrapper
    return cacheargs

def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logfile = open('log.txt','a')
        key = str(args) + str(kwargs)
        wrapper.count += 1
        fval = f(*args, **kwargs)
        towrite = 'fib(' + str(key) + ')= ' + str(fval) + '\n'
        logfile.write(towrite)
        return fval
    wrapper.count = 0
    return wrapper

theargs = {}
@track(theargs)
@log
def fib(n):
    #print('running fib with', n)
    if n in (0,1):
        #print('returning ', n)
        return n 
    else:
        m = fib(n-1) + fib(n-2)
        #print((n-1),(n-2))
        #print('returning ', m)
        return m


print(fib(10))
print(fib.count)
print(theargs)
