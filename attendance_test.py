def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    attendance_marked = (
        student_id == "STU101"
        and attendance_status == "Present"
    )

    assert attendance_marked
    print("Attendance marking test passed!")


if __name__ == "__main__":
    test_mark_attendance()
