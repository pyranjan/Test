class create_user:
    def __init__(self, u, n):
        self.user = u
        self.balance = n

    def printname(self):
        print(self.user, self.balance)

class add_expense(create_user):
    def __init__(self, n, a, p, split):
        self.name = n
        self.amount = a
        self.paid_by = p
        self.split_by = split

users = dict()
ch = 1
while(ch != 3):
    print("1. Create user \n2. Add expense")
    ch = int(input())
    if(ch == 1):
        name = input()
        n = {key:0 for key in users}
        users[name]=create_user(name,n)
            
    elif(ch == 2):
        name = input()
        amount = int(input())
        paid_by = input()
        split_by = input()
        for key in users:
            if paid_by != key:
                if users[key].balance.get(paid_by) != None:
                    users[key].balance[paid_by] += amount/len(users)
                else:
                    users[key].balance[paid_by] = amount/len(users)
            else:
                for x in users:
                    if x != paid_by:
                        if users[paid_by].balance.get(x) != None:
                            users[paid_by].balance[x] -= amount/len(users)
                        else:
                            users[paid_by].balance[x] = 0-amount/len(users)
                        
                    
    
    
    
    
for key in users:
    print(key, " balance record ", users[key].balance)
        
    
    
        
        
        
        
