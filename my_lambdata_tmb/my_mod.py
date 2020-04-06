# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# # if in global scope this will mess up 
# # our ability to import other functions
# # from this file
# # need to nest it under the main
# x = int(input("Please choose a number: "))
# result = enlarge(x)
# print(result)

if __name__ == "__main__":

   
    x = int(input("Please choose a number: "))
    result = enlarge(x)
    print(result)