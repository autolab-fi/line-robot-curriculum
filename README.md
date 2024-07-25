# Course of remote learning on Line-Following Robot


## Description of Repository Structure

- **images** folder: Contains images for the course. Images can be organized in any structure within this folder. We suggest saving images in different folders for different modules.
- **lessons** folder: Contains lessons in Markdown (.md) format. Lessons can be organized in any structure within this folder. We suggest saving lessons in different folders for different modules.
- **maps** folder: contains maps
- **course-info.json** file: Contains basic information about the course, such as the full course name, short name, description, workload, student requirements, and image links.
- **lessons-list.json** file: Contains a list modules with lessons:

### Structure of lessons-list.json
**lessons-list.json** contains list with modules.
Every module in the list has structure:

- *str_id*: unique string identifier for each module in the course.
- *name*: display name of the module on the course page.
- *description*: description of the module.
- *sn*: Serial number of the module in the course, **starting from 0**.
- *lessons*: list of the lessons in the module.

Every lessons has structure:
- *str_id*: Unique string identifier for each lesson in the course.
- *name*: Display name of the lesson on the course page.
- *url*: URL for the lesson's Markdown file.
- *sn*: Serial number of the lesson in the course, starting from 0.
- *description*: description of the lesson.
- *template*: code template that would be displayed for user in the code editor

### Structure of course-info.json
Course info:

- *fullCourseName*: Full name of the course.
- *shortCourseName*: Short name of the course.
- *shortDescription*: A short description of the course, up to 160 characters.
- *fullDescription*: A full description of the course, around 500 characters.
- *imageSmall*: URL for the small image (approximately 640x360 px).
- *imageBig*: URL for the large image (approximately 1920x1080 px).
- *workload*: Estimated time required to complete the course.
- *programmingLanguage*: string identifyer of programming language used in course.

## Library for the course
Library for the course is [here](https://github.com/autolab-fi/LineRobotLibrary)