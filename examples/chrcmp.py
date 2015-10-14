#Write a function that takes two strings as arguments and returns a string containing only the characters found in both strings.
## Have them write 2 versions – one that is O(n) and one that is O(n^2)

#O(n^2) algo
def retMatch(str1,str2):
    str3=""
    for chr in str1:
        for chr1 in str2:
            if(chr == chr1):
                str3+=chr
    return str3

# still O(n^2) in worst case but has avg case better than above
def retBestMatch(str1,str2):
    str3=""
    dict = {}
    for chr in str1:
        if(chr not in dict):
            for chr1 in str2:
                if((chr == chr1) and (chr not in dict)):
                    str3+=chr
                    dict[chr]=chr
    return str3

# runs at O(n), more space complexity due to dict and codes2 array but lets assume machine has enough mem
def retExcellenMatch(str1,str2):
    str3=""
    dict = {}
    codes2=[None]*len(str2)
    for chr in str2:
        codes2[ord(chr)%len(str2)]= chr
    for chr in str1:
        if((chr not in dict) and (chr == codes2[ord(chr)%len(str2)])):
            dict[chr]=chr
            str3+=chr
    return str3

def run():
    inputString1 = input("Enter String1 ")
    inputString2 = input("Enter String2 ")
    print(retExcellenMatch(inputString1,inputString2))

if __name__ == '__main__':
    run()