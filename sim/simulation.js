class LineFollowerSimulation {
  constructor() {
    this.canvas = document.getElementById("simulationCanvas");
    this.ctx = this.canvas.getContext("2d");

    // Set canvas size
    this.canvas.width = 500;
    this.canvas.height = 500;

    // Initialize parameters
    this.initializeParameters();
    this.setupControls();
    this.generatePath();

    // Start animation
    this.animate();
  }

  initializeParameters() {
    // Robot parameters
    this.robotX = this.path ? this.path[0].x : 0;
    this.robotY = this.path ? this.path[0].y : 0;
    this.robotAngle = 0;
    this.robotSpeed = parseFloat(document.getElementById("speed").value);
    this.wheelBase = 0.4;

    // Sensor parameters
    this.numSensors = 8;
    this.sensorSpread = 0.6;
    this.sensorPositions = new Array(this.numSensors)
      .fill()
      .map(() => ({ x: 0, y: 0 }));
    this.sensorValues = new Array(this.numSensors).fill(0);

    // PID parameters
    this.kp = parseFloat(document.getElementById("kp").value);
    this.ki = parseFloat(document.getElementById("ki").value);
    this.kd = parseFloat(document.getElementById("kd").value);
    this.integral = 0;
    this.prevError = 0;

    // Path tracking
    this.lookahead = 10;
    this.currentTargetIdx = 0;

    // Scale factor for drawing
    this.scale = 70; // Pixels per unit
    this.centerX = this.canvas.width / 2;
    this.centerY = this.canvas.height / 2;
  }

  generatePath() {
    this.path = [];
    const numPoints = 500;
    for (let i = 0; i < numPoints; i++) {
      const t = (i / numPoints) * Math.PI * 2;
      // Base circle with variations
      let x = 3 * Math.cos(t) + 0.2 * Math.sin(3 * t);
      let y = 3 * Math.sin(t) + 0.5 * Math.cos(5 * t);
      this.path.push({ x, y });
    }

    // Initialize robot position
    this.robotX = this.path[0].x;
    this.robotY = this.path[0].y;
  }

  setupControls() {
    // Set up slider event listeners
    ["kp", "ki", "kd", "speed"].forEach((param) => {
      const slider = document.getElementById(param);
      const display = document.getElementById(`${param}Value`);

      slider.addEventListener("input", (e) => {
        // this[param] = parseFloat(e.target.value);
        switch (param) {
          case "speed":
            this.updateSpeed(parseFloat(e.target.value));
          case "kp":
            this.updateKp(parseFloat(e.target.value));
          case "ki":
              this.updateKi(parseFloat(e.target.value));
          case "kd":
            this.updateKd(parseFloat(e.target.value));
          default:
            break;
        }
        display.textContent = e.target.value;
      });
    });
  }
  updateKp(val) {
    this.kp = val;
  }
  updateKi(val) {
    this.ki = val;
  }
  updateKd(val) {
    this.kd = val;
  }
  updateSpeed(val) {
    this.robotSpeed = val;
  }
  updateSensorPositions() {
    const sensorOffsets = Array.from(
      { length: this.numSensors },
      (_, i) =>
        -this.sensorSpread / 2 +
        (this.sensorSpread * i) / (this.numSensors - 1),
    );

    for (let i = 0; i < this.numSensors; i++) {
      const forwardOffset = 0.3;
      const xLocal = forwardOffset;
      const yLocal = sensorOffsets[i];

      const cosAngle = Math.cos(this.robotAngle);
      const sinAngle = Math.sin(this.robotAngle);

      this.sensorPositions[i] = {
        x: this.robotX + xLocal * cosAngle - yLocal * sinAngle,
        y: this.robotY + xLocal * sinAngle + yLocal * cosAngle,
      };
    }
  }

  readSensors() {
    const maxDistance = 0.4;

    this.sensorValues = this.sensorPositions.map((sensorPos) => {
      // Find minimum distance to path
      let minDistance = Infinity;
      for (const pathPoint of this.path) {
        const distance = Math.sqrt(
          Math.pow(pathPoint.x - sensorPos.x, 2) +
            Math.pow(pathPoint.y - sensorPos.y, 2),
        );
        minDistance = Math.min(minDistance, distance);
      }

      // Calculate sensor value with exponential falloff
      return Math.exp(
        -Math.pow(minDistance, 2) / (2 * Math.pow(maxDistance / 3, 2)),
      );
    });
  }

  calculateError() {
    const totalWeight = this.sensorValues.reduce((sum, val) => sum + val, 0);

    if (totalWeight < 0.1) {
      return this.prevError * 1.5;
    }

    const sensorPositionsNormalized = Array.from(
      { length: this.numSensors },
      (_, i) => -1 + (2 * i) / (this.numSensors - 1),
    );

    const weightedSum = this.sensorValues.reduce(
      (sum, val, i) => sum + val * sensorPositionsNormalized[i],
      0,
    );

    return weightedSum / totalWeight;
  }

  pidControl(error) {
    this.integral += error;
    this.integral = Math.max(-2, Math.min(2, this.integral));

    const derivative = error - this.prevError;
    const steering =
      this.kp * error + this.ki * this.integral + this.kd * derivative;

    this.prevError = error;
    return Math.max(-0.15, Math.min(0.15, steering));
  }

  draw() {
    // Clear canvas
    this.ctx.fillStyle = "#111122";
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw path
    this.ctx.beginPath();
    this.ctx.strokeStyle = "#00FFFF";
    this.ctx.lineWidth = 3;
    this.path.forEach((point, i) => {
      const screenX = this.centerX + point.x * this.scale;
      const screenY = this.centerY + point.y * this.scale;
      if (i === 0) this.ctx.moveTo(screenX, screenY);
      else this.ctx.lineTo(screenX, screenY);
    });
    this.ctx.stroke();

    // Draw robot
    this.ctx.beginPath();
    this.ctx.fillStyle = "blue";
    this.ctx.arc(
      this.centerX + this.robotX * this.scale,
      this.centerY + this.robotY * this.scale,
      0.2 * this.scale,
      0,
      Math.PI * 2,
    );
    this.ctx.fill();

    // Draw sensors
    this.sensorPositions.forEach((pos, i) => {
      const intensity = this.sensorValues[i];
      this.ctx.beginPath();
      this.ctx.fillStyle =
        intensity > 0.75
          ? "red"
          : intensity > 0.5
            ? "orange"
            : intensity > 0.25
              ? "yellow"
              : "gray";
      this.ctx.arc(
        this.centerX + pos.x * this.scale,
        this.centerY + pos.y * this.scale,
        0.04 * this.scale,
        0,
        Math.PI * 2,
      );
      this.ctx.fill();
    });
  }

  animate() {
    // Update simulation
    this.updateSensorPositions();
    this.readSensors();
    const error = this.calculateError();
    const steering = this.pidControl(error);

    // Update robot position
    this.robotAngle += steering;
    this.robotX += this.robotSpeed * Math.cos(this.robotAngle);
    this.robotY += this.robotSpeed * Math.sin(this.robotAngle);

    // Draw everything
    this.draw();

    // Continue animation
    requestAnimationFrame(() => this.animate());
  }
}

// Start simulation when page loads
window.onload = () => {
  new LineFollowerSimulation();
};
