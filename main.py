from state import *
from utils import *
import options as opts

from InquirerPy import prompt

# questions = [
#     {"type": "input", "message": "What's your name:", "name": "name"},
#     {"type": "confirm", "message": "Confirm?", "name": "confirm"},
# ]
# result = prompt(questions)
# name = result["name"]
# confirm = result["confirm"]

def main():
	opts.writeFolderStructure()
def cleanup():
	state["infoFile"].close()

main()
cleanup()
