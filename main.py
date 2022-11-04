import whisper
import json

#directories
jsout = "./output/"

#model options
verbose = False
language = "German"


def scribe(file):
    if filecheck(jsout + file + ".json"):
        return

    model = whisper.load_model("small")
    result = model.transcribe(file, verbose=verbose, language=language)
    with open(jsout + file + ".json", "w") as outfile:
        json.dump(result, outfile, indent=1)


def printfile(file):
    if not filecheck(jsout + file + ".json"):
        return

    with open(jsout + file + ".json") as json_file:
        data = json.load(json_file)
        segments = data["segments"]
        for i in range(len(segments)):
            segment = segments[i]
            print(segment["text"])



def filecheck(fn):
    try:
        open(fn, "r")
        return True
    except IOError:
        return False


if __name__ == '__main__':
    loop = True
    while loop:
        filename = input("Enter the filename: ")
        loop = not(filecheck(filename))
        if loop:
            print("Error: File does not appear to exist.\n")

    scribe(filename)
    printfile(filename)
