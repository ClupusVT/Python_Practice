def ispalindrome(string):
        list1 = []
        list2 = []
        for i in string:
            list1.append(i)
            #print(list1)
           
        list1.reverse()
        for i in string:
                list2.append(i)
                #print(list1)
                
        if list2 == list1:
                print ("This is Palindrome")
        else:
                print ("this is not Palindrome")
        
ispalindrome("madam") 