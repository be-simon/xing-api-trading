import pythoncom

class XASession_EventHandler:
  # Connect, Login, Logout 이벤트 핸들러
  server_res = 0
  login_state = 0

  def clear_res(self):
    XASession_EventHandler.server_res = 0

  def _set_res(self):
    XASession_EventHandler.server_res = 1
  
  def wait_res(self):
    while XASession_EventHandler.server_res == 0:
      pythoncom.PumpWaitingMessages()

  def OnLogin(self, code, msg):
    try:
      if code != '0000':
        raise Exception(msg)
    except Exception as err:
      print('>>>login err: ', err)
    else:
      print('>>> login success')
      XASession_EventHandler.login_state = 1
    finally:
      self._set_res()
      
  def OnDisconnect(self):
    print('>>> server disconnected')
    XASession_EventHandler.login_state = 0
    
  def OnConnectTimeOut(self):
    raise Exception('Time Out Exception')
  