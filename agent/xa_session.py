class XASession_EventHandler:
  # Connect, Login, Logout 이벤트 핸들러
  login_state = 0
    
  def OnLogin(self, code, msg):
    try:
      if code != '0000':
        raise Exception(msg)
    except Exception as err:
      print('>>>err: ', err)
    else:
      print('>>> login success')
      XASession_EventHandler.login_state = 1
  
  def OnDisconnect(self):
    print('>>> server disconnected')
    XASession_EventHandler.login_state = 0
    
  def OnConnectTimeOut(self):
    # 구현하고 싶다.
    raise Exception('Time Out Exception')
  