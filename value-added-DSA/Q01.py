s="abcafshskjgabdjdk"
arr=[0]*26
for i in range(len(s)):
    arr[ord(s[i])-97]+=1
for j in range(len(arr)):
        print(chr(j+97),"->",arr[j])