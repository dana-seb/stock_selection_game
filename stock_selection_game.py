import random
import numpy as np
import yfinance as yf
yf.pdr_override()




class Equities():
    def __init__(self, ticker):
        self.ticker = ticker[0]
        self.ticker2 = ticker[1]
        self.ticker3 = ticker[2]
        self.winner = None
        self.get_data()
        
    def get_data(self):
        data1 = yf.download(self.ticker, start="2023-01-01", end="2023-07-01").Close.to_frame()
        data2 = yf.download(self.ticker2, start="2023-01-01", end="2023-07-01").Close.to_frame()
        data3 = yf.download(self.ticker3, start="2023-01-01", end="2023-07-01").Close.to_frame()
        df1 = (data1[['Close']])
        df2 = (data2[['Close']])
        df3 = (data3[['Close']])
        df1['Returns'] = np.log(df1.div(df1.shift(1)))
        df2['Returns'] = np.log(df2.div(df2.shift(1)))
        df3['Returns'] = np.log(df3.div(df3.shift(1)))
        sum1 = df1.Returns.sum()
        sum2 = df2.Returns.sum()
        sum3 = df3.Returns.sum()
        avg1 = df1.Returns.mean()
        avg2 = df2.Returns.mean()
        avg3 = df3.Returns.mean()
        annual_return1 = round(((avg1 * 260) * 100),3)
        annual_return2 = round(((avg2 * 260) * 100),3)
        annual_return3 = round(((avg3 * 260) * 100),3)
        ret = {self.ticker:annual_return1, self.ticker2:annual_return2, self.ticker3:annual_return3}
        sorted_ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
        print("\n")
        print("\n",sorted_ret)
        print("\n")
        print("\n", sorted_ret[0][0], "is the winner with the greatest estimated yearly return value of", sorted_ret[0][1],"%")
        winner = sorted_ret[0][0]
        self.winner = winner


financials = {"VISA INC": "V", "MASTERCARD": "MA", "BLACKROCK": "BLK", "GOLDMAN SACHS": "GS", "FARMERS & MERCHANTS BANCORP": "FM", "AMERIPRISE FINANCIAL INC": "AMP",
              "MOODY'S CORP": "MCO", "JP MORGAN CHASE & CO": "JPM", "DISCOVER FINANCIAL SERVICES": "DFS", "FACTSET RESEARCH SYSTEMS": "FDS"}

information_technology = {"NVIDIA CORP": "NVDA", "CISCO SYSTEMS INC": "CSCO", "ADOBE INC": "ADBE", "MICROSOFT CORP": "MSFT", "JABIL INC": "JBL", "TEXAS INSTRUMENTS INC": "TXN", 
                          "MONOLITHIC POWER SYSTEM INC": "MPWR", "BROADCOM INC": "AVGO", "TELEDYNE TECH INC": "TDY", "KLA CORP": "KLAC"}

real_estate = {"PUBLIC STORAGE": "PSA", "PROLOGIS INC": "PLD", "CUSHMAN & WAKEFIELD PLC": "CWK", "CBRE GROUP INC": "CBRE", "ALTISOURCE ASSET MGMT CORP": "AAMC", "ZILLOW GROUP INC": "Z", 
               "COLLIERS INTL GROUP INC": "CIGI", "TRANSCONTL REALTY COM": "TCI", "MARCUS & MILLICHAP INC": "MMI"}

healthcare = {"REGENERON PHARM": "REGN", "IDEXX LABORATORIES INC": "IDXX", "THERMO FISHER SCIENTIFIC INC": "TMO", "UNITED HEALTH GROUP INC": "UNH", "ELI LILLY AND COMPANY": "LLY",
              "HUMANA INC": "HUM", "MCKESSON CORP": "MCK", "BECTON DICKINSON & CO": "BDX", "AMGEN INC": "AMGN", "RESMED INC": "RMD", "JOHNSON & JOHNSON": "JNJ", "ABBOTT LABORATORIES": "ABT"}

consumer_staples = {"BOSTON BEER CO INC": "SAM", "COCA-COLA INC": "COKE", "COSTCO WHOLESALE CORP": "COST", "KIMBERLY CLARK": "KMB", "PROCTER & GAMBLE CO": "PG", "PEPSICO INC": "PEP",
                    "DIAGEO ADR SPONSORED": "DEO", "CHURCH & DWIGHT COM": "CHD", "COLGATE-PALMOLIVE CO": "CL", "KELLOGG COMPANY": "K"}



def industry_selection(industry):
    choice = random.sample(industry.items(), 3)
    print("\nSelect a company from the following list\n", "\n",choice,"\n")
    game_stocks1 = choice[0][1]
    game_stocks2 = choice[1][1]
    game_stocks3 = choice[2][1]
    ticker = [game_stocks1, game_stocks2, game_stocks3]
    print("\n",ticker,"\n")
    player_guess = input("\nFrom the above selection, Which company has performed the best in the previous year? Enter a ticker below!\n")
  
    if player_guess == Equities(ticker).winner:
        print("\n")
        print("You have correctly guessed the stock with the greatest return!") 
    else:
        print("\n")
        print("You have not made the correct selection and have lost the game!\n")

print("\nThe Stock Selection Game\n")

while True:
  industry = input("\n1) Financials, 2) Information Technology, 3) Real Estate, 4) Healthcare, 5) Consumer Staples, 0) Exit \n")
  if industry == "1":
      industry_selection(financials)
  elif industry == "2":
      industry_selection(information_technology)
  elif industry == "3":
      industry_selection(real_estate)
  elif industry == "4":
      industry_selection(healthcare)
  elif industry == "5":
      industry_selection(consumer_staples)
  elif industry == "0":
      print("\nGoodbye")
      exit()
  else: 
      print("Invalid entry, enter a number from 1 to 5.")     