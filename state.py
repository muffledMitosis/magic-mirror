import json

infoFile = open('./info.json')
info = json.load(infoFile)

state = {
	"infoFile": infoFile,
	"info": info
}