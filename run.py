from db import CreateRecord
from models import ConfModel
from NHL import N2_API
from config import NHL_ACCESS_KEY


if __name__=="__main__":
    print("start process!")
    conferences = N2_API()

#    print(NHL_ACCESS_KEY+"conferences")
#conferences = "/Users/user/Desktop/NEW_GIT/NHL/again/conferences"
#
    for data in conferences:
        conf_data=N2_API(data)

#        CreateRecord().Conferences(
#            name=w_conf_data['data']
#            )
    print("DONE!")

