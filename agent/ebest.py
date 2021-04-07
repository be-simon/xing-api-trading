import win32com.client
import pythoncom
import json
from agent.xa_session import XASession_EventHandler

class EBest:
  def __init__(self, mode):
    try:
      if mode not in ['DEMO', 'HTS']:
        raise Exception('Run mode is DEMO or HTS')
      
      with open("config/config.json", 'r') as _jsf:
        _config = json.load(_jsf)[mode]
        self.host = _config['host']
        self.port = _config['port']
        self.user = _config['user']
        self.pw = _config['pw']
        self.cert_pd = _config['cert_pd']
        
      self.xa_session_inst = win32com.client.DispatchWithEvents("XA_Session.XASession", XASession_EventHandler)     
    except Exception as err:
      print(">>> err: ", err)
      
  
  def login(self):
    try:
      self.xa_session_inst.ConnectServer(self.host, self.port)
      self.xa_session_inst.Login(self.user, self.pw, 0, 0, 0)
    
      while XASession_EventHandler.login_state == 0:
        pythoncom.PumpWaitingMessages()
        
      acc_num = self.xa_session_inst.GetAccountList(0)
      acc_name = self.xa_session_inst.GetAccountName(acc_num)
      acc_detail = self.xa_session_inst.GetAcctDetailName(acc_num)
        
      print("=" * 10)
      print(acc_num)
      print(acc_name)
      print(acc_detail)  
      print("=" * 10)

    except Exception as err:
      print('>>> err: ', err)
    
    
  def logout(self) :
    self.xa_session_inst.DisconnectServer()
    print('=' * 10)
    print('server disconnected')
    print('=' * 10)
    XASession_EventHandler.login_state = 0