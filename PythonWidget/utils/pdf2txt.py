# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/10

import os

def pdf2txt(path: str, outfile: str = "__auto__"):
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage

    password = ""
    rotation = 0

    caching = True
    imagewriter = None
    laparams = LAParams()

    PDFResourceManager.debug = PDFPageInterpreter.debug = 0
    rsrcmgr = PDFResourceManager(caching=caching)

    if outfile == "__auto__":
        outfile = os.path.splitext(path)[0] + ".txt"

    with open(outfile, "w", encoding="utf-8") as outfp, open(path, "rb") as fp:
        # pdf转换
        device = TextConverter(rsrcmgr, outfp, laparams=laparams, imagewriter=imagewriter,)

        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理文档对象中每一页的内容
        pages = PDFPage.get_pages(
            fp, set(), maxpages=0,
            password=password, caching=caching,
            check_extractable=True,
        )
        for page in pages:
            page.rotate = (page.rotate + rotation) % 360
            interpreter.process_page(page)
        device.close()
    return open(outfile, encoding="utf-8").read()
