import os
import pathlib
from glob import glob
from argparse import ArgumentParser

from constants import PDF_EXTENSION
from full_text_extract import parse_pdfs
from utils import verboseprint


def create_directory(dirname):
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)


def fetch_pdfs(input_dir):
    return glob(os.path.join(input_dir, "**", PDF_EXTENSION), recursive=True)


def extract_text(input_dir, output_dir):
    pdf_files = fetch_pdfs(input_dir)
    create_directory(output_dir)
    parse_pdfs(pdf_files, output_dir)


def main():
    parser = ArgumentParser("PDF Processor to text")
    parser.add_argument(
        "--dir",
        help="Base directory for PDFs",
        required=False,
        default="../data/")
    parser.add_argument(
        "--output",
        help="Output directory for text and XML outputs",
        required=False,
        default="../data/parsed_text/")
    args = parser.parse_args()
    verboseprint(f"The input directory is {args.dir}")
    verboseprint(f"The output directory is {args.output}")
    extract_text(args.dir, args.output)

    
if __name__ == '__main__':
    main()
