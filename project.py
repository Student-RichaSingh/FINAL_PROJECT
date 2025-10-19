import csv
import random
upperlimit=0

def main():
    name=input("Enter your name: ").strip().capitalize()
    level=validate_level() #1 [1-10] 2 [1-50] 3 [1-100]
    
    
    highest_score(name,guess_check(level))

    update=True
    
    for _ in range(2):
        next=input('Enter \"continue\" to move to the next round or else write \"quit\": ')
        if next.lower()=="continue":
            level=validate_level() 

            highest_score(name,guess_check(level))
                
        elif next.lower()=="quit":

            with open("score.csv") as file:
                reader =csv.reader(file)
                for row in reader:
                    if row[0].strip().lower()==name.lower():
                        print(f"Your highest score is: {row[1]}") #scores print
                        update=False
                        break
            break
        else:
            print("Invalid Input")

    #printing highest score
    if update:
        with open("score.csv") as file:
            reader =csv.reader(file)
            for row in reader:
                if row[0].strip().lower()==name.lower():
                    print(f"Your highest score is: {row[1]}")


def highest_score(user, score):
    rows=[]
    flag=True
    try:
        with open("score.csv") as file:
            reader =csv.reader(file)
            for row in reader:
                if not row:   # skip empty lines
                        continue
                if row[0].strip().lower()==user.lower():
                    if score>int(row[1]):
                        row[1]=str(score)
                    flag=False
                rows.append(row)     

    except  FileNotFoundError:
        pass           
        
    if flag:
        rows.append([user, str(score)])

    with open("score.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
                   


def get_input(upperlimit):

    while True:
        try:
            n=int(input())
            if 1<=n<=upperlimit:
                return n
            else :
                print("number not in range.")
        except ValueError:
            print("Invalid input")
            pass


    
def generate_randomnumber(level):
    global upperlimit
    if level==1:
        
        upperlimit=10
      
    elif level==2:
        
        upperlimit=50
    else:
        
        upperlimit=100    

    return random.randint(1,upperlimit),upperlimit



def guess_check(level): #to check whether user's entered number and calculate the score
    rn,upperlimit=generate_randomnumber(level)
    print(f"Enter your numbers in range of 1 to {upperlimit}")
    print("You will be given 5 chances")

    count =0
    for _ in range(5):
        n=get_input(upperlimit)
        
        if rn==n:
            print(f"You cleared level {level}.")
            break
        else:
            count+=1
            if n<rn:
                print("Too low!")
            if n>rn:
                print("Too large!")    
        
                    
    return 100-(count*20)     #returning score out of 100   


def validate_level():
    while True:
        try:
            level=int(input("Enter level 1 , 2 or 3: "))
            levels=[1,2,3]
 
            if level not in levels:
                print("Invalid level.Try again.")
                pass
            else:
                return level
            
        except ValueError:
            print("Invalid Input. Try again.")
            pass

if __name__=="__main__":
    main()    
