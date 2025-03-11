import control
import matplotlib.pyplot as plt

# Define the transfer function coefficients
a = 4
b = 25

# Create the transfer function model
sys = control.TransferFunction([b], [1, a, b])

# Evaluate performance metrics for the initial transfer function
info = control.step_info(sys)
percent_overshoot = info['Overshoot']
settling_time = info['SettlingTime']
peak_time = info['PeakTime']
rise_time = info['RiseTime']

# Plot the step response for the initial transfer function
t, y = control.step_response(sys)
plt.plot(t, y)

# Define the updated transfer function coefficients (increased real part)
a_updated = a * 2
b_updated = b

# Create the updated transfer function model
sys_updated = control.TransferFunction([b_updated], [1, a_updated, b_updated])

# Evaluate performance metrics for the updated transfer function (increased real part)
info_updated = control.step_info(sys_updated)
percent_overshoot_updated = info_updated['Overshoot']
settling_time_updated = info_updated['SettlingTime']
peak_time_updated = info_updated['PeakTime']
rise_time_updated = info_updated['RiseTime']

# Plot the step response for the updated transfer function (increased real part)
t_updated, y_updated = control.step_response(sys_updated)
plt.plot(t_updated, y_updated)

# Define the updated transfer function coefficients (decreased real part)
a_updated = a / 2
b_updated = b

# Create the updated transfer function model
sys_updated = control.TransferFunction([b_updated], [1, a_updated, b_updated])

# Evaluate performance metrics for the updated transfer function (decreased real part)
info_updated = control.step_info(sys_updated)
percent_overshoot_updated2 = info_updated['Overshoot']
settling_time_updated2 = info_updated['SettlingTime']
peak_time_updated2 = info_updated['PeakTime']
rise_time_updated2 = info_updated['RiseTime']

# Plot the step response for the updated transfer function (decreased real part)
t_updated, y_updated2 = control.step_response(sys_updated)
plt.plot(t_updated, y_updated2)

# Set labels, title, and legend for the plot
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.legend(['Initial', 'Increased Real Part', 'Decreased Real Part'])
plt.grid(True)
plt.show()

# Print performance metrics for the initial and updated transfer functions
print("Initial Transfer Function:")
print("Percent Overshoot:", percent_overshoot)
print("Settling Time:", settling_time)
print("Peak Time:", peak_time)
print("Rise Time:", rise_time)
print()
print("Transfer Function with Increased Real Part:")
print("Percent Overshoot:", percent_overshoot_updated)
print("Settling Time:", settling_time_updated)
print("Peak Time:", peak_time_updated)
print("Rise Time:", rise_time_updated)
print()
print("Transfer Function with Decreased Real Part:")
print("Percent Overshoot:", percent_overshoot_updated2)
print("Settling Time:", settling_time_updated2)
print("Peak Time:", peak_time_updated2)
print("Rise Time:", rise_time_updated2)
