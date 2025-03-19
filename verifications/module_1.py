import cv2
import math
import time
import os
import numpy as np


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
            f'Robot failed the task, moved {forward:.1f} cm forward, {backward:.1f} cm backward | Score: {result["score"]}')

    td['prev_robot_center'] = robot_position
    return image, td, text, result


def maneuvering(robot, image, td: dict):
    """Test for lesson 4: Maneuvering"""

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100  
    }
    text = "Not recognized"

    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 12,
            "target_angle": [
                {"left": 90, "right": 0},
                {"left": 90, "right": 0},
                {"left": 0, "right": 90}
            ]
        }

    min_for_error = 15
    min_for_change_point = 5
    robot_position = robot.get_info()["position"]

    if robot is not None:
        ang = robot.compute_angle_x(robot)

        if 'ang_0' in td:
            if td['ang_0'] < 90 and ang > 300:
                td['ang_0'] = 360 + td['ang_0']
            elif td['ang_0'] > 300 and ang < 90:
                td['ang_0'] -= 360

            delta_ang = ang - td['ang_0']

            if delta_ang < 0:
                td['target_angle'][-1]['right'] += delta_ang
            else:
                td['target_angle'][-1]['left'] -= delta_ang

        if (
            td['target_angle'][-1]['left'] < min_for_change_point and
            td['target_angle'][-1]['right'] < min_for_change_point
        ):
            if len(td['target_angle']) > 1:
                td['target_angle'].pop()
            elif td["end_time"] - td["start_time"] == 12:
                td["end_time"] = time.time() + 1

        text = f"Current angle with x-axis: {ang:0.0f}"
        td['ang_0'] = ang

    if (
        td['target_angle'][-1]['left'] < -min_for_error or
        td['target_angle'][-1]['right'] < -min_for_error or
        (
            td['end_time'] - time.time() < 2 and
            (
                td['target_angle'][0]['right'] > min_for_error or
                td['target_angle'][0]['left'] > min_for_error
            )
        )
    ):
        result["success"] = False
        result["score"] = 0 
        result["description"] = (
            f"It is disappointing, but robot failed the task. "
            f"The robot had to turn more: "
        )

        for i in range(len(td['target_angle']) - 1, -1, -1):
            if abs(td['target_angle'][i]['right']) > min_for_change_point:
                result["description"] += (
                    f"{int(td['target_angle'][i]['right'])} degrees right; "
                )
            if abs(td['target_angle'][i]['left']) > min_for_change_point:
                result["description"] += (
                    f"{int(td['target_angle'][i]['left'])} degrees left; "
                )


    result["description"] += f' | Score: {result["score"]}'  
    return image, td, text, result



def calculate_target_point(rb, targets):
    """Calculate the target points based on the robot's current position and movement directions."""
    point = [rb.center[0], rb.center[1]]
    direction = rb.compute_angle_x(rb)
    res = []
    for target in targets:
        if isinstance(target, dict):
            point[0] += target['forward'] * math.cos(math.radians(direction))
            point[0] -= target['backward'] * math.cos(math.radians(direction))
            point[1] -= target['forward'] * math.sin(math.radians(direction))
            point[1] += target['backward'] * math.sin(math.radians(direction))
            res.append((point[0], point[1]))
        else:
            # Handle reversed y-axis
            direction += target[0]['left']
            direction -= target[0]['right']

    res.reverse()
    return res


def image_to_mask(filename, percentage):
    """Load an image and create a mask with a given scaling percentage."""
    temp = cv2.imread(filename)
    temp = cv2.resize(temp, (int(temp.shape[1] * percentage), int(temp.shape[0] * percentage)))

    lower_limit = np.array([0, 0, 0])  
    upper_limit = np.array([255, 254, 255])  
    mask = cv2.inRange(temp, lower_limit, upper_limit)

    return temp, mask


def fruit_ninja(robot, image, td: dict):
    """Test for lesson 5: Long distance race."""


    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"

    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 24,
            "data": {},
            "delta": 4,
            "reached_point": False
        }


    if not td["data"] and robot:
        route = [
            {'forward': 30, 'backward': 0},
            [{'left': 90, 'right': 0}],
            {'forward': 20, 'backward': 0},
            [{'left': 0, 'right': 90}],
            {'forward': 30, 'backward': 0},
            [{'left': 0, 'right': 90}],
            {'forward': 20, 'backward': 0}
        ]

        td["data"]['targets'] = calculate_target_point(robot, route)
        td["data"]['delta'] = 4
        td["data"]['reached_point'] = False

        td["data"]["fruit"] = {}
        td["data"]["mask"] = {}
        td["data"]["animation"] = {}

        basepath = os.path.abspath(os.path.dirname(__file__))

        for i in range(4):
            td["data"]["fruit"][i] = {}
            td["data"]["mask"][i] = {}
            
            for j in range(1, 7):
                filepath = os.path.join(basepath, 'images', f'{i}-{j}.jpg')
                td["data"]["fruit"][i][j], td["data"]["mask"][i][j] = image_to_mask(filepath, percentage=0.7)
            
            td["data"]["animation"][i] = 1

        td["data"]['coordinates'] = [(robot.cm_to_pixel(x), robot.cm_to_pixel(y)) for x, y in td["data"]['targets']]

    d = None

    if robot:
        d = delta_points(robot.center, td["data"]['targets'][-1])
        text = f'The distance to the next ({td["data"]["targets"][-1][0]:0.0f}, {td["data"]["targets"][-1][1]:0.0f}) ' \
               f'point is {d:0.0f}'

        if d < td["data"]['delta']:
            if len(td["data"]['targets']) > 1:
                td["data"]["animation"][len(td["data"]['targets']) - 1] += 1
                td["data"]['delta'] += 1.3
                td["data"]['targets'].pop()
            elif not td["data"]['reached_point']:
                td["data"]["animation"][0] += 1
                td["data"]['reached_point'] = True
                td["end_time"] = time.time() + 4


    if d is not None and td["end_time"] - time.time() < 2 and (
            len(td["data"]['targets']) != 1 or d > td["data"]['delta']):
        if len(td["data"]['targets']) > 1:
            text = "Robot missed several checkpoints"
        else:
            text = f'It is disappointing, but robot failed the task, because it is {d:0.0f} centimeters away from the target point'
        result["description"] = text
        result["success"] = False
        result["score"] = 0

    if td["data"]:
        for i in range(len(td["data"]['coordinates'])):
            if td["data"]["animation"][i] > 6:
                td["data"]['coordinates'].pop()
                td["data"]['fruit'].pop(i)
                td["data"]["mask"].pop(i)
                td["data"]["animation"].pop(i)
            else:
                x, y = td["data"]['coordinates'][i]
                fruit = td["data"]["fruit"][i][td["data"]["animation"][i]]
                mask = td["data"]["mask"][i][td["data"]["animation"][i]]

                ymin = fruit.shape[0] // 2
                ymax = fruit.shape[0] - ymin
                xmin = fruit.shape[1] // 2
                xmax = fruit.shape[1] - xmin

                cv2.copyTo(fruit, mask, image[y - ymin:y + ymax, x - xmin:x + xmax])

                if td["data"]["animation"][i] > 1:
                    td["data"]["animation"][i] += 1

    return image, td, text, result