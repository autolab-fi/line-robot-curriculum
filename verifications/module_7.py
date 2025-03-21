import cv2
import time
import os
import numpy as np

target_points = {
    'pid_half': [(100, 20), (30,0)],
    #'line_detection': [(30, 50), (30, 0)],

}

block_library_functions = {
    'pid': False,
    #'line_detection': False,
}


def get_block_library_functions(task):
    """Retrieve block library status for a given task."""
    return block_library_functions.get(task, False)


def get_target_points(task):
    """Retrieve target points for a given task."""
    return target_points.get(task, [])

def pid_half(robot, image, td: dict):
    """Test for line following with checkpoint verification and timer display."""

    # ✅ Initialize the result structure
    result = {
        "success": True,
        "description": "The robot successfully passed through the checkpoints!",
        "score": 100
    }

    # ✅ Initialize text for the user
    text = "Verifying"

    # ✅ Define checkpoint positions
    checkpoint_positions = [(270, 1120), (380, 850), (530, 1110), (740, 970)]
    
    # ✅ Initialize the test data structure
    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 10,
            "data": {
                # ✅ Dynamically initialize reached checkpoints based on the number of positions
                "reached_checkpoints": [False] * len(checkpoint_positions),
                "task_completed": False,
                "timer_start": None,   # Timer start time
                "timer_stop": None     # Timer stop time
            }
        }

    # ✅ Draw robot information
    image = robot.draw_info(image)

    # ✅ Draw red circles at checkpoints
    for i, (y, x) in enumerate(checkpoint_positions):
        # ✅ Check for list index safety
        if i < len(td["data"]["reached_checkpoints"]) and not td["data"]["reached_checkpoints"][i]:
            cv2.circle(image, (x, y), 30, (0, 0, 255), -1)  # Red circle for unchecked

    # ✅ Robot detection and checkpoint validation
    info = robot.get_info()
    robot_position_px = info.get('position_px')

    if robot_position_px:
        robot_x, robot_y = robot_position_px

        for i, (y, x) in enumerate(checkpoint_positions):
            if i < len(td["data"]["reached_checkpoints"]):
                if not td["data"]["reached_checkpoints"][i]:
                    distance = np.linalg.norm([robot_x - x, robot_y - y])
                    
                    # ✅ Check if robot reaches checkpoint
                    if distance < 50:
                        td["data"]["reached_checkpoints"][i] = True
                        
                        # ✅ Start timer on first checkpoint
                        if i == 0 and td["data"]["timer_start"] is None:
                            td["data"]["timer_start"] = time.time()

                        # ✅ Stop timer on last checkpoint
                        if i == len(checkpoint_positions) - 1:
                            td["data"]["timer_stop"] = time.time()

                        # Change circle color to green when passed
                        cv2.circle(image, (x, y), 30, (0, 255, 0), -1)  # Green circle (passed)

    # ✅ Timer logic
    elapsed_time = 0.0
    if td["data"]["timer_start"]:
        elapsed_time = time.time() - td["data"]["timer_start"]

        # ✅ Use the stop time if the robot reached the last checkpoint
        if td["data"]["timer_stop"]:
            elapsed_time = td["data"]["timer_stop"] - td["data"]["timer_start"]

    # ✅ Draw the timer at the top-right corner (BIGGER FONT)
    timer_text = f"Time: {elapsed_time:.2f} sec"
    cv2.putText(image, timer_text, (image.shape[1] - 350, 70), cv2.FONT_HERSHEY_SIMPLEX, 
                2, (0, 255, 255), 3, cv2.LINE_AA)  # Bigger size and thicker stroke

    # ✅ Check if all checkpoints are passed
    if all(td["data"]["reached_checkpoints"]):
        td["data"]["task_completed"] = True
        result.update({
            "success": True,
            "description": f"The robot successfully passed through all checkpoints",
            "score": 100
        })
        text = f"Robot passed all checkpoints"

    # ✅ Check if time has expired
    if time.time() >= td["end_time"]:
        if not all(td["data"]["reached_checkpoints"]):
            result.update({
                "success": False,
                "description": "The robot did not pass all checkpoints within time.",
                "score": 0
            })
            text = "Failed"

    # ✅ Add the elapsed time to the result description
    if td["data"]["timer_start"] and td["data"]["timer_stop"]:
        result["description"] += f" Time taken: {elapsed_time:.2f} sec."

    # ✅ Retrieve MQTT message (if any)
    msg = robot.get_msg()
    if msg:
        text = f"Message received: {msg}"

    # ✅ Return results
    return image, td, text, result


def pid_full(robot, image, td: dict):
    """Test for line following with checkpoint verification."""

    # ✅ Initialize the result structure
    result = {
        "success": True,
        "description": "The robot successfully passed through the checkpoints!",
        "score": 100
    }

    # ✅ Initialize text for the user
    text = "Verifying"

    # ✅ Define checkpoint positions
    checkpoint_positions = [(270, 1120),(400, 830),(530, 1130),(740, 970),(740,550),(400,480),(500,650),(530,250),(210, 400)]
    
    # ✅ Initialize the test data structure
    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 10,
            "data": {
                # ✅ Dynamically initialize reached checkpoints based on the number of positions
                "reached_checkpoints": [False] * len(checkpoint_positions),
                "task_completed": False
            }
        }

    # ✅ Draw robot information
    image = robot.draw_info(image)

    # ✅ Draw red circles at checkpoints
    for i, (y, x) in enumerate(checkpoint_positions):
        # ✅ Check for list index safety
        if i < len(td["data"]["reached_checkpoints"]) and not td["data"]["reached_checkpoints"][i]:
            cv2.circle(image, (x, y), 30, (0, 0, 255), -1)  # Red circle for unchecked

    # ✅ Robot detection and checkpoint validation
    info = robot.get_info()
    robot_position_px = info.get('position_px')

    if robot_position_px:
        robot_x, robot_y = robot_position_px

        for i, (y, x) in enumerate(checkpoint_positions):
            # ✅ Ensure safe access to the list
            if i < len(td["data"]["reached_checkpoints"]):
                if not td["data"]["reached_checkpoints"][i]:
                    distance = np.linalg.norm([robot_x - x, robot_y - y])
                    if distance < 50:
                        td["data"]["reached_checkpoints"][i] = True
                        # Change circle color to green when passed
                        cv2.circle(image, (x, y), 30, (0, 255, 0), -1)  # Green circle (passed)

    # ✅ Check if all checkpoints are passed
    if all(td["data"]["reached_checkpoints"]):
        td["data"]["task_completed"] = True
        result.update({
            "success": True,
            "description": "The robot successfully passed through all checkpoints!",
            "score": 100
        })
        text = "Robot passed all checkpoints!"

    # ✅ Check if time has expired
    if time.time() >= td["end_time"]:
        if not all(td["data"]["reached_checkpoints"]):
            result.update({
                "success": False,
                "description": "The robot did not pass all checkpoints within time.",
                "score": 0
            })
            text = "Failed"

    # ✅ Retrieve MQTT message (if any)
    msg = robot.get_msg()
    if msg:
        text = f"Message received: {msg}"

    # ✅ Return results
    return image, td, text, result