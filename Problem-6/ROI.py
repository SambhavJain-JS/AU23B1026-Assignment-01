from financial_term import *

fg_improvement=future_gain_improvement()
print('Future Gain from Improvement: ',fg_improvement)

tg_improvement=total_gain_improvement()
print('Total Gain from Improvement: ',tg_improvement)

ag_improvement=annual_gain_improvement()
print('Annual Gain from Improvement: ',ag_improvement)

print('Annual ROI: ',calculate_ratio(ag_improvement,improvement_cost))

x=calculate_ratio(tg_improvement,improvement_cost)
print('ROI:',x)


