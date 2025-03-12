# Description

This folder will be fully downloaded to the device responsible for automated verification.

## Structure

The name of each verification function must match the `str_id` field specified in the `lessons_list.json` file. Additionally, each verification function must be located in a Python file whose name matches the `str_id` of the module specified in the `lessons_list.json` file.

Example:
In the `lessons_list.json` file, the first module titled "Introduction to the Robot" has a `str_id` field with the value `module_0`. Therefore, this directory contains a file named `module_0.py`. Additionally, in the `lessons_list.json` file, within the module titled "Introduction to the Robot," there is a `lessons` list containing several lessons with `str_id` fields such as: `draw`, `test_drive`, and `license_to_drive`. The `module_0.py` file contains functions with corresponding names. These functions will be used by the device responsible for automated verification.

## Description of the Verification Function

The verification function is called for each frame received from the camera.

Arguments passed to the verification function:
- `robot` - a reference to the `robot` object, which has its own methods that can be used within the verification functions. For more details about the robot object's methods, refer to [here](#robot-object).
- `image` - the image from the camera, an object of type `numpy.ndarray`. The image is in RGB format.
- `td` - a dictionary containing various parameters required for the verification function, an object of type `dict`. On the first call of the function, it is set to `None`.

The function returns:
- `image` - the modified image within the verification function, which will be displayed to the user, an object of type `numpy.ndarray`. The image is in RGB format.
- `td` - a dictionary containing various parameters required for the verification function, an object of type `dict`. This dictionary can store data that will be used in subsequent iterations of the verification function. **It is mandatory** to include a field named **`end_time`** in this dictionary, which specifies when the verification will end.
- `text` - the message text to be displayed to the user, a field of type `string`.
- `result` - a dictionary containing the results of the verification iteration. This dictionary must include the following **mandatory** fields:
    - **`success`** - a field of type `boolean`. If this field is `False`, the task is considered failed, and the verification ends immediately.
    - **`description`** - a description of the result, which will be displayed to the user after the verification ends. A field of type `string`.
    - **`score`** - the task score, ranging from 0 to 100, where 0 means the task is failed, and 100 means the task is completed perfectly.

## Additional Mandatory Data in Module Files

In each module file, besides the verification functions and their helper functions, the following must **mandatorily** be included:

1) A dictionary containing the starting positions for each task. Each starting position is described by two tuples: the first is the position in centimeters on the field; the second is the robot's direction. The guiding point is calculated as follows: the robot's x-coordinate + the first value from the direction tuple, and the robot's y-coordinate + the second value from the direction tuple. The keys of the dictionary are the `str_id` fields of the tasks from the `lessons_list.json` file.

    Example of guiding point calculation:
    Suppose for the task `test_drive`, we have a list of two points: `[(35, 50), (30, 0)]`. Here, `(35, 50)` is the starting point the robot will move to. `(30, 0)` is the robot's direction. When the robot reaches the starting point, its coordinates will roughly match `(35, 50)`. The guiding point will then be calculated as: `(35+30, 50+0)`, meaning the robot will be directed toward the point `(35+30, 50+0)`, i.e., in the positive direction of the x-axis.

    Example of a dictionary with starting points:
    ```python
    # start points for the tasks
    target_points = {
        'test_drive': [(35, 50), (30, 0)],
        'license_to_drive': [(35, 50), (30, 0)],
        'draw': [(50, 50), (30, 0)]
    }
    ```

2) A dictionary containing information about blocking library functions. This is necessary to prevent cheating. For example, a course task might require the user to write a function for robot movement, but the user might attempt to use a standard library function for movement. To address this, a blocking mechanism is introduced. If the value in this dictionary is `True`, the standard library functions will be blocked. The keys of the dictionary are the `str_id` fields of the tasks from the `lessons_list.json` file.

    Example of such a dictionary:
    ```python
    block_library_functions = {
        'test_drive': False,
        'license_to_drive': False,
        'draw': False,
    }
    ```

3) A function that returns a value from dictionary 1. The function below can simply be copied into the module file.

    ```python
    # function to get value from dictionary target_point
    def get_target_points(task):
        global target_points
        return target_points[task]
    ```

4) A function that returns a value from dictionary 2. The function below can simply be copied into the module file.

    ```python
    # function to get value from dictionary block_library_functions
    def get_block_library_functions(task):
        global block_library_functions
        return block_library_functions[task]
    ```

## Robot Object

In progress...