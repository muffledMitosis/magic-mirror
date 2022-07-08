from distutils.util import execute
from email import message
import os
from random import choices
from utils import *
from state import *

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

def writeFolderStructure(destination=state["info"]["destination"]):
	for folder in state["info"]["folders"]:
		path = os.path.join(destination, folder["name"])
		os.mkdir(path)
		if "children" in folder:
			for child in folder["children"]:
				cp = os.path.join(path, child["name"])
				os.mkdir(cp)

def copyOver():
	dest = state["info"]["destination"]
	src = state["info"]["source"]

	folderToUse = inquirer.select(
		message="Select a folder",
		choices=(x["name"] for x in state["info"]["folders"]),
		default=None,
	).execute()

	childToUse = False
	children = False

	for folder in state["info"]["folders"]:
		if (folder["name"] == folderToUse) and "children" in folder:
			children = (x["name"] for x in folder["children"])
	
	if children:
		childToUse = inquirer.select(
			message="Selec subfolder",
			choices=children,
			default=None,
		).execute()
		
	tmp = f"/{childToUse}" if childToUse else ""
	finalSubPath = f"{folderToUse}{tmp}"

	stuffSelection = os.listdir(f"{src}/{finalSubPath}")
	
	moveOverChoices = inquirer.checkbox(
		message="Select stuff to move over",
		choices=stuffSelection,
		cycle=True
	).execute()

	for choice in moveOverChoices:
		