import sys
def require(modules):
    missing=[]
    modules=list(modules)
    for i in modules:
        if (i in sys.modules):
            pass
        else:
            missing.append(i)
    if 0 < len(missing) < 2:
        statement="\nYou are missing the following modules: "+'%s'*len(missing)+ '.\n'
        print(statement%tuple(missing))
        return False
    if 1 < len(missing):
        statement="\nYou are missing the following modules: "+'%s, '*(len(missing)-1)+ '%s.\n'
        print(statement%tuple(missing))
        return False
    if len(missing)==0:
        print('\nAll required modules installed\n')
        return True

#program will return False if missing module

#if require.require([modules]) is False:
#    sys.exit()
