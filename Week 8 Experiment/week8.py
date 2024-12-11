import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the serial connection (adjust COM port and baud rate as needed)
ser = serial.Serial('COM6', 9600)

# Lists to store temperature data and time points
temperatures = []
time_stamps = []

# Initialize the plot
plt.style.use('classic')
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', label='Temperature (°C)')
ax.set_title("Real-Time Temperature Monitoring")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (°C)")
ax.legend(loc="upper left")

# Update function for the real-time plot
def update(frame):
    global temperatures, time_stamps

    try:
        # Read and decode data from the serial port
        data = ser.readline().decode('utf-8').strip()
        temperature = float(data)

        # Append new data
        temperatures.append(temperature)
        time_stamps.append(len(time_stamps))  # Use the length of the list as a simple time counter

        # Update the plot
        line.set_data(time_stamps, temperatures)
        ax.relim()
        ax.autoscale_view()

        return line,

    except ValueError:
        # Handle any data conversion errors
        print("Received invalid data:", data)
        return line,

# Set up the animation
ani = FuncAnimation(fig, update, interval=1000)  # Update every 1 second

try:
    plt.show()  # Display the plot
except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()  # Ensure the serial port is closed

