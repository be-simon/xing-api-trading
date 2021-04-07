import win32com.client
import pythoncom
from agent.xa_query import XAQuery_EventHandler

class QueryManager:
  def get_stock_list(self, market = 0):
    # 주식 종목 조회
    # TR number: t8430
    
    if market not in [0, 1, 2]:
      raise Exception('market param : 0 - all, 1 - KOSPI, 2 - KOSDAQ')
    
    # XAQuery 객체 생성 및 리소스 파일 불러오기
    xa_query = win32com.client.DispatchWithEvents('XA_DataSet.XAQuery', XAQuery_EventHandler)
    xa_query.LoadFromResFile(XAQuery_EventHandler.RES_PATH + 't8430' + '.res')
    
    inblock_name = 't8430InBlock'
    outblock_name = 't8430OutBlock'
    inblock_data = {'gubun': market}
    outblock_fields = ['hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun']
    
    # 인블럭 세팅
    for key, value in inblock_data.items():
      xa_query.SetFieldData(inblock_name, key, 0, value)
    
    # 요청
    result = xa_query.Request(0)
    while xa_query.tr_state == 0:
      pythoncom.PumpWaitingMessages()
    if result < 0:
      raise Exception('request err code: ', result)
    
    # 결과값 가져오기
    result = []
    occurs = xa_query.GetBlockCount(outblock_name) # occurs의 수 
    for o in range(occurs):
      item = {}
      for f in outblock_fields:
        v = xa_query.GetFieldData(outblock_name, f, o)
        item[f] = v
      result.append(item)
    
    return result
    
        
    

    
    