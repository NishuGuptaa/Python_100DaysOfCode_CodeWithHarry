import argparse
import requests

def download_file(url, local_filename):
    # if local_filename is None:
    # local_filename = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

parser.add_argument("url", help="URL of the file to download")
parser.add_argument("output", help="By which name do you want to save your file")

# parser.add_argument("-o", "--output", help="description of optional argument", default="default_value")

args = parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url, args.output)