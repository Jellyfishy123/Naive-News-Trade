from AlgoAPI import AlgoAPIUtil, AlgoAPI_Backtest
from datetime import datetime, timedelta

class AlgoEvent:
    def __init__(self):
        self.lasttradetime = datetime(2000,1,1)
        self.keywordList = ["increase", "up", "improve"]

    def start(self, mEvt):
        self.myinstrument = mEvt['subscribeList'][0]
        self.evt = AlgoAPI_Backtest.AlgoEvtHandler(self, mEvt)
        self.evt.start()
        
    def on_newsdatafeed(self, nd):
        if nd.lang=="en" and nd.category=="AMERICAS": #listen to English Americas News 
            cnt = sum(1 for word in self.keywordList if word in nd.text)
            # check if News content contains all desired keywords
            if cnt==len(self.keywordList):
                # open a new order 
                order = AlgoAPIUtil.OrderObject(
                    instrument=self.myinstrument,
                    volume=1,
                    openclose='open',
                    buysell=1,          #1=long_order, -1=short_order
                    ordertype=0         #0=market_order, 1=limit_order, 2=stop_order
                )
                self.evt.sendOrder(order)

    def on_bulkdatafeed(self, isSync, bd, ab):
        pass

    def on_marketdatafeed(self, md, ab):
        pass

    def on_orderfeed(self, of):
        pass

    def on_dailyPLfeed(self, pl):
        pass

    def on_openPositionfeed(self, op, oo, uo):
        pass
