import os,re,csv,sys
Sub_ID_List = []
Sub_ID_List_Only = []

# Finding Payee NPI to replace Submitter ID based on NPI on 835 File)
def bxc_find_payee_NPI (bxc_fl):
    xx = open(bxc_fl,"r")
    x_filename = bxc_f1
    fxx =xx.read()
# Read the file to replace the existing ISA 06, 08 & GS 03,04
    r1 = re.findall("\WXX\W(\d{10,10})\W",fxx) 
# Regular Expression to retrieve all the Billing NPi from the ERA ANSI X12 835 file 
#   Print("****DEBUG MODE - Regular Expression Output******")
#   print(r1)
    return(r1)

# To retrieve Submitter ID from the Provider List spreadsheet based on the Payee NPI value retrieved above in the 835 file
def bxc_find_subid(str):
    for line in str:
        csvFile = csv.reader(open('835_Providers_List.csv',"r"),delimiter=",")
        for row in csvFile:
            if row[1] == line:
                Sub_ID_List_Only.append(row[3])
#return (Sub_ID_List_Only)


# To replace Submitter ID in the 835 file
def bxc_rep_subid (str,Sub_ID_List_Only):
    fi = open(str,"r")
    A="*ZZ*{}"
    B='*TEST_SUBID*{}*'
    fi_data = fi.read()
    #count = fi_data.count('~N1*PE*')
    for inx_Val in SUB_ID_List_Only:
        fi_data = fi_data.replace('*ZZ*0000000000',A.format(inx_val),1)
        fi_data = fi_data.replace('*TEST_SUBID*0000000000',B.format(inx_val),1)
    f= open(str,'w')
    f.write(fi_data)
    f.close()

#To Replace data preping the file for updates. Note - These files highly structured and formatted per HIPAA Standards 

def bxc_rep(str):
    fi = open(str,"rt")
    fi_data = fi.read()
    fi_data = fi_data.replace('*ZZ*ISA06     ','ZZ*TEST_SUBID')
    fi_data = fi_data.replace('*ZZ*ISA08     ','ZZ*0000000000')
    fi_data = fi_data.replace('*ZZ*GS02      ','ZZ*TEST_SUBID')
    fi_data = fi_data.replace('*ZZ*GS03      ','ZZ*0000000000')
    f = open(str,'w')
    f.write(fi_data)
    f.close()
    #   Print("****---DEBUG MODE - Prep Files for ISA GS Updates by filling All Zeros ---******")
    return

## // MAIN PROGRAM STARTS HERE
if __name__ == "__main__":
    os.chdir('E:/SOURCE FILE LOCATION')
    DIR = os.listdir()
    for line in DIR             # Replace Submitter ID based on the Payee NPI for each of the file in the Source Folder
        provider_NPI_List = []
        Sub_ID_List_Only = []
        if line.startswith('2021'):   # Replace on for files received in 2021
            bxc_rep(line)
            provider_NPI_List = bxc_find_payee_NPI (line)     # Get Payee NPI List
            #print(provider_NPI_List)           # Check Provider NPI Listing - For Manual Verification and Debugging
            bxc_find_subid (provider_NPI_List)                # Get Submitter ID each Payee NPI is registed with to replace
            #print(Sub_ID_List_Only)            # Check Sub_ID_List_Only - For Manual Verification and Debugging
            bxc_rep_subid (line,Sub_ID_List_Only)             # Replace PAYEE NPI with SUBMITTER ID
## // MAIN PROGRAM ENDS HERE
