import requests
import os
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from functools import partial
from glob import glob
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

from constants import API_URL, PDF_EXTENSION


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
    text_output_file = '%s.%s' % (input_file, 'txt')
    xml_output_file = '%s.%s' % (input_file, 'xml')
    with open(text_output_file, 'w') as fwriter:
        fwriter.write(raw_text)
    with open(xml_output_file, 'w') as fwriter:
        fwriter.write(xml_text)


def parse_pdf(pdf_file, output_dir):
    text = extract_full_text(pdf_file)
    raw_text, xml_text = process_xml(text)
    write_output(xml_text, raw_text, pdf_file, output_dir)


def parse_pdfs(pdf_files, output_dir):
    parse_pdf_partial = partial(parse_pdf, output_dir=output_dir)
    with Pool(cpu_count()) as pool:
        with tqdm(total=len(pdf_files)) as pbar:
            for i, _ in tqdm(
                    enumerate(
                        pool.imap_unordered(parse_pdf_partial,
                                            pdf_files))):
                pbar.update()


def main():
    parser = ArgumentParser("GROBID CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pdf-file", help="Path to PDF File")
    group.add_argument("--directory", help="Path to directory with PDF files")
    parser.add_argument(
        "--output", help="Path to output directory", required=True)
    args = parser.parse_args()
    if args.pdf_file:
        parse_pdf(args.pdf_file, args.output)
    else:
        pdf_files = get_pdfs(args.directory)
        parse_pdfs(pdf_files, args.output)


if __name__ == "__main__":
    main()
