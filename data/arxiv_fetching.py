"""
This script is used for fetching papers from arxiv.org.
Use --help or -h flag to check help message.

Example Usage: 

python arxiv_fetching.py -e 9 -t ~/arxiv_pdfs/ -m arxivData.json

This will download first 10 pdfs. The metadata file can be downloaded from
https://www.kaggle.com/neelshah18/arxivdataset
"""

import os
import json
import argparse
import requests

IDX_MAX = 40999

def get_args():
    parser = argparse.ArgumentParser(description = 'Fetch papers from arxiv.org.')
    parser.add_argument('-s', type = int, default = 0,
                        help = 'starting index, counts from 0, default value is 0')
    parser.add_argument('-e', type = int, default = 0,
                        help = 'ending index, counts from 0, default value is 0, maximum value is 40999')
    parser.add_argument('-m', default = '../resources/arxivData.json',
                        help = 'position of the metadata file, default value is \'../resources/arxivData.json\'')
    parser.add_argument('-t', default = './arxiv_pdfs/',
                        help = 'target directory, downloaded pdfs are stored in this directory, \
                         default value is \'./arxiv_pdfs/\'')
    return parser.parse_args()

def get_titles_and_links(mj, s, e):
    titles_and_links = []
    for i in range(s, e+1):
        title = mj[i]['title']
        link = None
        links = json.loads(mj[i]['link'].replace('\'','\"' )
                                        .replace('None', 'null'))
        for l in links:
            if l['type'] == 'application/pdf':
                link = l['href']
        titles_and_links.append((title, link))
    return titles_and_links

def download_pdfs(titles_and_links, directory):
    counter = 0
    length = len(titles_and_links)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in titles_and_links:
        print("Downloading " + str(counter + 1) 
            + " of " + str(length) + ": " + i[0])
        response = requests.get(i[1])
        with open(directory + str(counter) + ".pdf", 'wb') as f:
            f.write(response.content)
        counter += 1
    print("finished.")

if __name__ == "__main__":
    args = get_args()
    if args.e > IDX_MAX or args.s > args.e:
        print("Error: illegal starting or ending index.")
        os._exit(1)
    try:
        metadata = open(args.m)
        metadata_json = json.load(metadata)
        titles_and_links = get_titles_and_links(metadata_json, args.s, args.e)
        download_pdfs(titles_and_links, args.t)
    except:
        print("Error: Can not locate metadata file, please try agian.")