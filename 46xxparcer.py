import argparse
SECDELIMITER = "\n# "
if __name__ == '__main__':
    parcer = argparse.ArgumentParser(description="46xxsettings parces")
    parcer.add_argument('-f', type=str, help="46xxsettings file (path and name)", required=True)
    parcer.add_argument('-a', type=int, help="active paramenets only", default=0,required=True)
    args = parcer.parse_args()

    file46xxsettings = open(args.f,'r+')
    txt46xxfile = file46xxsettings.read()
    #print(txt46xxfile)
    f46xxsettingsSection = txt46xxfile.split(SECDELIMITER)
    #f46xxsettingsSection.pop(0)
    textinsectionlist = []

    for as2 in f46xxsettingsSection:
        print("-------------------------SECTION-------------------------")
        #print(as2)
        allparams = []
        sectionnoncommentstrings = []
        sectionnonactiveparameters = []
        textinsectionlist = as2.split("\n")
        if f46xxsettingsSection.index(as2) == 0:
            print("MAIN SECTION")
        else:
            print(textinsectionlist[0])
            textinsectionlist.pop(0)
        for stringsdata in textinsectionlist:
            if stringsdata.find("## SET ") == 0 and args.a == 0:
                sectionnonactiveparameters.append(stringsdata)
                allparams.append(stringsdata)
                continue
            if stringsdata.find("##") == 0:
                continue
            if len(stringsdata) > 1:
                sectionnoncommentstrings.append(stringsdata)
                allparams.append(stringsdata)

        for sttext in allparams:
            print("\t",sttext)

