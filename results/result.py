import json
import printer_for_results as printer2

number_of_files = 17
i=1
j=1

while i<=number_of_files:
    filename = 'allmatches-'+str(i) + '.txt'
    allmatches_file = open(filename, 'r')
    wdcnt = 0
    swcnt = 0
    mccnt = 0
    matches = []
    itsnum = False
    itsplacename = True
    for line in allmatches_file:
        if itsplacename:
            placename = line[:-1]
            itsnum = True
            itsplacename = False
            print(j)
            j+=1
        elif itsnum:
            lnsp = line.split()
            wdcnt = int(lnsp[0])
            swcnt = int(lnsp[1])
            mccnt = int(lnsp[2])
            mccnt1 = mccnt
            itsnum = False
            if mccnt == 0:
                printer2.AddWithoutMatches(placename, wdcnt, swcnt)
                itsplacename = True
        elif mccnt > 0:
            match = line
            matches.append(match[:-1])
            mccnt -= 1
            if mccnt == 0:
                itsplacename = True
                printer2.AddWithMatches(placename, wdcnt, swcnt, mccnt1, matches)
                matches = []
    allmatches_file.close()
    i+=1
