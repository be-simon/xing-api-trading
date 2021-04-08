import win32com.client
import pythoncom
from agent.xa_query import XAQuery_EventHandler

class QueryManager:
  # TR의 구성
  #   요청: SetFieldData method로 inblock을 설정
  #   결과 처리: GetBlockCount method로 occurs의 수 지정
  #              GetFieldData method로 원하는 Field의 data를 저장  
  
  def _execute_query(self, tr_name, inblock_name, outblock_name, inblock_data, outblock_fields):
    # 쿼리 실행 모델
    # tr_name(string): TR의 이름
    # inblock_data (dict): TR로 전달할 inblock 데이터
    # outblock_fields (list): 결과로 보려고 하는 outblock의 fields
    # return (list): 각 occur 마다의 결과를 list로 반환, 각 item은 dict type으로 되어있음 
  
    # xa_query 객체 생성
    xa_query = win32com.client.DispatchWithEvents('XA_DataSet.XAQuery', XAQuery_EventHandler)
    xa_query.LoadFromResFile(XAQuery_EventHandler.RES_PATH + tr_name + '.res')
    
    # xa_query객체에 인블럭 데이터 세팅
    for key, value in inblock_data.items():
      xa_query.SetFieldData(inblock_name, key, 0, value)
  
  # xa_query를 이용해 쿼리 request
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
  
  def get_stock_list(self, market = 0):
    # 주식 종목 조회
    # TR number: t8430
    
    if market not in [0, 1, 2]:
      raise Exception('market param : 0 - all, 1 - KOSPI, 2 - KOSDAQ')
    
    inblock_name = 't8430InBlock'
    outblock_name = 't8430OutBlock'
    inblock_data = {'gubun': market}
    outblock_fields = ['hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun']
    
    result = self._execute_query('t8430', inblock_name, outblock_name, inblock_data, outblock_fields)
    
    return result
    
        
    

    
    