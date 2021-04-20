import random
def primary():
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   rnd=random.randint(0,13)
   quotes = f.readlines()
   print(quotes[rnd])
   f.close()

  #print(quotes)

if __name__== "__main__":
  primary()
