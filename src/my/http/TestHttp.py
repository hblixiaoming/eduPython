from urllib import request

def getOpenRoomList():
    header_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = 'http://www.baidu.com'
    req = request.Request(url, headers=header_dict)
    res = request.urlopen(req)
    ret = res.read()
    print(ret)
    pass

getOpenRoomList()



