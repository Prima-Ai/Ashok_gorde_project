# package import statement
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
from dotenv import load_dotenv
import os
load_dotenv()

class SmartOne:
    def __init__(self):
        #create object of call
        self.obj=SmartConnect(api_key=os.getenv("api_key"))
    
    def place_order(self,symbol,transactiontype,price,quantity):
        try:
            ## login api call
            data = self.obj.generateSession(os.getenv("CLIENT_ID"),os.getenv("PASSWORD"),os.getenv("TOTP"))
            if data['data'] != None:
                refreshToken = data['data']['refreshToken']
                
                ## fetch the feedtoken
                feedToken = self.obj.getfeedToken()
                
                ## fetch userProfile
                if not refreshToken:
                    return "Please check your refresh token"

                ## fetch User Profile
                userProfile = self.obj.getProfile(refreshToken)
                
                ##place order
                try:
                    orderparams = {
                        "variety": "NORMAL",
                        "tradingsymbol": f"{symbol}-EQ",
                        "symboltoken": "3045",
                        "transactiontype": f"{transactiontype}",
                        "exchange": "NSE",
                        "ordertype": "LIMIT",
                        "producttype": "INTRADAY",
                        "duration": "DAY",
                        "price": f"{price}",
                        "squareoff": "0",
                        "stoploss": "0",
                        "quantity": f"{quantity}"
                        }
                    orderId=self.obj.placeOrder(orderparams)
                except Exception as e:
                    print("Order placement failed: {}".format(e.message))
            else:
                return "please add a valid TOTP"
                            
        except Exception as e:
            raise e
        


# angelone = SmartOne()
# print(angelone.place_order())