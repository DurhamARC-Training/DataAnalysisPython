import zipfile
from urllib.request import urlopen
import io

if __name__ == '__main__':
    REPO = "https://github.com/DurhamARC-Training/DataAnalysisPython"
    BRANCH = "main"
    url = f"{REPO}/zipball/{BRANCH}"
    print(f"Downloading {url}...)")
    # urlopen allows us to access files on the internet
    with urlopen(url) as url_obj:
        # BytesIO to store zip in memory instead of writing to file on disk
        zip_content = io.BytesIO(url_obj.read())
    
    # extract zip file content
    with zipfile.ZipFile(zip_content) as zfile:
        zfile.extractall(".")
