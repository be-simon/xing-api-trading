import win32com.client

class XAQuery_EventHandler:
  RES_PATH = 'C:\\eBest\\xingAPI\\Res\\'
  tr_state = 0
  
  def OnReceiveData(self, code):
    print(">>> receive data: ", code)
    XAQuery_EventHandler.tr_state = 1
    
  def OnReceiveMessage(self, err, code, msg):
    # > 0000~0999 : 정상 (ex ) 0040 : 매수 주문이 완료되었습니다.)
    # > 1000~7999 : 업무 오류 메시지 (1584 : 매도잔고가 부족합니다.)
    # > 8000~9999 : 시스템 에러 메시지
    print('>>> receive message: ', err, code, msg)
    