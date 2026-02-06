from user_opeerations import add_user, view_users
from mess_operations import add_menu, view_menu
from email_operations import add_email_summary, view_email_summaries
from marketplace_operations import add_item, view_items
from lost_found_operations import report_item
from cab_operations import add_trip
from places_oprations import add_place, view_places
from places_review_operations import add_review, view_reviews
from academic_operations import add_course, view_courses
from timetable_operations import add_timetable_entry, view_timetable
from assignment_operations import add_assignment, view_assignments
from submission_operations import submit_assignment, view_submissions
from notification_operations import send_notification
from message_operations import send_message


def main_menu():
    while True:
        print("\n=== Campus Hub Main Menu ===")
        print("1. Users")
        print("2. Mess Menu")
        print("3. Email Summaries")
        print("4. Marketplace")
        print("5. Lost & Found")
        print("6. Cab Pool")
        print("7. Places")
        print("8. Place Reviews")
        print("9. Courses")
        print("10. Timetable")
        print("11. Assignments")
        print("12. Submissions")
        print("13. Notifications")
        print("14. Messages")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_menu()
        elif choice == "3":
            add_email_summary()
        elif choice == "4":
            add_item()
        elif choice == "5":
            report_item()
        elif choice == "6":
            add_trip()
        elif choice == "7":
            add_place()
        elif choice == "8":
            add_review()
        elif choice == "9":
            add_course()
        elif choice == "10":
            add_timetable_entry()
        elif choice == "11":
            add_assignment()
        elif choice == "12":
            submit_assignment()
        elif choice == "13":
            send_notification()
        elif choice == "14":
            send_message()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main_menu()
