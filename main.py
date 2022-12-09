import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="Enter pdf file name")
parser.add_argument("-w", "--word", type=str, help="Enter word you want to search")
args = parser.parse_args()

pdf = PdfFileReader(args.file)
output_file = 'output.txt'
word = args.word


def read_pdf(output_file: str) -> None:
    """Read pdf file and write to output.txt file."""
    with open(output_file, 'w') as f:
        for page_num in range(pdf.numPages):
            pageObj = pdf.getPage(page_num)
            try:
                content = pageObj.extractText()
                f.write(content)
            except Exception as e:
                print(f"[-] Error: {e}")
                raise e

    return content


def search_word(word: str) -> None:
    """Search for word in output file"""
    count: int = 0
    with open(output_file, "r") as file:
        for line_number, line in enumerate(file, start=1):  
            if word in line:
              count += 1
    print(f"Word '{word}' found {count} number of times")


def clean_up():
    """Delete output.txt file."""
    if not os.path.isfile(output_file):
        print("[-] Temp file output.txt does not exist...")
    # os.remove(output_file)


read_pdf(output_file)
search_word(word)
clean_up()

