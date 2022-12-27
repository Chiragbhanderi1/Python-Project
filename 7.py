list_a = [1,2,3,4,5]
class mylist(list):
  def index_withoutexception():
    try:
        a = eval(input("Enter the index = "))
        print(list_a[a])
    except IndexError:
        print("The index is incorrect and index should lie between -5 and 4")
    except NameError:
        print("Use a Integer value as the input")
        
  index_withoutexception()

  
