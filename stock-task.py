
#Function to calculate the Maximum profit with the given data
def CalculateProfit(StockPrice):
    profit=0
    days=len(StockPrice)

    #Will be zero if data of only one day is given
    if(days<=1):
    	return 0;
    
    # Bought is a variable to check if curently a stock is bought or not, bought=-1 if no
    bought=-1

    for i in range(0,days-1):
        
        #Checking that the stock price isn't decreasing the following day
        if(StockPrice[i]<=StockPrice[i+1]):     

            #if stock isn't been bought yet , buy now, And save the day in bought variable
            if(bought==-1):
                bought=i               
        else:  
            # Stock will decrease, sell it now, and record the profit made              
            if(bought>=0):               
                profit+=StockPrice[i]-StockPrice[bought]    
                bought=-1

    #if we reach till the last day and still have stock, sell it and record profit
    if(bought>=0):
        profit+=StockPrice[-1]-StockPrice[bought]

    #return the total profit
    return profit





#Calling the functions with the 3 given test cases
print("Test case 1  [7,1,5,3,6,4], Output :",CalculateProfit([7,1,5,3,6,4]))
print("Test case 2  [1,2,3,4,5], Output :",CalculateProfit([1,2,3,4,5]))
print("Test case 3  [7,6,4,3,1], Output :",CalculateProfit([7,6,4,3,1]))

