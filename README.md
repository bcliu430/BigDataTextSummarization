# ECE/CS 5984: Big Data Text Summarization

This repository focuses on text summarization using deep learning techniques.
We focus on three types of text summarization:

* Extractive Text Summarization
* Abstractive Text Summarization
* Hybrid Text Summarization

The `Papers/` directory contains a list of papers that reference recent work in
text summarization.

## Code Repositories

Some of the repositories that already have implementations of some approaches
towards text summarization are listed below.

* [Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting](https://github.com/ChenRocks/fast_abs_rl): ACL 2018 Paper from Chen and Bansal on a hybrid approach to text summarization. The authors use abstractive summarization to select salient sentences and subsequently compress the selected sentences using reinforcement learning. The code is in PyTorch 0.4.

* [Get to the Point: Summarization with Pointer Generator Networks](https://github.com/atulkum/pointer_summarizer): The paper comes from Stanford (Christopher Manning's lab) that augments neural sequence-to-sequence networks by adding a pointer generator network to select specific words from the original text and use coverage to keep track of what has already been summarized to avoid repetition. The code is in PyTorch 0.3.

## Dataset

Most of the papers we have read so far use the CNN/Daily Mail dataset for text summarization. The dataset can be obtained using the repository [here](https://github.com/abisee/cnn-dailymail).

Additionally, we also plan to use http://summari.es from Cornell.

## Evaluation

The two main evaluation techniques used are:

* [ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric)): An implementation for calculating the ROUGE metric is available in Python as a package `pyrouge`.
* [METEOR](https://en.wikipedia.org/wiki/METEOR)
