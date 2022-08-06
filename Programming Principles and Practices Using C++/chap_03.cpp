#include "std_lib_facilities.h"

int main()
{
    // Part 01
    cout << "\nEnter the name of the person you want to write to: ";
    string first_name;
    cin >> first_name;
    cout << "\nDear " << first_name << ",";
    // Part 02
    cout << "\n\tI hope this letter finds you well."
         << " It has been a long time since last we met."
         << " If you are free this coming weekend, we should met up."
         << " Let me know when and where, and I will be sure to be there.\n";
    // Part 03
    cout << "\nPlease enter the name of another friend: ";
    string friend_name;
    cin >> friend_name;
    cout << "\nHave you seen " << friend_name << " lately?";
    // Part 04
    char friend_sex = '0';
    while (friend_sex != 'm' && friend_sex != 'f') {
        cout << "\n\nEnter 'm' if the friend is male, 'f' if female: ";
        cin >> friend_sex;
    }
    if (friend_sex == 'm') {
        cout << "\nIf you see " << friend_name << " Please ask him to call me.";
    }
    if (friend_sex == 'f') {
        cout << "\nIf you see " << friend_name << " Please ask her to call me.";
    }
    // Part 05
    cout << "\n\nPlease enter the age of the recipient: ";
    int age;
    cin >> age;
    cout << "\nI hear you just has a birthday and your are " << age << " years old.";
    if (age <= 0 || age >= 110) {
        simple_error("you're kidding!");
    }
    // Part 06
    if (age < 12) {
        cout << "\nNext year you will be " << age + 1 << '.';
    }
    if (age == 17) {
        cout << "\nNext year you will be able to vote.";
    }
    if (age > 70) {
        cout << "\nI hope you are enjoying retirement.";
    }
    // Part 07
    cout << "\n\nYours sincerely\n\n";
}