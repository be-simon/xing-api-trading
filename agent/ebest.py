import win32com.client
import pythoncom
import json
from agent.xa_session import XASession_EventHandler
from agent.query_manager import QueryManager

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
      self.query_manager = QueryManager()
      
    except Exception as err:
      print(">>> err: ", err)
      
  
  def connect_server(self):
    try:
      self.xa_session_inst.ConnectServer(self.host, self.port)
      if self.xa_session_inst.IsConnected():
        print('>>> connect server success')
      else:
        raise Exception ('connect server fail')
    except Exception as err:
      print('connect server err: ', err)
  
  
  # login 실패시 while문을 어떻게 벗어날 것인가?
  def login(self):
    try:
      self.xa_session_inst.Login(self.user, self.pw, 0, 0, 0)
      while XASession_EventHandler.login_state == 0:
        pythoncom.PumpWaitingMessages()
    except Exception as err:
      print('>>> login: ', err)
    
    else:   
      acc_num = self.xa_session_inst.GetAccountList(0)
      acc_name = self.xa_session_inst.GetAccountName(acc_num)
      acc_detail = self.xa_session_inst.GetAcctDetailName(acc_num)
        
      print("=" * 10)
      print(acc_num)
      print(acc_name)
      print(acc_detail)  
      print("=" * 10)
    
  def logout(self) :
    try:  
      self.xa_session_inst.DisconnectServer()
      print('>>> server disconnected')
      XASession_EventHandler.login_state = 0
    except Exception as err:
      print('>>> err: ', err)
      
