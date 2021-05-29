import win32com.client

class XAReal_EventHandler:
  RES_PATH = 'C:\\eBest\\xingAPI\\Res\\'

  def OnReceiveRealData(self, tr_name):
    print(">>> receive real data: ", tr_name)
    
  def OnReceiveLinkData(self, link_name, data, filter):
    print('>>> receive link data: ', link_name, data)
    