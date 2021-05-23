from pathlib import Path
from typing import Iterator

def lines(file_location: str) -> str:
    file = file_location.open()
    for i in file:
        yield i

def parse_csv(source: Iterator[str]) -> Iterator[str]:
    for x in source:
        yield x.rstrip().split(" = ") # deleting \n and separating by " = "

def dictionary(file):
    empty   = {}
    line    = lines(file)
    parsed  = parse_csv(line)
    for e_list in parsed:
        if e_list != ['']:
            key = e_list[0]
            value = e_list[1]
            empty[key] = value
    return empty

def write(input, output):
    o = open(output, "w")
    o.write("Citizen.CreateThread(function()\n")
    i = dictionary(input)
    for key in i:
        o.write("    AddTextEntryByHash(" + str(key) + ", " + '"{}"'.format(str(i[key])) + ")\n")
    o.write("end)")
    o.close

script_location = Path(__file__).absolute().parent
input = script_location / 'insert_your_gtx2_text_here.txt'
output = script_location / 'names.lua'
write(input, output)