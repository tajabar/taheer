# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "plugins/dm/callBack/file_process/threePagesToOne.py"

import fitz
from logger import logger


async def threePagesToOne(input_file: str, cDIR: str) -> (bool, str):
    """
    This function takes a PDF file with three pages per sheet and converts it to a single page per sheet format.
    The output file will contain all pages from the input file in sequential order, but with each pair of pages
    combined onto a single sheet.

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user.

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        with fitz.open(input_file) as iNPUT:
            with fitz.open() as oUTPUT:
                width, height = fitz.paper_size("a4")
                r1 = fitz.Rect(0, 0, width, height / 3)
                r2 = fitz.Rect(0, height / 3, width, (2 * height) / 3)
                r3 = fitz.Rect(0, (2 * height) / 3, width, height)
                r_tab = [r1, r2, r3]
                for page in iNPUT:
                    if page.number % 3 == 0:
                        pg = oUTPUT.new_page(-1, width=width, height=height)
                    pg.show_pdf_page(r_tab[page.number % 3], iNPUT, page.number)
                oUTPUT.save(output_path, garbage=3, deflate=True)
        return True, output_path

    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)
        return False, Error

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
