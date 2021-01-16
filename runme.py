# import yfinance as yf
#
#
#
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
#
# print(data)




class investment:

    def __init__(self, maxGeschoss, aGrund, GFZ, wertHaus):

        self.maxGeschoss = maxGeschoss
        self.aGrund = aGrund
        self.GFZ = GFZ
        self.wertHaus = wertHaus


        pass


    def rentPrice(self, N_aprt, Qm_aprt, count_room):
        pass



    def aWohn(self):
        maxA = self.aGrund * self.GFZ


        return maxA



    def ruecklagen(self):

        rueckpa = self.wertHaus * 0.02
        rueckpm = rueckpa/12

        return rueckpa, rueckpm





if __name__ == "__main__":

    test = investment
    print(test(2,564,0.4,700000).aWohn())
