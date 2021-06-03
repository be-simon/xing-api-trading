import win32com.client
import pythoncom

class XAQuery_EventHandler:
  RES_PATH = 'C:\\eBest\\xingAPI\\Res\\'
  def __init__(self):
    self.server_res = 0
  
  def clear_res(self):
    self.server_res = 0

  def _set_res(self):
    self.server_res = 1
  
  def wait_res(self):
    while self.server_res == 0:
      pythoncom.PumpWaitingMessages()
      
  def OnReceiveData(self, code):
    print(">>> receive data: ", code)
    self._set_res()
        
  def OnReceiveMessage(self, err, code, msg):
    # > 0000~0999 : 정상 (ex ) 0040 : 매수 주문이 완료되었습니다.)
    # > 1000~7999 : 업무 오류 메시지 (1584 : 매도잔고가 부족합니다.)
    # > 8000~9999 : 시스템 에러 메시지
    print('>>> receive message: ', err, code, msg)
