# put your student name and identification here
#Yuelin Liu
#101154473
import re

# define and write each of your functions here

#this function returns uppercase of the string
def uppercase(words_remove_punc):
    up_out = ""
    #transfer words into Unicode code
    for a in range(len(words_remove_punc)):
        Unicode = ord(words_remove_punc[a])
        #Only deal with lowercase letters
        if Unicode >= 97 and Unicode <= 122:
            up_out += chr(Unicode-32 )
        #If uppercase letters or number, don't change
        else:
            up_out += words_remove_punc[a]
    return up_out


#this function returns string after replacing phrases
def re_phrases(up_out):
    ph_out = up_out
    #define 4 phrases to be replaced
    btw = "BY THE WAY"
    lol = "LAUGHING OUT LOUD"
    omg = "OH MY GOD"
    asap = "AS SOON AS POSSIBLE"

    #if each phrase in the string to be translated, replace it
    for x in range(len(up_out)):
        
        if btw in ph_out:
            btw_i = ph_out.index(btw)
            ph_out = ph_out[:btw_i] + "BTW" + ph_out[len(btw)+btw_i:]
        elif lol in ph_out:
            lol_i = ph_out.index(lol)
            ph_out = ph_out[:lol_i] + "LOL" + ph_out[len(lol)+lol_i:]
        elif omg in ph_out:
            omg_i = ph_out.index(omg)
            ph_out = ph_out[:omg_i] + "OMG" + ph_out[len(omg)+omg_i:]
        elif asap in ph_out:
            asap_i = ph_out.index(asap)
            ph_out = ph_out[:asap_i] + "ASAP" + ph_out[len(asap)+asap_i:]
       
    return ph_out


#this function returns string after replacing words
def re_words(phrases):
    #define 4 words to be replaced
    wo_out = phrases
    acc = "ACCORDING"
    est = "ESTABLISHED"
    no = "NUMBER"
    ltd = "LIMITED"
    
    #if each phrase in the string to be translated, replace it
    for y in range(len(wo_out)):
        if acc in wo_out:
            acc_i = wo_out.index(acc)
            wo_out = wo_out[:acc_i] + "ACC" + wo_out[len(acc)+acc_i:]
        elif est in wo_out:
            est_i = wo_out.index(est)
            wo_out = wo_out[:est_i] + "EST" + wo_out[len(est)+est_i:]
        elif no in wo_out:
            no_i = wo_out.index(no)
            wo_out = wo_out[:no_i] + "NO" + wo_out[len(no)+no_i:]
        elif ltd in wo_out:
            ltd_i = wo_out.index(ltd)
            wo_out = wo_out[:ltd_i] + "LTD" + wo_out[len(ltd)+ltd_i:]
        
    return wo_out


#this function returns string after replacing letters
def re_le(words, lett):
    #turn the string that after replacing words into list
    list_words = list(words)
    #construct a list with letters to be replaced 
    list_1 = ["B", "G", "S", "T", "Z", "X", "P", "E"]
    #construct a list with homoglyphs that corresponds to the list with letters to be replaced
    list_2 = ["8", "9", "5", "7", "2", "><", "|>", "[-"]
    #turn the string that user wants to replace letters into list
    list_lett = list(lett)
    #construct an empty list that used to put the letters that user wants to replace
    list_ans1 = []
    #construct an empty list that used to put the homoglyphs that corresponds to the letters that user wants to replace
    list_ans2 = []
    #construct an empty list that used to put the final result
    list_final = []

    #if the letter that user wants to replace in the letter list, append it to the corresponding empty list
    for num in range(len(lett)):
        if lett[num] in list_1:
            for index in range(len(list_1)):
                if list_1[index] == lett[num]:
                    list_ans1.append(lett[num])
                    list_ans2.append(list_2[index])
        #if letter doesn't in list, explain to users
        else:
            print("This program cannot translate the letter '{}'.".format(lett[num]))
            
    #if the letter that user wants to replace in both letter list and string, replace it and append it to the final string
    for a in range(len(words)):
        if words[a] in list_ans1:
            for b in range(len(list_ans1)):
                if words[a] == list_ans1[b]:
                    list_final.append(list_ans2[b])
        #if it doesn't in it, append the original letters
        else:
            list_final.append(words[a])

    #turn the final list into string   
    final_output = "".join(list_final)
        
    return final_output

                                                                                          
# this is the definition of your main function
def main():
    # write the part of the program that interacts with the user here
    again = "yes"
    while uppercase(again) == "YES":
        words = input("Type the string to be translated: ")
        #remove punctuation
        words_remove_punc = re.sub(r'[^\w\s]','',words)
        up_out = uppercase(words_remove_punc)
        print('\n',up_out,'\n')

        phr = input("Do you want to replace pharses? ")
        while True:
            if uppercase(phr) == "YES" or uppercase(phr) == "Y":
                phrases = re_phrases(up_out)
                break
            elif uppercase(phr) == "NO" or uppercase(phr) == "N":
                phrases = up_out
                break
            else:
                phr = input("Please enter yes or no. Do you want to replace pharses? ")
                
        print('\n')    
        wo = input("Do you want to replace words? ")
        while True:
            if uppercase(wo) == "YES" or uppercase(wo) == "Y":
                words = re_words(phrases)
                break
            elif uppercase(wo) == "NO" or uppercase(wo) == "N":
                words = phrases
                break
            else:
                wo = input("Please enter yes or no. Do you want to replace pharses? ")
                
        print('\n')
        le = input("Do you want to replace letters? ")
        while True:
            if uppercase(le) == "YES" or uppercase(le) == "Y":
                print('\n')
                lett = input("What letters do you want to replace? ")
                lett = uppercase(lett)
                final = re_le(words, lett)
                break
            elif uppercase(le) == "NO" or uppercase(le) == "N":
                final = words
                break
            else:
                le = input("Please enter yes or no. Do you want to replace pharses? ")

        #print the string after each step and the final output
        print('\n', "String for translation: ", up_out)
        print('\n', "After replacing phrases: ", phrases)
        print('\n', "After replacing words: ",  words)
        print('\n', "After replacing letters: ", final)
        print('\n', "The translated string is '{}'.".format(final),'\n')
        
        #ask users if they want to translate another string
        again = input("Do you want to translate another string? ")

        if uppercase(again) == "YES" or uppercase(again) =="y":
            pass
        elif uppercase(again) == "NO" or uppercase(again) =="n":
            print('\n', "Goodbye.")
        else:
            again = input("Please enter yes or no. Do you want to translate another string? ")
    
	
# these should be the last two lines of your submission
if __name__ == '__main__':
	main()
