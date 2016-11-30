# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 21:36:53 2016

@author: ajatgd
"""

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
            
def smsRes(request):
    id1=['I8ckg12tIqOpz613Sf/VLPClcVhOTKH2','6lAPqTztmhj/1ml4NmER+KXwJev8eMWN','I8ckg12tIqOpz613Sf/VLPClcVhOTKH2','I8ckg12tIqOpz613Sf/VLPClcVhOTKH2']
    wallet=['4817497275977414861','5622253132157119015','5243188823714477159','5014900270407291489']
    body = request.POST.get('Body', '')
    number = request.POST.get('From','')
    comma_index= list(find(',',body))
    if(body[:8]=='payprem'):
        identity=body[9:comma_index[0]]
        wc=body[comma_index[0]:]
        amt=20
        if (identity in id1) and (wc in wallet):
            confirmpayment(identity,wc,amt)
        
    if(body[:8]=='getsubs'):
        identity=body[9:comma_index[0]]
        wc=body[comma_index[0]:]
        amt=20
        if identity in id1 and wc in wallet:
            banktocus(identity,wc,amt)
        
    r = Response()
    r.message(msg)
def confirmpayment(identity,wc,amt):
    
    w2='5622253132157119015'
    payload={
    "FromWalletCode": wc,
    "ToWalletCode": w2,
    "Date": "20/12/2015",
    "Amount": amt,
    "Reason": "Transfer to test transaction"
    }
    payld=json.dumps(payload)
    headers = {'Authorization': 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa', "Content-Type": "application/json",'deviceID':'Onion123456789123456789', 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    print("transfer funds 1 to 2")
    response20= requests.post(url,headers=headers,data=payld)
    response20=json.loads(response20.text)
    print(response20)
    return(str(response20['Message']))

    
def banktocus(identity,wc,amt):
    w2='5622253132157119015'
    payload={
    "FromWalletCode": w2,
    "ToWalletCode": wc,
    "Date": "20/12/2015",
    "Amount": amt,
    "Reason": "Transfer to test transaction"
    }
    payld=json.dumps(payload)
    headers = {'Authorization': 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa', "Content-Type": "application/json",'deviceID':'Onion123456789123456789', 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    print("transfer funds 1 to 2")
    response9= requests.post(url,headers=headers,data=payld)
    response9=json.loads(response9.text)
    print(response9)
    return(str(response9['Message']))
    
    
    
    
    
def trans_his(identity,wc):
    url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletTransactions?walletCode='+wc+'&startDate=01/01/2015&endDate=04/11/2016&pageNum=0&pageSize=0'
    headers = {'Authorization': 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa', "Content-Type": "application/json",'deviceID':'Onion123456789123456789', 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    res=requests.get(url,headers=headers)
    res=json.loads(res.text)
    message=str(res['Message'])
    tran_hist=str(res['ListOfObjects'][1]['TranAmount'])
    return(message+'last trans'+tran_hist)
    
    
    
    
def wallet_details(identity,wc):
    url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+wc
    headers = {'Authorization': 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa', "Content-Type": "application/json",'deviceID': 'Onion123456789123456789', 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    print("wallet 1 updated info")
    response7= requests.get(url,headers=headers)
    response7=json.loads(response7.text)
    print(response7)
    message=str(response7['Message'])
    bal=str(response7['DataObject']['CurrentBalance'])
    return(message+'current balance'+bal)
    