import cv2
import time
import os
import numpy as np

target_points = {
    'line_follower': [(20, 50), (0,-350)],
    'line_detection': [(30, 50), (30, 0)],

}

block_library_functions = {
    'line_follower': False,
    'line_detection': False,
}


def get_block_library_functions(task):
    """Retrieve block library status for a given task."""
    return block_library_functions.get(task, False)


def get_target_points(task):
    """Retrieve target points for a given task."""
    return target_points.get(task, [])




def line_follower(robot, image, td: dict):
    """Test for line following with checkpoint verification."""


    result = {
        "success": True,
        "description": "Verifying",
        "score": 50
    }
    text = "Verifying"


    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 10,
            "data": {
                "reached_checkpoints": [False, False],
                "task_completed": False
            }
        }


        basepath = os.path.abspath(os.path.dirname(__file__))
        cone = cv2.imread(os.path.join(basepath, "images", "checkpoint.png"))
        cone = cv2.resize(cone, (60, 60))


        mask = cv2.bitwise_not(cv2.inRange(cone, np.array([0, 240, 0]), np.array([35, 255, 35])))

        td["data"].update({
            "cone": cone,
            "cone-mask": mask
        })


    if td["data"]["task_completed"]:
        result.update({
            "success": True,
            "description": "The robot successfully passed through the checkpoints!",
            "score": 100
        })
        text = "Robot passed both checkpoints!"
        return image, td, text, result


    checkpoint_positions = [(270, 220), (210, 800)]
    for i, (y, x) in enumerate(checkpoint_positions):
        if not td["data"]["reached_checkpoints"][i]:
            roi = image[y - 30:y + 30, x - 30:x + 30]
            cv2.copyTo(td["data"]["cone"], td["data"]["cone-mask"], roi)


    if robot:
        robot_x, robot_y = robot.center_px

        for i, (y, x) in enumerate(checkpoint_positions):
            if not td["data"]["reached_checkpoints"][i]:
                distance = np.linalg.norm([robot_x - x, robot_y - y])
                if distance < 50:
                    td["data"]["reached_checkpoints"][i] = True
                    image[y - 30:y + 30, x - 30:x + 30] = (255, 255, 255) 


        if all(td["data"]["reached_checkpoints"]):
            td["data"]["task_completed"] = True
            result.update({
                "success": True,
                "description": "The robot successfully passed through the checkpoints!",
                "score": 100
            })
            text = "Robot passed both checkpoints!"
            return image, td, text, result

 
    if time.time() >= td["end_time"]:
        result.update({
            "success": False,
            "description": "The robot did not pass both checkpoints within time.",
            "score": 0
        })
        text = "Failed"
        return image, td, text, result

    return image, td, text, result
