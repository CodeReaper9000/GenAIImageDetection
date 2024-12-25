import requests
import os

# Define the selected directories and subfolder
selected_dirs = {
    "D01_Samsung_GalaxyS3Mini",
    "D02_Apple_iPhone4s",
    "D03_Huawei_P9",
    "D19_Apple_iPhone6Plus",
    "D24_Xiaomi_RedmiNote3",
    "D27_Samsung_GalaxyS5"
}
valid_subfolder = "natFBH"
valid_extensions = {".jpg", ".png"}

# Read the URLs from the text file
with open(r"D:\downloads\urls.txt", "r") as file:
    urls = file.readlines()

# Filter URLs based on the criteria
filtered_urls = []
for url in urls:
    url = url.strip()

    # Check if URL matches selected directories
    if any(f"/{d}/" in url for d in selected_dirs):
        print(f"  Matches a selected directory: {url}")

        # Check if URL is in the correct subfolder (natFBH)
        if f"/{valid_subfolder}/" in url:
            print(f"  Matches the subfolder 'natFBH': {url}")

            # Check if URL ends with a valid image extension
            if any(url.endswith(ext) for ext in valid_extensions):
                print(f"  Matches valid file extension: {url}")
                filtered_urls.append(url)
            else:
                print(f"  Does not match a valid file extension: {url}")
        else:
            print(f"  Does not match the subfolder 'natFBH': {url}")
    else:
        print(f"  Does not match a selected directory: {url}")

# Download the filtered files
os.makedirs(r"D:\downloads\camera", exist_ok=True)
for url in filtered_urls:
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.join(r"D:\downloads\camera", os.path.basename(url))
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {e}")