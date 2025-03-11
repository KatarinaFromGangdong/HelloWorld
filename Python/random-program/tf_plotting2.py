import control
import matplotlib.pyplot as plt
import math

# Define the transfer function coefficients
a = 4
b = 25

# Create the transfer function model
num = [b]
den = [1, a, b]
sys = control.TransferFunction(num, den)

# Evaluate the performance parameters for the original transfer function
info = control.step_info(sys)
overshoot = info['Overshoot']
settling_time = info['SettlingTime']
peak_time = info['PeakTime']
rise_time = info['RiseTime']

# Plot the poles for the original transfer function
poles = sys.pole()
plt.figure()
plt.plot(poles.real, poles.imag, 'x')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole Plot')
plt.grid(True)

# Define the modified transfer functions
a_modified = a
b_modified = 2 * b
sys_modified_1 = control.TransferFunction(num, [1, a_modified, b_modified])

a_modified = a
b_modified = 4 * b
sys_modified_2 = control.TransferFunction(num, [1, a_modified, b_modified])

# Damping ratio (approximated from percent overshoot)
zeta = info['Overshoot'] / 100
wn = 4 / (zeta * info['SettlingTime'])  # Natural frequency

# Evaluate the performance parameters for the modified transfer functions
info_modified_1 = control.step_info(sys_modified_1)
overshoot_modified_1 = info_modified_1['Overshoot']
settling_time_modified_1 = info_modified_1['SettlingTime']
peak_time_modified_1 = info_modified_1['PeakTime']
rise_time_modified_1 = info_modified_1['RiseTime']
zeta_1 = info_modified_1['Overshoot'] / 100
wn_1 = 4/(zeta_1*settling_time_modified_1)

info_modified_2 = control.step_info(sys_modified_2)
overshoot_modified_2 = info_modified_2['Overshoot']
settling_time_modified_2 = info_modified_2['SettlingTime']
peak_time_modified_2 = info_modified_2['PeakTime']
rise_time_modified_2 = info_modified_2['RiseTime']
zeta_2 = info_modified_2['Overshoot'] / 100
wn_2 = 4/(zeta_2*settling_time_modified_2)

# Plot the step responses for all transfer functions
t, y = control.step_response(sys)
t_modified_1, y_modified_1 = control.step_response(sys_modified_1)
t_modified_2, y_modified_2 = control.step_response(sys_modified_2)

plt.figure()
plt.plot(t, y, label='Original')
plt.plot(t_modified_1, y_modified_1, label='increased by 2')
plt.plot(t_modified_2, y_modified_2, label='increased by 4')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.legend()

# Display the results
print("Original Transfer Function:")
print("Overshoot: {:.2f}%".format(overshoot))
print("Settling Time: {:.2f}".format(settling_time))
print("Peak Time: {:.2f}".format(peak_time))
print("Rise Time: {:.2f}".format(rise_time))
print("\n")

print("Imaginary Part Increased by 2:")
print("Overshoot: {:.2f}%".format(overshoot_modified_1))
print("Settling Time: {:.2f}".format(settling_time_modified_1))
print("Peak Time: {:.2f}".format(peak_time_modified_1))
print("Rise Time: {:.2f}".format(rise_time_modified_1))
print("Damping Ratio: {:.2f}".format(zeta_1))
print("Natural Frequency: {:.2f}".format(math.sqrt(wn_1)))
print("\n")

print("Imaginary Part Increased by 4:")
print("Overshoot: {:.2f}%".format(overshoot_modified_2))
print("Settling Time: {:.2f}".format(settling_time_modified_2))
print("Peak Time: {:.2f}".format(peak_time_modified_2))
print("Rise Time: {:.2f}".format(rise_time_modified_2))
print("Damping Ratio: {:.2f}".format(zeta_2))
print("Natural Frequency: {:.2f}".format(math.sqrt(wn_2)))

plt.show()
