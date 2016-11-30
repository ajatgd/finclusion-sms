
import requests
import json
token='qJ8Prj6nXVSxA92xVCu9c4ldekIa'
AppId='HackathonDemoApp12'

#mem1

url = 'https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/member/CreateTempMember?pageSize=0&pageNum=0'
DeviceId='Onion123456789123456789'
payload = {
   "PersonaCode": "StudentDefault"
}
payld = json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12'}
response1 = requests.post(url,headers=headers,data=payld)
response1=json.loads(response1.text)
id1=str(response1['DataObject']['InstallationID'])
print('details mem 1')
print(response1)


#wallet1
url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/CreateWallet'
payload={
   "WalletName": "wallet1"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id1}
response3= requests.post(url,headers=headers,data=payld)
response3=json.loads(response3.text)
print("wallet 1 response")
print(response3)
walletcode1=str(response3['DataObject']['WalletCode'])


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/AddValue'
payload={
   "WalletCode": walletcode1,
   "Date": "04/11/2016",
   "Amount": "100",
   "Reason": "Topup for MRT",
   "SubCategoryCode": "FundsTransfers"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id1}
response4= requests.post(url,headers=headers,data=payld)
response4=json.loads(response4.text)
print("add value to wallet 1")
print(response4)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+walletcode1
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id1}
print("wallet 1 info")
response7= requests.get(url,headers=headers)
response7=json.loads(response7.text)
print(response7)


url = 'https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/member/CreateTempMember?pageSize=0&pageNum=0'
DeviceId='Onion123456789123456789'
payload = {
   "PersonaCode": "StudentDefault"
}
payld = json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12'}
response11 = requests.post(url,headers=headers,data=payld)
response11=json.loads(response11.text)
id3=str(response1['DataObject']['InstallationID'])
print('details mem 3')
print(response11)


#wallet1
url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/CreateWallet'
payload={
   "WalletName": "wallet3"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id3}
response12= requests.post(url,headers=headers,data=payld)
response12=json.loads(response12.text)
print("wallet 1 response")
print(response12)
walletcode3=str(response12['DataObject']['WalletCode'])


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/AddValue'
payload={
   "WalletCode": walletcode3,
   "Date": "04/11/2016",
   "Amount": "100",
   "Reason": "Topup for MRT",
   "SubCategoryCode": "FundsTransfers"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id3}
response13= requests.post(url,headers=headers,data=payld)
response13=json.loads(response13.text)
print("add value to wallet 3")
print(response13)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+walletcode3
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id3}
print("wallet 3 info")
response14= requests.get(url,headers=headers)
response14=json.loads(response14.text)
print(response14)




url = 'https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/member/CreateTempMember?pageSize=0&pageNum=0'
DeviceId='Onion123456789123456789'
payload = {
   "PersonaCode": "StudentDefault"
}
payld = json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12'}
response15 = requests.post(url,headers=headers,data=payld)
response15=json.loads(response15.text)
id4=str(response1['DataObject']['InstallationID'])
print('details mem 4')
print(response15)


#wallet1
url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/CreateWallet'
payload={
   "WalletName": "wallet4"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id4}
response16= requests.post(url,headers=headers,data=payld)
response16=json.loads(response16.text)
print("wallet 4 response")
print(response16)
walletcode4=str(response16['DataObject']['WalletCode'])


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/AddValue'
payload={
   "WalletCode": walletcode4,
   "Date": "04/11/2016",
   "Amount": "1000",
   "Reason": "Topup for MRT",
   "SubCategoryCode": "FundsTransfers"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id4}
response17= requests.post(url,headers=headers,data=payld)
response17=json.loads(response17.text)
print("add value to wallet 4")
print(response17)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+walletcode3
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id4}
print("wallet 4 info")
response18= requests.get(url,headers=headers)
response18=json.loads(response18.text)
print(response18)




url = 'https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/member/CreateTempMember?pageSize=0&pageNum=0'
Authorization= 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa'
payload = {
   "PersonaCode": "StudentDefault"
}
payld = json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12'}
response2 = requests.post(url,headers=headers,data=payld)
response2=json.loads(response2.text)
id2=str(response2['DataObject']['InstallationID'])
print(response2)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/CreateWallet'
payload={
   "WalletName": "wallet2"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id2}
response5= requests.post(url,headers=headers,data=payld)
response5=json.loads(response5.text)
print("wallet 2 response")
print(response5)
walletcode2=str(response5['DataObject']['WalletCode'])


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/AddValue'
payload={
   "WalletCode": walletcode2,
   "Date": "04/11/2016",
   "Amount": "999",
   "Reason": "Topup for MRT",
   "SubCategoryCode": "FundsTransfers"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id2}
response6= requests.post(url,headers=headers,data=payld)
response6=json.loads(response6.text)
print("add value to wallet 2")
print(response6)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+walletcode2
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id2}
print("wallet 2 info")
response8= requests.get(url,headers=headers)
response8=json.loads(response8.text)
print(response8)



url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/TransferValue'
w1=walletcode1
w2=walletcode2
payload={
"FromWalletCode": w1,
"ToWalletCode": w2,
"Date": "20/12/2015",
"Amount": "10",
"Reason": "Transfer to test transaction"
}
payld=json.dumps(payload)
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id1}
print("transfer funds 1 to 2")
response9= requests.post(url,headers=headers,data=payld)
response9=json.loads(response9.text)
print(response9)


url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/GetWalletInfo?walletCode='+walletcode1
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':id1}
print("wallet 1 updated info")
response7= requests.get(url,headers=headers)
response7=json.loads(response7.text)
print(response7)
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
        if identity in id1 && wc in wallet:
            confirmpayment(identity,wc,amt)
        
    if(body[:8]=='getsubs'):
        identity=body[9:comma_index[0]]
        wc=body[comma_index[0]:]
        amt=20
        if identity in id1 && wc in wallet:
            banktocus(identity,wc,amt)
        
    r = Response()
    r.message(msg)
def confirmpayment(identity,wc,amt):
    
    w2=walletcode2
    payload={
    "FromWalletCode": wc,
    "ToWalletCode": w2,
    "Date": "20/12/2015",
    "Amount": amt,
    "Reason": "Transfer to test transaction"
    }
    payld=json.dumps(payload)
    headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    print("transfer funds 1 to 2")
    response20= requests.post(url,headers=headers,data=payld)
    response20=json.loads(response20.text)
    print(response20)

    
def banktocus(identity,wc,amt):
    w2=walletcode2
    payload={
    "FromWalletCode": w2,
    "ToWalletCode": wc,
    "Date": "20/12/2015",
    "Amount": amt,
    "Reason": "Transfer to test transaction"
    }
    payld=json.dumps(payload)
    headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json",'deviceID': DeviceId, 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    print("transfer funds 1 to 2")
    response9= requests.post(url,headers=headers,data=payld)
    response9=json.loads(response9.text)
    print(response9)
    