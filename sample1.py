from collections import Counter 
  
def remov_duplicates(input): 
  
    # split input string separated by space 
    input = input.split(" ") 
  
    # joins two adjacent elements in iterable way 
    for i in range(0, len(input)): 
        input[i] = "".join(input[i]) 
  
    # now create dictionary using counter method 
    # which will have strings as key and their  
    # frequencies as value 
    UniqW = Counter(input) 
  
    # joins two adjacent elements in iterable way 
    s = " ".join(UniqW.keys()) 
    print (s) 
    print("Sample1 executed Successfully")
  
# Driver program 
if __name__ == "__main__": 
    input = 'Python is great and Java is also great'
    remov_duplicates(input) 
