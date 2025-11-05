import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# temperature['average'].view()

# humidity.view()

# rule1.view()
# status.view(sim=stat)

temperature = ctrl.Antecedent(np.arange(-10, 55, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(40, 120, 1), 'humidity')
gases = ctrl.Antecedent(np.arange(0, 1000, 1), 'gases')
status = ctrl.Consequent(np.arange(0, 9, 1), 'Shelf Life (Months)')

# This function computes fuzzy membership values using the product of two sigmoidal membership functions
temperature['good'] = fuzz.trapmf(temperature.universe, [-10, -10, 10, 20])
temperature['average'] = fuzz.trapmf(temperature.universe, [23, 27, 60, 60])
temperature['poor'] = fuzz.trapmf(temperature.universe, [10, 20, 23, 27])

# temperature.view()
# plt.show()

humidity['average'] = fuzz.trapmf(humidity.universe, [40, 40, 55, 65])
humidity['poor'] = fuzz.trapmf(humidity.universe, [78, 85, 120, 120])
humidity['good'] = fuzz.trapmf(humidity.universe, [55, 65, 75, 85])

# humidity.view()
# plt.show()
gases['poor'] = fuzz.trapmf(gases.universe, [500, 600, 900, 1000])
gases['average'] = fuzz.trapmf(gases.universe, [100, 150, 500, 600])
gases['good'] = fuzz.trapmf(gases.universe, [0, 0, 100, 150])
# gases.view()
# plt.show()
#left center right
# status['low'].view()
# plt.show()
status['poor'] = fuzz.trapmf(status.universe, [0, 0, 1, 2])
status['average'] = fuzz.trapmf(status.universe, [1, 2, 3, 4])
status['good'] = fuzz.trapmf(status.universe, [3, 4, 8, 8])
# status.view()
# plt.show()

rule1 = ctrl.Rule(temperature['good'] & humidity['poor'] & gases['poor'], status['average'])
rule2 = ctrl.Rule(temperature['poor'] & humidity['poor'] & gases['poor'], status['poor'])
rule3 = ctrl.Rule(temperature['average'] & humidity['poor'] & gases['poor'], status['poor'])

rule4 = ctrl.Rule(temperature['good'] & humidity['poor'] & gases['average'], status['good'])
rule5 = ctrl.Rule(temperature['poor'] & humidity['poor'] & gases['average'], status['poor'])
rule6 = ctrl.Rule(temperature['average'] & humidity['poor'] & gases['average'], status['poor'])

rule7 = ctrl.Rule(temperature['good'] & humidity['poor'] & gases['good'], status['good'])
rule8 = ctrl.Rule(temperature['poor'] & humidity['poor'] & gases['good'], status['poor'])
rule9 = ctrl.Rule(temperature['average'] & humidity['poor'] & gases['good'], status['average'])

rule10 = ctrl.Rule(temperature['good'] & humidity['average'] & gases['poor'], status['average'])
rule11 = ctrl.Rule(temperature['poor'] & humidity['average'] & gases['poor'], status['poor'])
rule12 = ctrl.Rule(temperature['average'] & humidity['average'] & gases['poor'], status['poor'])

rule13 = ctrl.Rule(temperature['good'] & humidity['average'] & gases['average'], status['good'])
rule14 = ctrl.Rule(temperature['poor'] & humidity['average'] & gases['average'], status['average'])
rule15 = ctrl.Rule(temperature['average'] & humidity['average'] & gases['average'], status['average'])

rule16 = ctrl.Rule(temperature['good'] & humidity['average'] & gases['good'], status['good'])
rule17 = ctrl.Rule(temperature['poor'] & humidity['average'] & gases['good'], status['average'])
rule18 = ctrl.Rule(temperature['average'] & humidity['average'] & gases['good'], status['good'])

rule19 = ctrl.Rule(temperature['good'] & humidity['good'] & gases['poor'], status['average'])
rule20 = ctrl.Rule(temperature['poor'] & humidity['good'] & gases['poor'], status['poor'])
rule21 = ctrl.Rule(temperature['average'] & humidity['good'] & gases['poor'], status['poor'])

rule22 = ctrl.Rule(temperature['good'] & humidity['good'] & gases['average'], status['good'])
rule23 = ctrl.Rule(temperature['poor'] & humidity['good'] & gases['average'], status['average'])
rule24 = ctrl.Rule(temperature['average'] & humidity['good'] & gases['average'], status['good'])

rule25 = ctrl.Rule(temperature['good'] & humidity['good'] & gases['good'], status['good'])
rule26 = ctrl.Rule(temperature['poor'] & humidity['good'] & gases['good'], status['average'])
rule27 = ctrl.Rule(temperature['average'] & humidity['good'] & gases['good'], status['good'])


status_ctrl = ctrl.ControlSystem([
                                  rule1, rule2, rule3,
                                  rule4, rule5, rule6,
                                  rule7, rule8, rule9,
                                  rule10, rule11, rule12,
                                  rule13, rule14, rule15,
                                  rule16, rule17, rule18,
                                  rule19, rule20, rule21,
                                  rule22, rule23, rule24,
                                  rule25, rule26, rule27,
                                ])

 # status_ctrl.view()
# plt.show()
stat = ctrl.ControlSystemSimulation(status_ctrl)




def estimate_Shelf_life(temperature,humidity,gases):
    stat.input['temperature'] = temperature
    stat.input['humidity'] = humidity
    stat.input['gases'] = gases
    stat.compute()
    res = stat.output['Shelf Life (Months)']
    res=round(res, 2)
    print(f"fuzzy.py : Expected shelf life of onion is : ", res, "months")
    return res
# estimate_Shelf_life(30,60,300)
# status.view(sim=stat)
# plt.show()