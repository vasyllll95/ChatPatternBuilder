
from message import Message
from pattern import Pattern

# TODO: add tests

if __name__=='__main__':
    m=Message("z a d f a b c")
    p=Pattern(m)
    print(p.volley)