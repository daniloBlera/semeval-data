#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


def get_lines_from(filename: str) -> List[str]:
    lines = list()
    with open(filename) as fd:
        lines = fd.read().splitlines()

    return lines


def get_statement(var: str, idx: str, value: str) -> str:
    return f'{var}[{idx}] = {repr(value)}'


def main():
    with open('statements', 'w') as fd:
        idxs = get_lines_from('./train/train-idxs')
        sentences = get_lines_from('./train/train-modified')
        for (i, s) in zip(idxs, sentences):
            stmt = get_statement('train_sentences_raw', i, s)
            _ = fd.write(stmt + '\n')

        _ = fd.write('\n')

        idxs = get_lines_from('./test/test-idxs')
        sentences = get_lines_from('./test/test-modified')
        for (i, s) in zip(idxs, sentences):
            stmt = get_statement('test_sentences_raw', i, s)
            _ = fd.write(stmt + '\n')

    print('Done!')


if __name__ == '__main__':
    main()
