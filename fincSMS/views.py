from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.contrib import messages
import requests
import json
from django_twilio.decorators import twilio_view
from twilio.twiml import Response


# Create your views here.
from .models import UserData


def index(request):
	return render(request,'index.html');

def register(request):
	form=UserForm()
	return render(request,'registration.html',{'form':form});

def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request,	"Error")
        
    return HttpResponseRedirect('/')

############################################
############################################
@twilio_view
def smsRes(request):
	body=request.POST.get('Body','')
	number=request.POST.get('From','')
	id1=['I8ckg12tIqOpz613Sf/VLPClcVhOTKH2','6lAPqTztmhj/1ml4NmER+KXwJev8eMWN','I8ckg12tIqOpz613Sf/VLPClcVhOTKH2','I8ckg12tIqOpz613Sf/VLPClcVhOTKH2']
	wallet=['4817497275977414861','5622253132157119015','5243188823714477159','5014900270407291489']
    #body = request.POST.get('Body', '')
    #number = request.POST.get('From','')
    #comma_index= list(find(',',body))
    
	if(body.split(",")[0]=='payprem'):
        
		identity=body.split(",")[1]
        
		wc=body.split(",")[2]
        
		amt=20
		if (identity in id1) and (wc in wallet):
			a=confirmpayment(identity,wc,amt)
			b=wallet_details(identity,wc)
            
			msg = a+b
        
	elif(body.split(",")[0]=='getsubs'):
		identity=body.split(",")[1]
		wc=body.split(",")[2]
		amt=20
		if identity in id1 and wc in wallet:
			a=banktocus(identity,wc,amt)
			b=wallet_details(identity,wc)
			msg = a+b
            
            
	elif(body.split(",")[0]=='tranhis'):
		identity=body.split(",")[1]
		wc=body.split(",")[2]
		amt=20
		if identity in id1 and wc in wallet:
			a=trans_his(identity,wc)
			msg= a
	        
	elif(body.split(",")[0]=='knowbal'):
	    identity=body.split(",")[1]
	    wc=body.split(",")[2]
	    amt=20
	    if identity in id1 and wc in wallet:
	        a=wallet_details(identity,wc)
	        msg=a
            
    
	else:
		msg= "Invalid Request"    
	r = Response()
	r.message(msg)
	return r
def confirmpayment(identity,wc,amt):
    url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/TransferValue'

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
    
    response20= requests.post(url,headers=headers,data=payld)
    response20=json.loads(response20.text)
    
    return(str(response20['Message']))

    
def banktocus(identity,wc,amt):
    url='https://api.dev.modjadji.org:8243/tipsgo_dev/v1.0.0/api/wallet/TransferValue'

    w2='5243188823714477159'
    payload={
    "FromWalletCode": w2,
    "ToWalletCode": wc,
    "Date": "20/12/2015",
    "Amount": '10',
    "Reason": "Transfer to test transaction"
    }
    payld=json.dumps(payload)
    headers = {'Authorization': 'Bearer qJ8Prj6nXVSxA92xVCu9c4ldekIa', "Content-Type": "application/json",'deviceID':'Onion123456789123456789', 'AppId': 'HackathonDemoApp12','InstallationID':identity}
    
    response9= requests.post(url,headers=headers,data=payld)
    response9=json.loads(response9.text)
    
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
    
    response7= requests.get(url,headers=headers)
    response7=json.loads(response7.text)
    
    message=str(response7['Message'])
    bal=str(response7['DataObject']['CurrentBalance'])
    return(message+'current balance'+bal)