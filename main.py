import os
import argparse
from datetime import date

def printHeader(year, day=0, filename=""):
    if day == 0:
        day = int(filename.split('.')[0][-2:])
    print(f"============= {year} / day {day} =============")
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # -y 2022 -d 1 -a 0
    parser.add_argument("-y", "--year", dest="year", default="2022", help="AoC Year")
    parser.add_argument("-d", "--day", dest="day", default="0", help="AoC Day")
    parser.add_argument(
        "-a", "--all", dest="runall", default="0", help="Run all"
    )

    args = parser.parse_args()

    mainfile = os.path.basename(__file__)
    if int(args.runall) == 1:
        folders = [file for file in os.listdir() if not file.startswith('.')]
        for year in folders: #should only be year folders
            for filename in os.listdir(year):
                if filename != mainfile and filename.endswith(".py"):
                    printHeader(year, filename=filename)
                    os.chdir(f"{year}/")
                    exec(open(filename).read())
                    os.chdir("../")
    else:
        os.chdir(f"{args.year}/")
        if int(args.day) == 0:
            for filename in os.listdir():
                if filename != mainfile and filename.endswith(".py"):
                    printHeader(args.year, filename=filename)
                    exec(open(filename).read())
        else:
            printHeader(args.year, day=args.day)
            exec(open(f"day{args.day.zfill(2)}.py").read())
