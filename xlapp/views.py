from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import pandas as pd
import mpld3

# Create your views here.
def home(request):
    if request.method=="POST":
        excel_file = request.FILES["excel_file"]
        file_ext=excel_file.name.split(".")[1]
        if file_ext == 'csv':
            df=pd.read_csv(excel_file)
        else:
            df=pd.read_excel(excel_file)
        total_profit=df['Profit'].sum()
        total_sales=df['Sales'].sum()
        print('total_profit:',total_profit)
        print('total_sales:',total_sales)
        ## plot 1
        df.plot(kind='bar',x='Ship Mode',y='Order Quantity',color='green')
        plt.savefig('static/plot1.png')
        #df["Profit"].plot(kind = 'hist')
        df.plot(kind='scatter',x='Customer Segment',y='Unit Price')
        plt.savefig('static/plot2.png')
        
        
        context = {'total_profit':total_profit,'total_sales':total_sales,'bar graph': ('plot1.png','plot2.png')}
        return render(request,"graph.html",context)
    else:
        return render(request,"home.html")


