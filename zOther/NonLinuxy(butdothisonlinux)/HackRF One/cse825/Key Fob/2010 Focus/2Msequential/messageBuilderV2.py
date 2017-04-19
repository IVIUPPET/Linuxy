import argparse
import os
#messages array
signalIndex=[] 
signalMessage=[]
signalMessageHex = []


def string_slice(f_input):
    isOne = 0
    for line in f_input:
        #Fix out of range error
        if line == '\n':
            continue
        #Split line into it's sub-messages
        line = line.split()
        #String to hold bitstring
        message=""
        #remove the index
        index=line.pop(0)
        #remove the '....'
        line.pop(-1)
        #Build the bitstring
        # concatenate the the message with the 2nd and 4th digit of the 4 digit thing
        if(not isOne):
            for element in line:
                isOne += int(element)
        if(isOne):
            for element in line:
                if(len(element)==4):
                    message = message+element[1]+element[3]

            #Append only 16 bit messages
            if(len(message) == 16):
                signalMessage.append(message)
                signalIndex.append(index)

def check_error():    
    # Check the messages are byte-orientated.
    # Each message should be 2 bytes (16 bits)
    try:
        for line in  signalMessage:
            if(len(line)!=16):
                errmessage = "Incorrect size, should be 16 bit is only "+len(line)+" bits"
                raise ValueError(errmessage)
    except ValueError:
        print("Error:")

def hex_conversion():        
    # Convert to hex
    for element in signalMessage:
        if element == "\n": #in case runs into \n mid nibble will skip
            continue
        element = hex(int(element,2))
        signalMessageHex.append(element)
    return signalMessageHex

def output_process(f_output):
    #Display message to screen, make text file
    for x in range(0,len(signalIndex)):
        temp = signalIndex[x]  + " " + signalMessageHex[x]+"\n"
        f_output.write(temp)
    f_output.close()
    print("Wrote to file")

def process_sig(infile,outfile):
    string_slice(infile)
    hex_conversion()
    output_process(outfile)

def main():
    parser = argparse.ArgumentParser()
    #Set arguements
    parser.add_argument("-sig", "--signal")
    parser.add_argument("-out", "--output")
    
    args=parser.parse_args()
    
    try:
        infile = open(args.signal,'r')
        outfile = open(args.output,'w') 
    except FileNotFoundError:
        print("Could not find " + args.signal + ". Check you're in the correct directory.")
    process_sig(infile,outfile)
    
    outfile.close()
    return 0

if __name__ == "__main__":
    main()
    
