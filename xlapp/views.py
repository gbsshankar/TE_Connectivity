import matplotlib
matplotlib.use('Agg')
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
        total_invoice_qty=round(df['Invoice qty'].sum(),2)
        total_spent=round(df['Spend $'].sum(),2)
        #print('total_profit:',total_profit)
        #print('total_sales:',total_sales)
        ## plot 1
        df1=df.groupby('Month')['Invoice qty'].sum()
        print('df1:',df1)
        df1.plot(kind='bar')
        plt.title("Bar graph Month vs Invoice qty")
        plt.xlabel('Month')
        plt.ylabel('Invoice qty')
        
        #df.plot(kind='bar',x='Month',y='Invoice qty',color='green')
        plt.savefig('static/plot1.png',bbox_inches='tight')
        plt.cla()

        df2=df.groupby('Commodity Group')['Spend $'].sum()
        df2=df2.to_frame()
        print(df2)
        df2.plot.pie(subplots=True,autopct='%1.0f%%')
        plt.title("Pie chart for amount spent on each commodity group")
        plt.legend().remove()
        plt.savefig('static/plot2.png',bbox_inches='tight')
        plt.cla()

        df3=df.groupby('Region')['Spend $'].sum()   
        df3=df3.to_frame()
        df3.plot(kind='bar',color='green')
        #plt.xlabel('Region')
        #plt.ylabel('Spend $')
        #df["Profit"].plot(kind = 'hist') bar,hist,pie,scatter
        #df.plot()
        #df.plot(kind='scatter',x='Customer Segment',y='Unit Price')
        plt.title("Bar graph Region vs spend$")
        plt.savefig('static/plot3.png',bbox_inches='tight')
        plt.cla()

        df4=df['Invoice qty'] 
        df4.plot(kind='hist')
        #plt.xlabel('Region')
        #plt.ylabel('Spend $')
        #df["Profit"].plot(kind = 'hist') bar,hist,pie,scatter
        #df.plot()
        #df.plot(kind='scatter',x='Customer Segment',y='Unit Price')
        plt.title("Histogram for Invoice qty")
        plt.savefig('static/plot4.png',bbox_inches='tight')
        plt.cla()

        x=df['Invoice qty'] 
        y=df['Spend $'] 
        plt.scatter(x,y)
        #plt.xlabel('Region')
        #plt.ylabel('Spend $')
        #df["Profit"].plot(kind = 'hist') bar,hist,pie,scatter
        #df.plot()
        #df.plot(kind='scatter',x='Customer Segment',y='Unit Price')
        plt.title("Scatter plot for Invoice qty and $ spent")
        plt.savefig('static/plot5.png',bbox_inches='tight')
        plt.cla()

        
        context = {'total_invoice_qty':total_invoice_qty,'total_spent':total_spent,'graph': ('plot1.png','plot2.png','plot3.png','plot4.png','plot5.png')}
        return render(request,"graph.html",context)
    else:
        return render(request,"home.html")


