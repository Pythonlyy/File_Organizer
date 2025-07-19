import os  # lets us work with folders and files
import shutil  # used to move files from one place to another

# 👇 Change this path to the folder you want to clean up
FOLDER_TO_ORGANIZE = "/Users/yourusername/Downloads"

# 🗂️ This dictionary groups file types by category
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# 🧹 This function does the organizing
def organize_folder(folder_path):
    # 🔁 Go through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # ✅ Check if it's a file (and not a folder)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()  # get the file extension
            moved = False  # track if the file has been moved

            # 🔍 Check which category the file belongs to
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    # 🗃️ Create the category folder if it doesn't exist
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)

                    # 🚚 Move the file into the category folder
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} → {category}/")
                    moved = True
                    break  # stop checking once it's moved

            # ❓ If the file doesn't match any known type, put it in "Others"
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved: {filename} → Others/")

# 🚀 Run the function
organize_folder(FOLDER_TO_ORGANIZE)
