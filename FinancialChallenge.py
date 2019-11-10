import numpy as np

#Scenario: You are a Data Scientist working for a consulting firm. One of your colleges from the Auditing department has asked you to help them assess the financial statement of organization X.
#You have been supplied with two lists of data: monthly revenue and monthly expenses for the financial year in question. Your task is to calculate the following financial metrics:
#-----------------------------------------------------------------------------------------------
#1.Profit for each month
#2.profit after tax for each month (the tax is 30%)
#3.Profit margin for each month - equals to profit after tax divided by revenue
#4. Good months - where the profit after tax was greater than the mean for the year
#5. Bad months - where the profit after tax was less than the mean for the year
#6. The best month - where the profit after tax was max for the year
#7. The worst month - where the profit after tax was min for the year
#-----------------------------------------------------------------------------------------------
#Data 

revenue = np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50])
expenses = np.array([12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96])
#-----------------------------------------------------------------------------------------------

#Solution
#1. Profit for each month
profitMonthly = revenue - expenses
print("Profit for each month: {}".format(profitMonthly))
print("-------------------------------")
#-----------------------------------------------------------------------------------------------
#2.profit after tax for each month (the tax is 30%)
profitAfterTax = profitMonthly - ((profitMonthly * 30)/100)
profitAfterTax = np.around(profitAfterTax, decimals = 2)
print("Profit for each month after Tax: {}".format(profitAfterTax))
print("-------------------------------")
#-----------------------------------------------------------------------------------------------
#3.Profit margin for each month - equals to profit after tax divided by revenue
profitMargin = (profitAfterTax / revenue)*100 
profitMargin = np.around(profitMargin, decimals = 2)
print("Profit Margin for each month (%): {}".format(profitMargin))
print("-------------------------------")
#-----------------------------------------------------------------------------------------------
#6. The best month - where the profit after tax was max for the year
profitMax = np.amax(profitAfterTax)
print("The best month of profit is: {}".format(profitMax))
print("-------------------------------")
#-----------------------------------------------------------------------------------------------
#7. The worst month - where the profit after tax was min for the year
profitMin = np.amin(profitAfterTax)
print("The worst month of profit is: {}".format(profitMin))
print("-------------------------------")
#-----------------------------------------------------------------------------------------------