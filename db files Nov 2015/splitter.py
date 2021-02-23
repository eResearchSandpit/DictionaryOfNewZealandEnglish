#!/usr/bin/env python3

import os, sys, itertools

headword_marker='Homonym Number'
ouputfolder="ByHeadword"
# filename='nzdc_export_A.txt'

# Count the arguments
arguments = len(sys.argv) - 1
# Output argument-wise
position = 1
while (arguments >= position):
    print ("Parameter %i: %s" % (position, sys.argv[position]))
    
    filename = sys.argv[position]
    dictionary_letter=filename[-5]
    position = position + 1

    #make sure directory exists
    letter_output_folder=ouputfolder+'/'+dictionary_letter
    if not os.path.exists(letter_output_folder):
        os.makedirs(letter_output_folder)

    headword_loc=[]

    linecount=0
    with open(filename) as myFile:
        for num, line in enumerate(myFile,1):
            linecount=linecount+1
            if headword_marker in line:
                headword_loc.append(num)

    # #print headwords
    # for loc in headword_loc:
    #     print(num)
    #     headword = linecache.getline(filename,loc-1)
    #     print(headword)

    #correct_headword loc
    headword_loc = [x-2 for x in headword_loc]
    headwords=len(headword_loc)
    headword_loc.append(linecount)

    multiple_headword_count=0

    # print first headword section
    for i in range(headwords-1):
        #get the headword text
        headword_text=[]
        with open(filename,'r') as f:
            for line in itertools.islice(f,headword_loc[i],headword_loc[i+1]-1):
                headword_text.append(line)
            headword = headword_text[0].replace('/',' OR ')
            outputfilename=letter_output_folder+'/'+headword
            

            #handle multiple same named headwords
            if os.path.exists(outputfilename):
                multiple_headword_count=multiple_headword_count+1
                outputfilename = outputfilename + " entry " +str(multiple_headword_count)
            else:
                multiple_headword_count=0
            print(outputfilename)
            


