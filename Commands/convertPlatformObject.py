import re

path = r""  # the path to the object to convert
regex = "public\s*([\w<>?\.]+)\s*([\w<>?\.]+)\s*{\s*get"

SearchFunction = re.compile(regex)
with open(path, 'r') as contentFile:
    content = contentFile.read()
matches = re.finditer(SearchFunction, content)

lines = []
result = ""
outputFile = open("result.txt", "w")
knownTypes = {'ComplexText': 'List<TranslatedText>', 'ComplexTextExt': 'List<TranslatedText>'}

for matchNum, match in enumerate(matches):
    matchNum += 1
    if len(match.groups()) >= 2:
        typeInputText = "Type : " + match.group(1) + (
            " (" + knownTypes[match.group(1)] + ")" if match.group(1) in knownTypes else "") + " > "
        typeInputDefault = knownTypes[match.group(1)] if match.group(1) in knownTypes else match.group(1)
        type = input(typeInputText) or typeInputDefault
        name = input("Name : " + match.group(2) + " > ") or match.group(2)
        output = "[DataMember(Name = \"" + re.sub(r"^(.)", lambda match: match.group(1).lower(), name) + "\")]\n"
        output += "[JsonProperty(NullValueHandling = NullValueHandling.Ignore)]\n"
        output += "public " + type + " " + name + " { get; set; }\n\n"
        result += output

        if not (match.group(1) in knownTypes):
            knownTypes[match.group(1)] = type

        print(output)
outputFile.write(result)
outputFile.close()
