from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
import pandas as pd
from django.contrib.auth.decorators import login_required
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from django.contrib.auth.forms import UserCreationForm
#@login_required
def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    df=pd.read_csv(r"D:\adi docs\College_VIT______Chennai\Sixth_Semester(Winter2022_23)\MLR_Theory_Rajarajeshwari\Project\ChennaiHousingSale.csv")
    df=df[['INT_SQFT','DIST_MAINROAD','N_BEDROOM','N_ROOM','N_BATHROOM','SALES_PRICE','AREA']]
    le=LabelEncoder()
    df['AREA']=le.fit_transform(df['AREA'])
    df.dropna(subset=['INT_SQFT','DIST_MAINROAD','N_BEDROOM','N_ROOM','N_BATHROOM','SALES_PRICE','AREA'],inplace=True)
    X=df.drop('SALES_PRICE',axis=1)
    Y=df['SALES_PRICE']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)
    model=LinearRegression()
    model.fit(X_train,Y_train)
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    d1={0:"Adyar",1:"Anna Nagar",2:"Chromepet",3:"KK Nagar",4:"Karapakkam",5:"T Nagar",6:"Velachery"}
    pred = model.predict(np.array([var1,var2,var3,var4,var5,var6]).reshape(1,-1))
    pred=round(pred[0])
    price = "The predicted price is ₹"+str(pred)

    return render(request,"predict.html",{"result2":price})
    # return render(request)

def signup(request):
    if(request.method=='POST'):
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirmed password are not the same pls enter again")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('')
        
    
    return render(request,'signup.html')

def login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        print(username,pass1)
    return render(request,'login.html')

 