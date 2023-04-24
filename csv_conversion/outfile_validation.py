import os


def check_existing_outfile(outfile):
    if os.path.exists(outfile):
        os.remove(outfile)
