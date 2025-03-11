import control
import matplotlib.pyplot as plt
import numpy as np

# Define the transfer function coefficients for each set
num_a = [[1], [2], [3], [4]]
# Example coefficients for four second-order systems
den_a = [[1, 1], [1, 2], [1, 3], [1, 4]]

# Create a_num figure for pole plot
plt.figure()

# Loop through each set of transfer function coefficients
for a_num, a_den in zip(num_a, den_a):
    # Create the transfer function model
    sys = control.TransferFunction(a_num, a_den)

    # Plot the poles
    poles = sys.pole()
    plt.plot(np.real(poles), np.imag(poles), 'x')

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole Plot')
plt.grid(True)

# Create a_num figure for step response plot
plt.figure()

# Loop through each set of transfer function coefficients
for a_num, a_den in zip(num_a, den_a):
    # Create the transfer function model
    sys = control.TransferFunction(a_num, a_den)

    # Compute the step response
    t, y = control.step_response(sys)

    # Plot the step response
    plt.plot(t, y)

plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.legend(['a = 1', 'a = 2', 'a = 3', 'a = 4'])
plt.show()
