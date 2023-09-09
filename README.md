# IIITG PORTAL

**IIITG PORTAL** is a web-based student management system built with Node.js, Express.js and MongoDB which is designed to cater to the needs of Directors, Teachers, Students, and Office Staff within an educational institution.

## Features

### Director
- View details of staff and students.
- Manage courses and staff.
- Address complaints.

### Teacher
- Add and manage student results.
- Take attendance.

### Student
- View attendance records.
- Check results.
- Raise complaints.

## Getting Started

To set up the **IIITG PORTAL** system, follow these steps:

1. **Clone or Download:** Begin by cloning this repository to your local machine or downloading the project's source code.

2. **Install Dependencies:** Open a command prompt within the project folder and run the command `npm install` to install the necessary dependencies. You can also use `npm update` if needed.

3. **Start the Server:** Run the following command to start the server:
```sh
$ cd student-management-system
$ npm install
$ nodemon
```

## Import User Data

To populate the **IIITG PORTAL** system with user data, you can use the following command to import user information into the local MongoDB server:

```sh
$ mongoimport --db student-mgmt-sys --collection users --file users.json
```

# Screenshots

### Login
![Login](screenshots/login.png)

## Director

### Dashboard
![Director Dashboard](screenshots/admin_dashboard.png)

### Manage Courses
![Manage Courses](screenshots/manage_course.png)

### Manage Staff
![Manage Staff](screenshots/manage_staff.png)

### Complaints
![Complaints](screenshots/complaints.png)

## Teacher

### Dashboard
![Teacher Dashboard](screenshots/faculty_dashboard.png)

### Take Attendance
![Take Attendance](screenshots/take_attendence.png)

### Add Result
![Add Result](screenshots/add_result.png)

## Student

### Dashboard
![Student Dashboard](screenshots/student_dashboard.png)

### View Result
![View Result](screenshots/view_result.png)

### View Attendance
![View Attendance](screenshots/attendence.png)


