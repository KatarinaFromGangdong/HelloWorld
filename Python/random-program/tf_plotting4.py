import control
import matplotlib.pyplot as plt

# Define the transfer function coefficients
a = 4
b = 25

# Create the transfer function model
sys = control.TransferFunction([b], [1, a, b])

# Evaluate parameters for the original transfer function
os, ts, tp, zeta, wn, tr = control.step_response(
    sys, return_characteristics=True)
print("Original Transfer Function:")
print("Percent Overshoot: {:.2f}%".format(os * 100))
print("Settling Time: {:.2f}".format(ts))
print("Peak Time: {:.2f}".format(tp))
print("Damping Ratio: {:.2f}".format(zeta))
print("Natural Frequency: {:.2f}".format(wn))
print("Rise Time: {:.2f}".format(tr))

# Plot the poles
poles = sys.pole()
plt.figure()
plt.plot(poles.real, poles.imag, 'x')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole Plot')
plt.grid(True)

# Increase the real part of the poles by a factor of 2
sys_new = control.TransferFunction([b], [1, 2 * a, b])
poles_new = sys_new.pole()
os_new, ts_new, tp_new, zeta_new, wn_new, tr_new = control.step_response(
    sys_new)
print("\nTransfer Function with Real Part Doubled:")
print("Percent Overshoot: {:.2f}%".format(os_new * 100))
print("Settling Time: {:.2f}".format(ts_new))
print("Peak Time: {:.2f}".format(tp_new))
print("Damping Ratio: {:.2f}".format(zeta_new))
print("Natural Frequency: {:.2f}".format(wn_new))
print("Rise Time: {:.2f}".format(tr_new))

# Increase the real part of the poles by half
sys_half = control.TransferFunction([b], [1, 0.5 * a, b])
poles_half = sys_half.pole()
os_half, ts_half, tp_half, zeta_half, wn_half, tr_half = control.step_response(
    sys_half)
print("\nTransfer Function with Real Part Increased by Half:")
print("Percent Overshoot: {:.2f}%".format(os_half * 100))
print("Settling Time: {:.2f}".format(ts_half))
print("Peak Time: {:.2f}".format(tp_half))
print("Damping Ratio: {:.2f}".format(zeta_half))
print("Natural Frequency: {:.2f}".format(wn_half))
print("Rise Time: {:.2f}".format(tr_half))

# Plot the step responses
t, y = control.step_response(sys)
t_new, y_new = control.step_response(sys_new)
t_half, y_half = control.step_response(sys_half)
plt.figure()
plt.plot(t, y, label='Original')
plt.plot(t_new, y_new, label='Real Part Doubled')
plt.plot(t_half, y_half, label='Real Part Increased by Half')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.legend()
plt.grid(True)
plt.show()
