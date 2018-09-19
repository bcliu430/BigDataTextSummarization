import requests
import os
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from functools import partial
from glob import glob
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

from constants import API_URL, PDF_EXTENSION
from utils import verboseprint


def get_pdfs(directory):
    return glob(os.path.join(directory, PDF_EXTENSION))


def extract_full_text(pdf_file):
    response = requests.post(
        API_URL, files=dict(input=open(pdf_file, 'rb').read()))
    return response.text


def process_xml(text):
    soup = BeautifulSoup(text, "lxml")
    texts = soup.find_all(['p'])
    raw_text = '\n\n'.join([text.text for text in texts])
    return raw_text, str(soup)


def write_output(xml_text, raw_text, input_file, output_dir):
    base_filename = os.path.basename(input_file)
    text_output_file = os.path.join(output_dir, f'{base_filename}.txt')
    xml_output_file = os.path.join(output_dir, f'{base_filename}.xml')
    verboseprint(f"Text output file for {input_file} is {text_output_file}")
    verboseprint(f"XML output file for {input_file} is {xml_output_file}")
    with open(text_output_file, 'w') as fwriter:
        fwriter.write(raw_text)
    with open(xml_output_file, 'w') as fwriter:
        fwriter.write(xml_text)


def parse_pdf(pdf_file, output_dir):
    verboseprint(f"Parsing PDF {pdf_file}")
    text = extract_full_text(pdf_file)
    raw_text, xml_text = process_xml(text)
    write_output(xml_text, raw_text, pdf_file, output_dir)


def parse_pdfs(pdf_files, output_dir, num_processes=cpu_count()):
    parse_pdf_partial = partial(parse_pdf, output_dir=output_dir)
    with Pool(num_processes) as pool:
        with tqdm(total=len(pdf_files)) as pbar:
            for i, _ in tqdm(
                    enumerate(
                        pool.imap_unordered(parse_pdf_partial, pdf_files))):
                pbar.update()


def main():
    parser = ArgumentParser("GROBID CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pdf-file", help="Path to PDF File")
    group.add_argument("--directory", help="Path to directory with PDF files")
    parser.add_argument("--proc", help="Number of processes to use")
    parser.add_argument(
        "--output", help="Path to output directory", required=True, type=int)
    args = parser.parse_args()
    if args.pdf_file:
        parse_pdf(args.pdf_file, args.output)
    else:
        pdf_files = get_pdfs(args.directory)
        if args.proc:
            parse_pdfs(pdf_files, args.output, args.proc)
        else:
            parse_pdfs(pdf_files, args.output)


if __name__ == "__main__":
    main()
