def most_frequent(str1):
    count=dict()
    sorted_list=list()
    for ch in str1:
        count[ch]=count.get(ch,0)+1
    sorted_list=sorted([(v,k) for k,v in count.items()],reverse=True)
    for k,v in dict(sorted_list).items():
        print(v,'=',k)
str1=input(" Please enter a string ")
most_frequent(str1)
