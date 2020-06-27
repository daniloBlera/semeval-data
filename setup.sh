#!/bin/sh
# Download and extract CoreNLP and dataset files into their respective directories
[ -f './downloads/corenlp.zip' ] || wget 'http://nlp.stanford.edu/software/stanford-corenlp-4.0.0.zip' -O './downloads/corenlp.zip'
[ -d './stanford-corenlp-4.0.0' ] || unzip './downloads/corenlp.zip'
[ -d './SemEval2010_task8_all_data' ] || unzip './downloads/SemEval2010_task8_all_data.zip'
