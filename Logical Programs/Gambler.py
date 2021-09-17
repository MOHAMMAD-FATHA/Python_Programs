'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 19:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 19:55
* @Title: Gambler Game
'''
import random
    
def gamblerProblem():
    """
    Description:
        This function Simulates a gambler who start with stake and place fair 1 bets until
        he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
        times he/she wins and the number of bets he/she makes. Run the experiment N
        times, averages the results, print the results.
    """
    stake=int(input("Enter The The Stake Amount:"))
    goal=int(input("Enter The Amount You Want To Win:"))
    bet_made=int(input("Enter The The Number Of Bets You Want To Make:"))
    no_of_times_won=0
    no_of_time_lost=0
    no_of_bets_made=0

    while(stake >= 0 and stake <= goal and no_of_bets_made < bet_made):
            no_of_bets_made+=1
            gambler_choice=random.randint(0, 1)  #generates a random number 0 or 1
            
            if gambler_choice==1:   #if the random number generated is 0
                no_of_times_won+=1
                stake=stake+1 
            else:
                no_of_time_lost+=1
                stake=stake-1

    percentage_win = (no_of_times_won/bet_made)*100
    print("Number Of Times Won",no_of_times_won)
    print("Percentage Of Win", percentage_win) 
    print("Percentage Of Loss", 100-percentage_win)
    print("Number Of Bets Made", no_of_bets_made) 
        

if __name__ == '__main__':
    gamblerProblem()        