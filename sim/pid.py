import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

class LineFollowerSimulation:
    def __init__(self):
        # Create the figure and axis
        plt.style.use('dark_background')  # Modern dark theme
        self.fig, self.ax = plt.subplots(figsize=(12, 10))
        plt.subplots_adjust(bottom=0.25)
        
        # Set up the plot
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.set_aspect('equal')
        self.ax.set_title('Effects of P, I, and D values on Robot\'s movement', fontsize=16, pad=20)
        self.ax.grid(True, alpha=0.3, linestyle='--')
        
        # Hide axis numbers and ticks but keep grid
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.tick_params(axis='both', which='both', length=0)
        
        # Path parameters
        self.path = self.generate_path()
        self.path_length = len(self.path)
        
        # Plot the path
        self.line, = self.ax.plot(self.path[:, 0], self.path[:, 1], color='#00FFFF', lw=3, alpha=0.8)
        
        # Add background for aesthetics
        self.bg = patches.Rectangle((-5, -5), 10, 10, color='#111122', zorder=-10)
        self.ax.add_patch(self.bg)
        
        # Robot parameters
        self.path_index = 0
        self.robot_x = self.path[0, 0]
        self.robot_y = self.path[0, 1]
        self.robot_angle = 0
        self.robot_speed = 0.05
        self.wheel_base = 0.4  # Distance between wheels
        
        # Sensor parameters
        self.num_sensors = 8  # Changed to 8 sensors
        self.sensor_spread = 0.6  # Total width of sensor array (widened for more sensors)
        self.sensor_positions = np.zeros((self.num_sensors, 2))
        self.sensor_values = np.zeros(self.num_sensors)
        self.sensor_dots = []
        
        # PID parameters
        self.kp = 1.0
        self.ki = 0.0
        self.kd = 0.5
        self.integral = 0
        self.prev_error = 0
        
        # Path tracking parameters
        self.lookahead = 10
        self.current_target_idx = min(self.lookahead, self.path_length - 1)
        
        # Create robot representation
        self.robot_body = patches.Circle((self.robot_x, self.robot_y), 0.2, fc='blue')
        self.ax.add_patch(self.robot_body)
        
        # Create sensor representations
        for i in range(self.num_sensors):
            sensor = patches.Circle((0, 0), 0.04, fc='red')  # Slightly smaller sensors
            self.ax.add_patch(sensor)
            self.sensor_dots.append(sensor)
        
        # Direction indicator
        self.direction, = self.ax.plot([], [], 'g-', lw=2)
        
        # Target point (for visualization)
        self.target_point, = self.ax.plot([], [], 'ro', markersize=5)
        
        # Sensor reading visualization
        self.sensor_reading_bars = []
        for i in range(self.num_sensors):
            bar = self.ax.bar(i, 0, width=0.4, bottom=-6, color='blue', alpha=0.7)[0]
            self.sensor_reading_bars.append(bar)
        
        # Create sliders for PID control
        self.ax_kp = plt.axes([0.25, 0.2, 0.65, 0.03])
        self.ax_ki = plt.axes([0.25, 0.15, 0.65, 0.03])
        self.ax_kd = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.ax_speed = plt.axes([0.25, 0.05, 0.65, 0.03])
        
        self.slider_kp = Slider(self.ax_kp, 'Kp', 0.0, 5.0, valinit=self.kp)
        self.slider_ki = Slider(self.ax_ki, 'Ki', 0.0, 5.0, valinit=self.ki)
        self.slider_kd = Slider(self.ax_kd, 'Kd', 0.0, 5.0, valinit=self.kd)
        self.slider_speed = Slider(self.ax_speed, 'Speed', 0.01, 0.2, valinit=self.robot_speed)
        
        self.slider_kp.on_changed(self.update_kp)
        self.slider_ki.on_changed(self.update_ki)
        self.slider_kd.on_changed(self.update_kd)
        self.slider_speed.on_changed(self.update_speed)
        
        # Error display - replace the existing line with these lines
        self.error_text = self.ax.text(
            0.75, 0.95, '', 
            transform=self.ax.transAxes,
            fontsize=10,
            fontfamily='monospace',
            verticalalignment='top',
            bbox=dict(
                boxstyle='round,pad=0.5',
                facecolor='black',
                alpha=0.7,
                edgecolor='cyan'
            )
        )
        
        # Animation
        self.animation = FuncAnimation(self.fig, self.update, interval=50, blit=False)
    
    def generate_path(self):
        # Generate a complex path with curves and turns
        t = np.linspace(0, 2*np.pi, 500)
        
        # Base circle
        x = 3 * np.cos(t)
        y = 3 * np.sin(t)
        
        # Add some variation to make the path more challenging
        x += 0.2 * np.sin(3*t)
        y += 0.5 * np.cos(5*t)
        
        return np.column_stack((x, y))
    
    def update_sensor_positions(self):
        # Calculate sensor positions based on robot position and orientation
        sensor_x_offsets = np.linspace(-self.sensor_spread/2, self.sensor_spread/2, self.num_sensors)
        for i in range(self.num_sensors):
            # Position sensors in front of the robot
            forward_offset = 0.3
            # Calculate sensor position in robot's coordinate frame
            x_local = forward_offset
            y_local = sensor_x_offsets[i]
            # Transform to global coordinates
            cos_angle = np.cos(self.robot_angle)
            sin_angle = np.sin(self.robot_angle)
            x_global = self.robot_x + x_local * cos_angle - y_local * sin_angle
            y_global = self.robot_y + x_local * sin_angle + y_local * cos_angle
            
            self.sensor_positions[i] = [x_global, y_global]
            self.sensor_dots[i].center = (x_global, y_global)
    
    def read_sensors(self):
        # Calculate sensor readings based on distance to path
        max_distance = 0.4  # Maximum distance at which sensors can detect the line
        
        for i, sensor_pos in enumerate(self.sensor_positions):
            # Find minimum distance from sensor to any point on the path
            distances = np.sqrt((self.path[:, 0] - sensor_pos[0])**2 + 
                               (self.path[:, 1] - sensor_pos[1])**2)
            min_distance = np.min(distances)
            
            # Calculate sensor value (1 when on the line, 0 when far from the line)
            # Using an exponential falloff for more realistic sensor behavior
            self.sensor_values[i] = np.exp(-min_distance**2 / (2 * (max_distance/3)**2))
            
            # Update sensor visualization
            # Color based on detection intensity
            intensity = self.sensor_values[i]
            if intensity > 0.75:
                color = 'red'
            elif intensity > 0.5:
                color = 'orange'
            elif intensity > 0.25:
                color = 'yellow'
            else:
                color = 'gray'
                
            self.sensor_dots[i].set_facecolor(color)
            
            # Update sensor reading bar
            self.sensor_reading_bars[i].set_height(self.sensor_values[i])
            self.sensor_reading_bars[i].set_color(color)
    
    def calculate_error(self):
        # Calculate weighted average of sensor positions
        # This gives us an estimate of the line position relative to the robot
        weighted_sum = 0
        total_weight = np.sum(self.sensor_values)
        
        if total_weight < 0.1:
            # No sensors detecting the line well, use the last error
            # This helps the robot recover when it loses the line
            return self.prev_error * 1.5, self.path[self.current_target_idx]  # Amplify the last error to help recovery
        
        # Calculate the weighted average position
        # Map sensor positions to values from -1 (leftmost) to 1 (rightmost)
        sensor_positions_normalized = np.linspace(-1, 1, self.num_sensors)
        
        for i in range(self.num_sensors):
            weighted_sum += sensor_positions_normalized[i] * self.sensor_values[i]
        
        # Calculate the error as the weighted average position
        # Negative error means the line is to the left, positive means to the right
        error = weighted_sum / total_weight
        
        # Find the target point on the path for visualization
        closest_distances = np.sqrt((self.path[:, 0] - self.robot_x)**2 + 
                                   (self.path[:, 1] - self.robot_y)**2)
        closest_idx = np.argmin(closest_distances)
        self.current_target_idx = (closest_idx + self.lookahead) % self.path_length
        target_point = self.path[self.current_target_idx]
        
        return error, target_point
    
    def pid_control(self, error):
        # PID control calculation
        self.integral += error
        derivative = error - self.prev_error
        
        # Limit integral to prevent wind-up
        self.integral = np.clip(self.integral, -2, 2)
        
        # Calculate steering adjustment
        steering = self.kp * error + self.ki * self.integral + self.kd * derivative
        
        # Limit steering to reasonable values
        steering = np.clip(steering, -0.15, 0.15)
        
        self.prev_error = error
        return steering
    
    def update(self, frame):
        # Update sensor positions
        self.update_sensor_positions()
        
        # Read sensors
        self.read_sensors()
        
        # Calculate error
        error, target_point = self.calculate_error()
        
        # Apply PID control
        steering = self.pid_control(error)
        
        # Update robot position and orientation
        self.robot_angle += steering
        
        # Move robot forward
        self.robot_x += self.robot_speed * np.cos(self.robot_angle)
        self.robot_y += self.robot_speed * np.sin(self.robot_angle)
        
        # Update robot visualization
        self.robot_body.center = (self.robot_x, self.robot_y)
        
        # Update direction indicator
        dir_x = [self.robot_x, self.robot_x + 0.5 * np.cos(self.robot_angle)]
        dir_y = [self.robot_y, self.robot_y + 0.5 * np.sin(self.robot_angle)]
        self.direction.set_data(dir_x, dir_y)
        
        # Update target point visualization
        self.target_point.set_data([target_point[0]], [target_point[1]])
        
        # Update error text
        pid_p = self.kp * error
        pid_i = self.ki * self.integral
        pid_d = self.kd * (error - self.prev_error)
        
        # Create a fixed-width info box with consistent formatting
        info_str = (
            f"CONTROL PARAMETERS\n"
            f"───────────────────\n"
            f"Error      : {error:+7.2f}\n"
            f"P-term     : {pid_p:+7.2f}\n"
            f"I-term     : {pid_i:+7.2f}\n" 
            f"D-term     : {pid_d:+7.2f}\n"
            f"Steering   : {steering:+7.2f}"
        )
        
        self.error_text.set_text(info_str)
        
        return (self.robot_body, self.direction, self.target_point, self.error_text, 
                *self.sensor_dots, *self.sensor_reading_bars)
    
    def update_kp(self, val):
        self.kp = val
    
    def update_ki(self, val):
        self.ki = val
        self.integral = 0  # Reset integral term when changing parameters
    
    def update_kd(self, val):
        self.kd = val
    
    def update_speed(self, val):
        self.robot_speed = val
    
    def run(self):
        plt.show()

# Run the simulation
if __name__ == "__main__":
    simulation = LineFollowerSimulation()
    simulation.run()