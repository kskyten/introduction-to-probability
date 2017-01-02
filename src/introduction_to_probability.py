from plasTeX import Command, Environment

class putfig(Command):
    args = 'arg1 arg2 arg3'

class emx(Command):
    args = 'self'

class example(Environment):
    args = '( title:str )'
    labelable = True
    # def invoke(self, tex):
    #     Environment.invoke(self, tex)

class definition(Environment):
    args = '( title:str )'
    labelable = True

class theorem(Environment):
    args = '( title:str )'
    labelable = True

class corollary(Environment):
    args = '( title:str )'
    labelable = True
