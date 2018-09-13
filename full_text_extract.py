import requests
from argparse import ArgumentParser
from bs4 import BeautifulSoup


API_URL = "http://localhost:8080/api/processFulltextDocument"


def extract_full_text(pdf_file):
    response = requests.post(
        API_URL, files=dict(input=open(pdf_file, 'rb').read()))
    return response.text


def process_xml(text):
    soup = BeautifulSoup(text, "lxml")
    texts = soup.find_all(['p'])
    raw_text = '\n\n'.join([text.text for text in texts])
    return raw_text, str(soup)


def write_output(xml_text, raw_text, output_file):
    text_output_file = output_file + '.txt'
    xml_output_file = output_file + '.xml'
    with open(text_output_file, 'w') as fwriter:
        fwriter.write(raw_text)
    with open(xml_output_file, 'w') as fwriter:
        fwriter.write(xml_text)


def main():
    parser = ArgumentParser("GROBID CLI")
    parser.add_argument("--pdf-file", help="Path to PDF File", required=True)
    parser.add_argument("--output", help="Path to Output File", required=True)
    args = parser.parse_args()
    text = extract_full_text(args.pdf_file)
    raw_text, xml_text = process_xml(text)
    write_output(xml_text, raw_text, args.output)


if __name__ == "__main__":
    main()
