import os
import pathlib
import shutil

downloads_folder_path = "/Users/pc/Downloads"

# Reads all the files inside this directory
downloads_files = os.listdir(downloads_folder_path)

global_file_extension = []
global_files = []
# These folders will be added automatically if they not exist inside the "Downloads" folder
required_folders = ["Images", "Audio", "Video", "Docs", "Apps"]
existing_folders = []
        

# Get all the extensions of the global files inside the Download folder
for ext in downloads_files:
    suffixes = pathlib.Path(ext).suffix

    # To avoid Folders
    if suffixes != "":
        global_file_extension.append(suffixes)
        global_files.append(ext)
    else:
        existing_folders.append(ext)

# Creates the required folders inside the Downloads folder
def createRequiredFolders(folder):
    os.mkdir(f"{downloads_folder_path}/{folder}")

    print(f"{folder} created!")


# checks if there's any required folders in the existing folders
for folder in required_folders:
    if folder not in existing_folders:
        createRequiredFolders(folder)
    else:
        if folder in existing_folders:
            print(f"{folder} already exists!")
        else:
            createRequiredFolders(folder)


images_extensions = ["jpg", "jpeg", "gif", "png", "svg", "tiff", "bmp", "jfif"]
audio_extensions = ["mp3", "wav", "aiff"]
video_extensions = ["mp4", "mov", "avi", "wmv", "mkv", "flv"]
docs_extensions = ["doc", "docx", "html", "pdf", "odt", "xls", "xlsx", "ppt", "pptx"]
apps_extension = ["exe", "bat", "com", "run"] # This one is for executable files(installer)


# moves to files to a folder based on their extension
def filterFiles(extensions, path, debug_mssg):
    for file in downloads_files:
        for ex in extensions:
            # Gets the extension of all the global files inside 'Downloads'
            suffixes = pathlib.Path(file).suffix

            if f".{ex}" == suffixes:
                # move from a directory to another
                shutil.move(f"{downloads_folder_path}/{file}", f"{downloads_folder_path}/{path}/{file}")
                print(debug_mssg)


filterFiles(images_extensions, "Images", "All Images were moved to 'Images' folder")
filterFiles(audio_extensions, "Audio", "All Audios were moved to 'Audio' folder")
filterFiles(video_extensions, "Video", "All Videos were moved to 'Videos' folder")
filterFiles(docs_extensions, "Docs", "All Docs were moved to 'Docs' folder")
filterFiles(apps_extension, "Apps", "All Executable files were moved to 'Apps' folder")