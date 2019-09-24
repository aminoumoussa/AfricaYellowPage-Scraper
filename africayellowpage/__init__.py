"""
Usage:
    africayellowpage_scraper mine <what> <where> [--file_path=<destination_file>]

Options:
    <what>    Qui,quoi? (Hotels)
    <where>        Où? (Ghana)   
    --file_path file to save results to 
"""

from docopt import docopt
import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')


#import helpers
from africayellowpage.helpers.scraper import get_pages, save_results



def main():
    args = docopt(__doc__,version="AfricaYellowPage Scraper 1.0")
    if args["mine"]:
        what = args["<what>"]
        where = args["<where>"]
        results = get_pages(what,where)
        if results:
            if args["--file_path"]:
                if results:
                    save_results(results,args["--file_path"])
            else:
                print(results)


if __name__=="__main__":
    main()