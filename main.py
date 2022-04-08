from state import *
from utils import *
import options as opts

from InquirerPy import prompt

def main():
    opts.copyOver()
def cleanup():
    state["infoFile"].close()

main()
cleanup()
