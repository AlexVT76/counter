calls=0
def count_coll (call):
     global  calls
     calls = call+1

def string_infor (string):
   count_coll(calls)
   str_1= (len(string), string.upper(), string.lower())
   return str_1
def is_contains (string,list_to_search):
    count_coll(calls)
    string_l=string.lower()
    list_to_search_l=list_to_search.lower()
    if string_l in list_to_search_l:
      return True
    else:
      return False

print(string_infor('арбалет'))
print(is_contains('arm','arm''ring'))
print(string_infor('Variable'))
print(is_contains('FIsh','fish''ball'))
print (calls)