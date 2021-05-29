import win32com.client
from agent.xa_real import XAReal_EventHandler

class RealManager:
  def __init__(self):
    self.xa_real = win32com.client.DispatchWithEvents('XA_DataSet.XAReal', XAReal_EventHandler)
    
  def _real_connect_server(self, real_name, inblock_data, outblock_fields):
    self.xa_real.LoadFromResFile(XAReal_EventHandler.RES_PATH + real_name + '.res')
    inblock_name = 'InBlock'
    outblock_name = 'OutBlock'
    
    # xa_real 객체에 인블럭 셋팅
    for k, v in inblock_data:
      self.xa_real.SetFieldData(inblock_name, k, v)
    
    # xa_real 객체로 tr 등록
    self.xa_real.AdviseRealData()
    
    # 결과 가져오기
    result = []
    item = {}
    for f in outblock_fields:
      v = self.xa_real.GetFieldData(outblock_name, f)
      item[f] = v
    result.append(item)
    
    # 블록 전체 데이터 가져오기
    # result = self.xa_real.GetBlockData(outblock_name)
    
    return result
  
  def real_disconnect_server(self):
    self.xa_real.UnAdviseRealData()
    
  def real_disconnect_code(self, code):
    self.xa_real.UnAdviseRealDataWithKey(code)
  
  def get_real_news(self):
    # 실시간 뉴스 제목 패킷 가져오기
    # Real name: NWS
    
    inblock_data = {'nwcode':'NWS001'}
    outblock_fields = ['date', 'time', 'id', 'realkey', 'title', 'code', 'bodysize']
    
    result = self._real_connect_server('NWS', inblock_data, outblock_fields)
    
    return result
    
    

    
    