class TradingAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} to account {self.account_id}. New balance: {self.balance}"
        
    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient balance in account {self.account_id}"
        else:
            self.balance -= amount
            return f"Withdrew {amount} from account {self.account_id}. New balance: {self.balance}"
        
    def get_balance(self):
        return self.balance

class RiskManagement:
    def __init__(self, risk_level):
        self.risk_level = risk_level

    def assess_risk(self):
        return self.risk_level
    
class AnalyticsEngine:
    def __init__(self, data_source):
        self.data_source = data_source

    def analyze_data(self):
        return self.data_source
    
class NotificationSystem:
    def __init__(self, notification_channel):
        self.notification_channel = notification_channel

    def send_notification(self, message):
        return f"Sent notification: {message} via {self.notification_channel}"
    
# StockTrader class
class StockTrader(TradingAccount, RiskManagement, AnalyticsEngine):
    def __init__(self, account_id, balance, risk_level, data_source):
        TradingAccount.__init__(self, account_id, balance)
        RiskManagement.__init__(self, risk_level)
        AnalyticsEngine.__init__(self, data_source)

    def buy_stock(self, stock_symbol, quantity):
        return f"Bought {quantity} shares of {stock_symbol} at {self.get_balance()} per share"
    
    def sell_stock(self, stock_symbol, quantity):
        return f"Sold {quantity} shares of {stock_symbol} at {self.get_balance()} per share"
    
    def get_portfolio(self):
        return f"Portfolio: {self.get_balance()}"
    
# CryptoTrader class
class CryptoTrader(TradingAccount, RiskManagement, NotificationSystem):
    def __init__(self, account_id, balance, risk_level, notification_channel):
        TradingAccount.__init__(self, account_id, balance)
        RiskManagement.__init__(self, risk_level)
        NotificationSystem.__init__(self, notification_channel)

    def buy_crypto(self, crypto_symbol, quantity):
        return f"Bought {quantity} {crypto_symbol} at {self.get_balance()} per unit"
    
    def sell_crypto(self, crypto_symbol, quantity):
        return f"Sold {quantity} {crypto_symbol} at {self.get_balance()} per unit"
    
    def get_portfolio(self):
        return f"Portfolio: {self.get_balance()}"
    
# ProfessionalTrader class
class ProfessionalTrader(StockTrader, CryptoTrader):
    def __init__(self, account_id, balance, risk_level, data_source, notification_channel):
        StockTrader.__init__(self, account_id, balance, risk_level, data_source)
        CryptoTrader.__init__(self, account_id, balance, risk_level, notification_channel)

    def get_portfolio(self):
        return f"Portfolio: {self.get_balance()}"
    
    def get_all_trades(self):
        return f"All trades: {self.get_portfolio()}"
    
    def get_all_notifications(self):
        return f"All notifications: {self.get_portfolio()}"
    
    def get_all_analytics(self):
        return f"All analytics: {self.get_portfolio()}"
    
    def __str__(self):
        return f"Professional Trader: {self.get_portfolio()}"
    
# Test the classes
stock_trader = StockTrader("123456", 10000, "Low", "Stock Data")
crypto_trader = CryptoTrader("123456", 10000, "Low", "Email")
professional_trader = ProfessionalTrader("123456", 10000, "Low", "Stock Data", "Email")
print(stock_trader)
print(crypto_trader)
print(professional_trader)

stock_trader.buy_stock("AAPL", 100)
crypto_trader.buy_crypto("BTC", 0.001)
professional_trader.buy_stock("AAPL", 100)
professional_trader.buy_crypto("BTC", 0.001)