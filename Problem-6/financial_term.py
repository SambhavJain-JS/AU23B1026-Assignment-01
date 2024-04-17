def future_gain_improvement():
    fgi= ((annual_pofit * (ic_rate/cc_rate) ) - annual_pofit) * ((1+i)**project_life - 1)/i - improvement_cost*((1+i)**project_life)
    return fgi


def total_gain_improvement():
    
    fgi=future_gain_improvement()
    tgi=(fgi/c)

    return tgi


def annual_gain_improvement():

    tgi=total_gain_improvement()
    agi=tgi/project_life

    return agi

def calculate_ratio(number_1, number_2):
    
    ratio_numerator = number_1 / number_2
    ratio_denominator = 1
    ratio = (ratio_numerator, ratio_denominator)
    c=str(ratio[0])+':'
    d=str(ratio[1])
    return (c+d)


annual_pofit=int(input('Annual Site Profit: '))
cc_rate=int(input('Current Conversion Rate: '))
ic_rate=int(input('Improved Conversion Rate: '))
improvement_cost=int(input('Improvement Cost: '))
project_life=int(input('Expected Project Life: '))
i=0.05
c=((1+i)**project_life)
