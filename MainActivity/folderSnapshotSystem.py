import os
import json
import hashlib



# Generate the SHA-256 hash of a file by reading it in fixed-size chunks
def hash_file(fileLocation):
    create_sha256 = hashlib.sha256()

    # Read the file incrementally to avoid loading large files into memory
    with open(fileLocation, "rb") as file:
        while True:
            file_data_chunk = file.read(65536)

            if not file_data_chunk:
                break

            # Update the hash with the current chunk of file data
            create_sha256.update(file_data_chunk)

    # Return the final SHA-256 hash as a hexadecimal string
    return create_sha256.hexdigest()



# Create a snapshot of the folder by mapping each file to its SHA-256 hash
def snapShotCreate(folderLocation):
    snapShotDict = {}

    # Generate a hash for every file in the target directory
    for file in os.listdir(folderLocation):
        fileLocation = os.path.join(folderLocation, file)

        # Ignore subdirectories and process only regular files
        if os.path.isfile(fileLocation):
            snapShotDict[file] = hash_file(fileLocation)

    # Return the folder snapshot for future comparison
    return snapShotDict



# Save the current folder snapshot as a JSON file for future comparison
def snapShotSave(snapShotDict, fileName="snapshot.json"):
    with open(fileName, "w") as snapShotJson:
        json.dump(snapShotDict, snapShotJson, indent=3)


# Load a previously saved folder snapshot from a JSON file 
def snapShotLoad(fileName="snapshot.json"):
    with open(fileName, "r") as snapShotJson:
        return json.load(snapShotJson)
    

# Compare two folder snapshots to detect added, modified and deleted files
def snapShotCompare(prevFile, newFile):

    # Check for newly added or modified files
    for file in newFile:
        if file not in prevFile:
            print(f"{file} is a newly added file.")
        elif newFile[file] != prevFile[file]:
            print(f"{file} has got some modifications.")

    # Check for files that have been removed
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

