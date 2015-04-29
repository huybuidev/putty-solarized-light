import os
import argparse


def readList(fpath):
    f = open(fpath)
    res = f.readlines()
    f.close()
    return res


def getRegFileContent(profile):
    data = '''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\%s]
"Colour0"="101,123,131"
"Colour1"="88,110,117"
"Colour2"="253,246,227"
"Colour3"="238,232,213"
"Colour4"="238,232,213"
"Colour5"="101,123,131"
"Colour6"="7,54,66"
"Colour7"="0,43,54"
"Colour8"="220,50,47"
"Colour9"="220,50,47"
"Colour10"="133,153,0"
"Colour11"="133,153,0"
"Colour12"="181,137,0"
"Colour13"="181,137,0"
"Colour14"="38,139,210"
"Colour15"="38,139,210"
"Colour16"="211,54,130"
"Colour17"="211,54,130"
"Colour18"="42,161,152"
"Colour19"="42,161,152"
"Colour20"="238,232,213"
"Colour21"="238,232,213"
"Font"="DejaVu Sans Mono"
"FontIsBold"=dword:00000001
"FontHeight"=dword:0000000c
''' % profile
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('profiles_list_file',
                        help='Text file contains PuTTY profiles list')
    args = parser.parse_args()
    print "Reading profile list from '%s' ..." % args.profiles_list_file,
    profiles = readList(args.profiles_list_file)
    print "DONE"
    print

    tmp_file = "tmp_putty_install.reg"
    for p in profiles:
        p = p[:-1]  # Remove trailing \n character
        reg_data = getRegFileContent(p)
        f = open(tmp_file, "w")
        f.write(reg_data)
        f.close()
        # Import reg file
        print "Install solarized for profile '%s' ..." % p,
        os.system("regedit.exe /s %s" % tmp_file)
        print "DONE"
    # Delete tmp_file
    os.remove(tmp_file)

    print
    print "FINISHED"
