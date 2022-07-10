
class Guess:

    def Info(this):
        print("------------------------------")
        print("--------Nik Software ---------")
        print("------Number Guess System-----")
        print("------------------------------")
    def Input(this):
        this.num=int(input("Enter Number : "))
        
    def Logic(this):
    
        mainNumber = 20
        i=0
        while(i <5):
            if(this.num >mainNumber):
                print("Entered Number is greater")
                this.Input()
                

            elif(this.num <mainNumber):
                print("Enter number is smaller")
                this.Input()
                
            elif(this.num ==mainNumber):
                print("You win")
                print("-------Thank You -----------")
                break
            
            i = i+1
        
        

guess = Guess()
guess.Info()
guess.Input()
guess.Logic()