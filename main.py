import xlrd
import numpy as np
from matplotlib import pyplot as plt

def get_data(index, loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(index)

    l = []
    for i in range(1,8):
        l.append(sheet.cell_value(i, 10))
    
    return l

def make_tab(n,data):
    m_percent = []
    hp = []
    dps = []
    death_time = []
    total_dmg = []
    mel_hp = []

    for i in range(0,n+1):
        m_percent.append(data[3]+(data[0]/100*data[3]*i))
        hp.append(data[2]+((n-i)*data[1]/100*data[2]))
        dps.append((data[6]/data[5])*m_percent[i])
        death_time.append(hp[i]/data[4])
        total_dmg.append(death_time[i]*dps[i])
        mel_hp.append(i/n)

    return (m_percent, hp, dps, death_time, total_dmg, mel_hp)

def best_ratio(tabs):
    max_index = tabs[4].index(max(tabs[4]))
    return tabs[5][max_index]

def main():
    sheet_n = int(input("Sheet number : "))
    data = get_data(sheet_n,"Therizi_BOSS.xlsx")
    l_best = []
    
    for i in range(1,89):
        l_best.append([i,best_ratio(make_tab(i,data))])
    data = np.array(l_best)
    x, y = data.T
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    main()

