# -*- coding: utf-8 -*-

from services.AuthService import AuthService
from models.User import Role
if __name__ == "__main__":
    auth = AuthService()
    u1 = auth.register("Chahd", "8559_4@-330", Role.ADMIN)
    u2 = auth.register("Bassma", "K225576&_54u", Role.MEMBER)
    u3 = auth.register("Amine", "Mz22_5@^669", Role.ADMIN)
    u4 = auth.register("Sara", "39r965--yil5s", Role.MEMBER)
    print(auth.login("Chahd", "8559_4@-330"))  
    print(auth.login("Bassma", "K225576&_54u"))
    print(auth.login("Amine", "Mz22_5@^669"))
    print(auth.login("Sara", "39r965--yil5s"))
    
