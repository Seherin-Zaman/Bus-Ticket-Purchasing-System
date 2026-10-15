
# ---------- class for saving receipt info ----------
class Receipt:
    def __init__(self, UserName, CategoryTitle, TopupTitle, Price, ClassName, Quantity, StartDate, EndDate ):
        
        # store the username of the person making the purchase
        self.UserName = UserName
        
        # main category (for example: Bus Pass, Ticket, etc.)
        self.CategoryTitle = CategoryTitle
        
        # specific top-up or product name (e.g., Weekly Pass, Monthly Topup)
        self.TopupTitle = TopupTitle
        
        # price of the item
        self.Price = Price
        
        # which class / type the item belongs to (if used in your project)
        self.ClassName = ClassName
        
        # quantity purchased (e.g., number of tickets)
        self.Quantity = Quantity
        
        # start date of validity (if it’s a pass/ticket)
        self.StartDate = StartDate
        
        # end date of validity
        self.EndDate = EndDate


        
        
    
