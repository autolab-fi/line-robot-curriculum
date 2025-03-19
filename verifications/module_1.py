import cv2
import math
import time


def delta_points(point_0, point_1):
    return math.sqrt(((point_0[0] - point_1[0]) ** 2) +
                     ((point_0[1] - point_1[1]) ** 2))


def short_distance_race(robot, image, td: dict):
    """Test for lesson 3: Short distance race"""

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"

    if not td:
        td = {
            "end_time": time.time() + 20,
            "prev_robot_center": None,
            "goal": {
                "forward": 20,   
                "backward": 35   
            }
        }
    robot_position = robot.get_info()["position"]
    
    if td["prev_robot_center"] is not None and robot_position is not None:
        delta_pos = delta_points(robot_position, td["prev_robot_center"])
        text = f'Robot position: x: {robot_position[0]:0.1f} y: {robot_position[1]:0.1f}'

        if 'robot_start_move_time' in td and 'robot_end_move_time' not in td and delta_pos < 0.7:
            td['robot_end_move_time'] = time.time()

        ang = robot.compute_angle_robot_point(td["prev_robot_center"])
        
        direction = 'unknown'
        if 170 < ang < 190: 
            direction = 'forward'
        elif 350 < ang or ang < 10:
            direction = 'backward'

        if direction != 'unknown':
            td["goal"][direction] -= delta_pos

        if td['goal']['forward'] <= 3 and td['goal']['backward'] <= 3 and td['robot_end_move_time'] - td['robot_start_move_time'] >= 20:
            td['robot_end_move_time'] = time.time() + 3

    if (td['goal']['forward'] < 15 and td['goal']['backward'] > 5) or td['goal']['forward'] < -5 or td['goal']['backward'] < -5 or (
                td['robot_end_move_time'] - time.time() <= 2 and (td['goal']['backward'] > 5 or td['goal']['forward'] > 5)):
        result["success"] = False
        result["score"] = 0
        backward = 35 - td['goal']['backward']
        forward = 20 - td['goal']['forward']
        result["description"] = (
            f'Robot failed the task, moved {forward:.1f} cm forward, {backward:.1f} cm backward | Score: {result["score"]}'
        )

    td['prev_robot_center'] = robot_position
    return image, td, text, result
