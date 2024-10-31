""" Mutable arguments """
from datetime import datetime
from random import randint
from dataclasses import dataclass
from pydantic import BaseModel, Field


# default argument are interpreted at compiling time 
def defaut_args_list(data: list = []):
    data.append(1)
    return data

def defautl_arg_dict(data: dict = {}):
    data[randint(1, 1000)] = randint(1, 1000)
    return data


class DefaultValues(BaseModel):
    a :list = [] # pydantic handle this automaticly by making a deep copy of [] and it's not the same case of dataclass
    b: datetime = datetime.now() # in this case is interpreted at compiling time so in all instances it's gonna be the same value
    c: datetime = Field(default_factory= lambda: datetime.now()) # that's the best practice to do not 


if __name__ == '__main__':
    print('testing default list argument')
    l = defaut_args_list()
    print(l)
    l = defaut_args_list()
    print(l)

    print('testing default list dict')
    d = defautl_arg_dict()
    print(d)
    d = defautl_arg_dict()
    print(d)

    print('testing default value list and calculated value')
    default_value1 = DefaultValues()
    print(default_value1.a, default_value1.b, default_value1.c)
    default_value2 = DefaultValues()
    print(default_value2.a, default_value2.b, default_value2.c)
    default_value3 = DefaultValues()
    print(default_value3.a, default_value3.b, default_value3.c)
