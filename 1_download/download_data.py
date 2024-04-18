import pathlib
import requests
import argparse

def go(args):
    # Derive the base name of the file from the URL
    url = args.file_url
    basename = 'data' if args.file_name else pathlib.Path(url).name.split("?")[0].split("#")[0]
    response = requests.get(url)
    with open(f'{basename}', mode="wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a file and upload it as an artifact to W&B", fromfile_prefix_chars="@"
    )
    parser.add_argument(
        "--file_url", type=str, help="URL to the input file", required=True
    )
    parser.add_argument(
        "--file_name", type=str, help="Name of the downloaded file to be saved", required=False
    )
    
    args = parser.parse_args()

    go(args)