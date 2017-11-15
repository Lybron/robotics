from math import *

def update(mean1, var1, mean2, var2):
    new_var = 1/((1/var1) + (1/var2))
    new_mean = ((var2 * mean1) + (var1 * mean2))/(var1 + var2)

    return [new_mean, new_var]

print('Update test:')
print(update(10.0, 8.0, 13.0, 2.0))

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2

    return [new_mean, new_var]

print('Prediction test:')
print(predict(10.0, 4.0, 12.0, 4.0))

measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
motion = [1.0, 1.0, 2.0, 1.0, 1.0]
measurement_sig = 4.0
motion_sig = 2.0
mu = 0.0
sig = 10000.0

assert(len(measurements) == len(motion)), 'measurements and motions be equal length'

for i in range(len(motion)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    print('update: ', [mu, sig])

    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    print('predict: ', [mu, sig])
