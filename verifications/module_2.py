import cv2
import math
import time
import os
import numpy as np

target_points = {
    'headlights': [(30, 50), (30, 0)],
    'alarm': [(30, 50), (30, 0)],
}

block_library_functions = {
    'headlights': False,
    'alarm': False,
}


def get_block_library_functions(task):
    """Retrieve block library status for a given task."""
    return block_library_functions.get(task, False)


def get_target_points(task):
    """Retrieve target points for a given task."""
    return target_points.get(task, [])



def headlights(robot, image, td: dict):
    """Test for lesson 6: Headlights."""

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"

    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 15,
            "data": {
                "headlight_frames": 0,
                "count_frames": 0
            }
        }


        basepath = os.path.abspath(os.path.dirname(__file__))

        temp_on = cv2.imread(os.path.join(basepath, "images", "headlight-on.jpg"))
        temp_off = cv2.imread(os.path.join(basepath, "images", "headlight-off.jpg"))

        temp_on = cv2.resize(temp_on, (temp_on.shape[1] // 3, temp_on.shape[0] // 3))
        temp_off = cv2.resize(temp_off, (temp_off.shape[1] // 3, temp_off.shape[0] // 3))

        td["data"]["turn-on"] = temp_on
        td["data"]["turn-off"] = temp_off

        td["data"]["turn-on-mask"] = cv2.inRange(temp_on, np.array([0, 240, 0]), np.array([15, 255, 15]))
        td["data"]["turn-off-mask"] = cv2.inRange(temp_off, np.array([0, 0, 0]), np.array([15, 15, 15]))

    percentage_white = 0
    td["data"]["count_frames"] += 1

    if robot:
        lower_white = np.array([230, 230, 230])
        upper_white = np.array([255, 255, 255])

        # Crop region of interest (ROI) near the robot's headlights
        crop_x, crop_y = robot.center_px[0] + 80, robot.center_px[1] - 90
        crop_width, crop_height = 80, 180

        croped_image = image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]

        # Create mask for detecting white pixels
        mask = cv2.inRange(croped_image, lower_white, upper_white)

        # Calculate white pixel percentage
        total_pixels = croped_image.shape[0] * croped_image.shape[1]
        white_pixels = cv2.countNonZero(mask)
        percentage_white = (white_pixels / total_pixels) * 100

        # Draw contours around the white regions
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_image = croped_image.copy()
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

        # Overlay the contour image back to the main image
        image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width] = contour_image

    # ✅ Headlight detection logic
    if percentage_white > 2:
        td["data"]["headlight_frames"] += 1
        text = "Headlights ON"
        cv2.copyTo(td["data"]["turn-on"], td["data"]["turn-on-mask"],
                   image[30:30 + td["data"]["turn-on"].shape[0], 1080:1080 + td["data"]["turn-on"].shape[1]])
    else:
        text = "Headlights OFF"
        cv2.copyTo(td["data"]["turn-off"], td["data"]["turn-off-mask"],
                   image[30:30 + td["data"]["turn-off"].shape[0], 1080:1080 + td["data"]["turn-off"].shape[1]])

    # ✅ Check for task completion status
    if td["end_time"] - time.time() < 1:
        headlight_ratio = td["data"]["headlight_frames"] / td["data"]["count_frames"]

        if headlight_ratio < 0.6:
            result["success"] = False
            result["description"] = "It is disappointing, but the robot failed the task."
            result["score"] = 0

    return image, td, text, result

def alarm(robot, image, td: dict):
    """Test for lesson 6: Alarm system with headlight detection."""

    # ✅ Initialize the result structure
    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"

    # ✅ Initialize task parameters
    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 15,
            "data": {
                "headlight_frames": 0,
                "count_frames": 0,
                "changed": 0
            }
        }

        # Load headlight images
        basepath = os.path.abspath(os.path.dirname(__file__))

        temp_on = cv2.imread(os.path.join(basepath, "images", "headlight-on.jpg"))
        temp_off = cv2.imread(os.path.join(basepath, "images", "headlight-off.jpg"))

        temp_on = cv2.resize(temp_on, (temp_on.shape[1] // 3, temp_on.shape[0] // 3))
        temp_off = cv2.resize(temp_off, (temp_off.shape[1] // 3, temp_off.shape[0] // 3))

        # Create masks for overlaying the headlight images
        td["data"]["turn-on"] = temp_on
        td["data"]["turn-off"] = temp_off

        td["data"]["turn-on-mask"] = cv2.inRange(temp_on, np.array([0, 240, 0]), np.array([15, 255, 15]))
        td["data"]["turn-off-mask"] = cv2.inRange(temp_off, np.array([0, 0, 0]), np.array([15, 15, 15]))

    # ✅ Check for robot headlights
    percentage_white = 0
    td["data"]["count_frames"] += 1

    if robot:
        lower_white = np.array([230, 230, 230])
        upper_white = np.array([255, 255, 255])

        # Crop region of interest (ROI) near the robot's headlights
        crop_x, crop_y = robot.center_px[0] + 80, robot.center_px[1] - 90
        crop_width, crop_height = 80, 180

        croped_image = image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]

        # Create mask for detecting white pixels
        mask = cv2.inRange(croped_image, lower_white, upper_white)

        # Calculate white pixel percentage
        total_pixels = croped_image.shape[0] * croped_image.shape[1]
        white_pixels = cv2.countNonZero(mask)
        percentage_white = (white_pixels / total_pixels) * 100

        # Draw contours around the white regions
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_image = croped_image.copy()
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

        # Overlay the contour image back to the main image
        image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width] = contour_image

        # ✅ Track headlight state changes
        if "last_state" not in td["data"]:
            td["data"]["last_state"] = percentage_white > 2
        elif (percentage_white > 2) != td["data"]["last_state"]:
            td["data"]["last_state"] = not td["data"]["last_state"]
            td["data"]["changed"] += 1

    # ✅ Headlight display logic
    if percentage_white > 2:
        text = "Headlights ON"
        td["data"]["headlight_frames"] += 1
        cv2.copyTo(td["data"]["turn-on"], td["data"]["turn-on-mask"],
                   image[30:30 + td["data"]["turn-on"].shape[0], 1080:1080 + td["data"]["turn-on"].shape[1]])
    else:
        text = "Headlights OFF"
        cv2.copyTo(td["data"]["turn-off"], td["data"]["turn-off-mask"],
                   image[30:30 + td["data"]["turn-off"].shape[0], 1080:1080 + td["data"]["turn-off"].shape[1]])

    # ✅ Task completion validation
    if td["end_time"] - time.time() < 0.5:
        headlight_ratio = td["data"]["headlight_frames"] / td["data"]["count_frames"]

        if headlight_ratio > 0.65 or headlight_ratio < 0.35 or td["data"]["changed"] < 13:
            result["success"] = False
            result["description"] = "It is disappointing, but the robot failed the task."
            result["score"] = 0

        print(f"State changes: {td['data']['changed']}")

    return image, td, text, result
