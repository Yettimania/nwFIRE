import subprocess 
import yaml
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from datetime import date

class History():

    def __init__(self,fname):
        with open(fname) as f:
            history = yaml.safe_load(f)

        self.dates = []
        self.networth = []
        self.financial_networth = []
        
        for key,value in history.items():
            self.dates.append(key)
            self.networth.append(value[0])
            self.financial_networth.append(value[1])

    def plot_history(self):
        fig,ax = plt.subplots()
        formatter = ticker.FormatStrFormatter('$%1.0f')
        ax.yaxis.set_major_formatter(formatter)
        ax.plot(self.dates,self.networth,color='r')
        ax.plot(self.dates,self.financial_networth,color='b')
        
        plt.title('Networth')
        plt.legend(['Networth','Financial Assets'],loc='upper left')

        for x,y in zip(self.dates,self.networth):
            
            label = "${:.0f}".format(y)

            plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),fontsize='x-small',ha='center')

        plt.xticks(rotation=70)
        plt.grid(True)
        plt.tight_layout()
        today = date.today()
        fname = today.strftime("%m-%d-%Y")
        fname = str('./historys/' + fname + '_history.png')
        plt.savefig(fname)

        subprocess.call(('xdg-open',fname))

    def forecast(self):
        present_value = self.networth[-1]
        age = int(input("What is your current age?: "))

        years = np.arange(age,61)

        percent_3 = self._compound_interest(present_value,.03,age)
        percent_5 = self._compound_interest(present_value,.05,age)
        percent_7 = self._compound_interest(present_value,.07,age)
        percent_9 = self._compound_interest(present_value,.09,age)

        dash = '-' * 67
        print(dash)
        print('RATE OF RETURN FOR CURRENT NETWORTH')
        print(dash)
        print('{:<6s}{:^11s}{:^13s}{:^16s}{:^17s}'.format('AGE','3%','5%','7%','9%'))
        print(dash)

        for idx,year in enumerate(years):
            self._print_return(year,percent_3[idx],percent_5[idx],percent_7[idx],percent_9[idx])

    def _compound_interest(self,present_value,rate,age):
        remainder = 60-age
        
        value = []
        value.append(present_value)

        for i in range(remainder):
            forecast = value[i] * (1+rate)
            value.append(forecast)

        return value

    def _print_return(self,value1,value2,value3,value4,value5):
        print('{:<6d}$ {:<12.0f}$ {:<12.0f}$ {:<12.0f}$ {:<12.0f}'.format(value1,value2,value3,value4,value5))

