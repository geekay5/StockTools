#!/usr/bin/env python3

import sys

def getFinalSum(ic, sip, topUp, term, ror):
    corpus = ic
    while term > 0:
        corpus = corpus + (sip * 12)
        corpus = corpus + (corpus / 100 * ror)
        sip = sip + (sip / 100 * topUp)
        term -= 1
    return corpus

if __name__== "__main__":
    if len(sys.argv) < 6:
        print("Usage: ./sipCorpus.py <sip> <topUp> <term> <ror> <iniCorpus>")
        exit(1)

    sip = int(sys.argv[1])
    topUp = int(sys.argv[2])
    term  = int(sys.argv[3])
    ror = int(sys.argv[4])
    iniCorpus = int(sys.argv[5])

    print("Final Corpus: ", getFinalSum(iniCorpus, sip, topUp, term, ror))