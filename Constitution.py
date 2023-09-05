#Analyzes any text file and outputs the most frequent characters, Upper case letters, and lower case letters
#Also gives count of how many characters total and for each individual character


path = './US_Constitution.txt'
print('Top 10 most frequent characters:')
with open(path, mode='r', encoding='utf-8') as file:
    count = 0


    max_frequency = {}
    for i in file.read():
        count += 1
    
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1

    x=list(max_frequency.values())
    
    x.sort(reverse=True)
    x=x[:10]
    for i in x:
        for j in max_frequency.keys():
            if(max_frequency[j]==i):
                print("'" + str(j)+ "'" + " : "+str(max_frequency[j]))

    
print('Top 10 most frequent Upper case letters:')
with open(path, mode='r', encoding='utf-8') as file:
    upper_case = {}
    for i in file.read():
    
        if i in upper_case and i.isupper():
            upper_case[i] += 1
        else:
            upper_case[i] = 0

    x=list(upper_case.values())
    
    x.sort(reverse=True)
    x=x[:10]
    for i in x:
        for j in upper_case.keys():
            if(upper_case[j]==i):
                print("'" + str(j)+ "'" + " : "+str(upper_case[j]))
print('Top 10 most frequent Lower case letters:')
with open(path, mode='r', encoding='utf-8') as file:
    lower_case = {}
    for i in file.read():
    
        if i in lower_case and i.islower():
            lower_case[i] += 1
        else:
            lower_case[i] = 0

    x=list(lower_case.values())
    
    x.sort(reverse=True)
    x=x[:10]
    for i in x:
        for j in lower_case.keys():
            if(lower_case[j]==i):
                print("'" + str(j)+ "'" + " : "+str(lower_case[j]))
    print(f'There are {count} characters in the US Constitution!')