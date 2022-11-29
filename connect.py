import pymongo

def connectdb() :
#if __name__=="__main__":
    print("Insert connect.py")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connect Done at :" + str(client))
    return client
    