list_a = ['car','place','tree','under','grass','price']
def remove_items_containing_a_or_A():
    for i in list_a:
        result = list(filter(lambda x:x=='a' or x=='A',i))
        if result==['a'] or result==['A']:
            list_a.remove(i)
remove_items_containing_a_or_A()
print(list_a)