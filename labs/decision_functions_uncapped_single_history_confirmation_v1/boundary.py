"""The actual executor control boundary, shared by real work and zero-fit mocks."""
from common import *
def run(out,start,work,expected):
    atomic(out/'EXECUTION_START.json',start);progress={'completed':0}
    try:
        axes=work(progress)
        atomic(out/'EXECUTION_TERMINAL.json',terminal(completed=progress['completed'],expected=expected,**axes))
    except BaseException as e:
        if not (out/'EXECUTION_TERMINAL.json').exists():atomic(out/'EXECUTION_TERMINAL.json',terminal(completed=progress['completed'],expected=expected,integrity='INCOMPLETE',numerical='UNRESOLVED',scientific='NOT_ESTABLISHED',reason=repr(e)))
        raise
