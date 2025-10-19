import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import os


def calc_pa(df, years):
  periods=252*years
  # calculate the rolling yearly revenue r = (A/K)^(1/d) - 1
  # info: the pct_change is already the percentage A/K-1, therefore +1 for correct calculation of r
  rolling_revenue = df.pct_change(periods=periods) + 1
  rolling_revenue = (rolling_revenue.pow(1/years) -1 ) * 100
  rolling_revenue = rolling_revenue.shift(-periods)

  # rolling average yearly revenue
  rolling_avg = rolling_revenue.rolling(window=int(periods/2)).mean()

  # longtime average of all yearly revenues
  avg_revenue = np.mean(rolling_revenue)
  return rolling_revenue, rolling_avg, avg_revenue

def plot_revenue(rolling_revenue, rolling_avg, avg_revenue, years):
  plt.style.use('default')
  plt.rcParams['font.size'] = '16'
  fig, ax1 = plt.subplots(figsize=(15, 7))
  ax1.plot(rolling_revenue.index, rolling_revenue, label="MSCI World Revenue", linewidth=1)
  ax1.plot(rolling_avg.index, rolling_avg, linewidth=1, linestyle='dotted', label="Rolling Average")

  # mark areas < 0 red
  ymin = plt.gca().get_ylim()[0]
  ax1.fill_between(x=rolling_revenue.index,y1=rolling_revenue['^990100-USD-STRD'], where=(rolling_revenue['^990100-USD-STRD'] < 0), color='red', alpha=0.45)

  ax2 = ax1.twinx()
  ax2.plot(yf_msciw.index, yf_msciw, label="MSCI World", linewidth=1, linestyle='dotted', color='grey', alpha=0.3)
  ax2.set_yscale('log', base=2)
  ax2.set_axis_off()

  # special lines: y=0, y=avg and average label
  avg_1yr_revenue_label = "Average " + str(round(avg_revenue,2)) + "%"
  ax1.axhline(y=avg_revenue, label=avg_1yr_revenue_label, color="red")
  ax1.set_ylabel('%')
  xaxis_formatting(ax1)
  #plt.yscale('log')
  # plt.title('Rollierende jährliche Rendite nach ' +  str(years) + ' Jahre')
  plt.tight_layout()
  plt.savefig(os.path.dirname(__file__) + '/msci-world-rolling_revenue_' + str(years) + '.svg', format='svg')

def xaxis_formatting(xaxis):
  xaxis.axhline(y=0, color="black")
  # plt.text('1972', -10, 'Generiert am für florian-staubach.de', ha='right', va='bottom', color='grey', alpha=0.5, fontsize=10)
  xaxis.set_xlabel('Year')
  xaxis.xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
  xaxis.xaxis.set_minor_locator(matplotlib.dates.YearLocator())
  xaxis.margins(x=0)
  xaxis.legend()
  xaxis.grid(True)

# get the data with set start and enddate
start=datetime.datetime(1972,2,1)
end=datetime.datetime.now()
yf_msciw = yf.download(tickers=['^990100-USD-STRD'], start=start, end=end)['Close']

# Drop rows with missing values
# yf_msciw.dropna(inplace=True)

fig, ax1 = plt.subplots(figsize=(15, 6))
ax1.plot(yf_msciw.index, yf_msciw, label="MSCI World")
ax1.set_ylabel('USD')
ax1.set_yscale('log', base=10)
ax1.yaxis.set_major_formatter(matplotlib.ticker.LogFormatter(base=10))
xaxis_formatting(ax1)
plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + '/msci-world.svg', format='svg')

# calculate maximum drawdowns
cumulative_max = yf_msciw.cummax()
drawdown = (yf_msciw - cumulative_max) / cumulative_max * 100
fig, ax1 = plt.subplots(figsize=(15, 6))
ax1.plot(drawdown.index, drawdown, color='red', label='Drawdown (%)')
ax1.set_ylabel('%')
xaxis_formatting(ax1)
plt.tight_layout()
plt.savefig(os.path.dirname(__file__) + '/msci-world-max_drawdown.svg', format='svg')

# Calculate 1-year rolling revenue (percentage change)
rolling_1yr_revenue, rolling_1yr_avg, avg_1yr_revenue = calc_pa(yf_msciw, 1)
plot_revenue(rolling_1yr_revenue, rolling_1yr_avg, avg_1yr_revenue, 1)

# Calculate 5-year rolling revenue (percentage change)
rolling_5yr_revenue, rolling_5yr_avg, avg_5yr_revenue = calc_pa(yf_msciw, 5)
plot_revenue(rolling_5yr_revenue, rolling_5yr_avg, avg_5yr_revenue, 5)

# Calculate 10-year rolling revenue (percentage change)
rolling_10yr_revenue, rolling_10yr_avg, avg_10yr_revenue = calc_pa(yf_msciw, 10)
plot_revenue(rolling_10yr_revenue, rolling_10yr_avg, avg_10yr_revenue, 10)

# Calculate 20-year rolling revenue (percentage change)
rolling_20yr_revenue, rolling_20yr_avg, avg_20yr_revenue = calc_pa(yf_msciw, 20)
plot_revenue(rolling_20yr_revenue, rolling_20yr_avg, avg_20yr_revenue, 20)
