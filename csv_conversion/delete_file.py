import os
def checkoutfile(outfile):
    if os.path.exists(outfile):
        os.remove(outfile)
