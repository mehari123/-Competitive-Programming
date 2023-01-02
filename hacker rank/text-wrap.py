import textwrap

def wrap(string, max_width):
    next1=max_width
    size=len(string)
    a=[]
    for start in range(0,len(string),max_width):
        a.append(string[start:start+max_width])
    return '\n'.join(a)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
