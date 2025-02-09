#Day 78: Download Files


#Create a script to download files from a website.

import requests

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

# Example usage
file_url = "https://example.com/sample.pdf"  # Replace with actual file URL
save_location = "sample.pdf"  # Change the filename if needed

download_file(file_url, save_location)
