def calculate_love_score(name1,name2):     # complete code and logic written by me

    Both_names=(name1+name2).lower()
    t=0
    l=0
    for i in Both_names:
        if i in "TRUE".lower():
             t+=1
        
        if i in "LOVE".lower():             # we not used elif because we need to check and this and and this so
            l+=1
        
    Final_score=str(t)+str(l)     # Look at this indnet makes a lot of trouble take care of this
    print("Your Love Score is :",Final_score)

calculate_love_score("Angela Yu","Erfan")

             