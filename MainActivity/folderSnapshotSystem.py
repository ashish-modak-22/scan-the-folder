import os
import json
import hashlib


# Generate the SHA-256 hash of a file by reading it in fixed-size chunks
def hash_file(fileLocation):
    create_sha256 = hashlib.sha256()

    with open(fileLocation, "rb") as file:
        while True:
            file_data_chunk = file.read(65536)

            if not file_data_chunk:
                break
            create_sha256.update(file_data_chunk)

    return create_sha256.hexdigest()


def snapShotCreate(folderLocation):
    snapShotDict = {}

    for file in os.listdir(folderLocation):
        fileLocation = os.path.join(folderLocation, file)
        
        if os.path.isfile(fileLocation):
            snapShotDict[file] = hash_file(fileLocation)

    return snapShotDict


def snapShotSave(snapShotDict, fileName="snapshot.json"):
    with open(fileName, "w") as snapShotJson:
        json.dump(snapShotDict, snapShotJson, indent=3)


def snapShotLoad(fileName="snapshot.json"):
    with open(fileName, "r") as snapShotJson:
        return json.load(snapShotJson)
    

def snapShotCompare(prevFile, newFile):
    for file in newFile:
        if file not in prevFile:
            print(f"{file} is a newly added file.")
        elif newFile[file] != prevFile[file]:
            print(f"{file} has got some modifications.")

    for file in prevFile:
        if file not in newFile:
            print(f"{file} is deleted")


folderLocation = "testFolder"

newSnapShot = snapShotCreate(folderLocation)

if os.path.exists("snapshot.json"):
    prevSnapShot = snapShotLoad("snapshot.json")
    snapShotCompare(prevSnapShot, newSnapShot)
else:
    print("Previous snapshot is not found. New snapshot in progress...")

snapShotSave(newSnapShot)

print("Snapshot saved successfully.")

