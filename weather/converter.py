import xmltodict
import json

def main():
    print("Please make sure that your XML file is in the same folder as this program.\n")
    print("Enter your XML file name (make sure to include .xml at the end) : ", end='')
    xmlPath = input().strip()

    try:
        xmlFile = open(xmlPath)
    except:
        print("File not found, the program will now be closed")
        return

    xmlContent = xmlFile.read()
    buffer = xmltodict.parse(xmlContent, attr_prefix='')
    jsonContent = json.dumps(buffer, indent=4)

    print("Enter your intended JSON file name (make sure to include .json at the end) : ", end='')
    jsonPath = input().strip()
    jsonTarget = open(jsonPath, 'w+')
    jsonTarget.write(jsonContent)

main()