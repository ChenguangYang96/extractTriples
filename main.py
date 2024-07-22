# -*- coding: utf-8 -*-

import pdf2Text
import triples_from_text


if __name__ == '__main__':
    pdf2Text.pdf2Text()
    triples_from_text.start_extract_triples()