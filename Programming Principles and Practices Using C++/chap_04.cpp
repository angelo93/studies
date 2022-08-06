#include "std_lib_facilities.h"

bool ValidateUnit(string unit)
{
    bool is_legal = false;
    const vector<string> legal_units {"cm", "m", "in", "ft"};

    for (string legal_unit : legal_units)
    {
        if (unit == legal_unit)
        {
            is_legal = true;
            break;
        }
    }

    if (!is_legal)
    {
        cout << "\nIllegal unit entered: '" << unit << "'";
    }

    return is_legal;
}

double ConvertToMeters(double val, string unit)
{
    constexpr double cm_to_m {0.01};
    constexpr double in_to_m {2.54 * cm_to_m};
    constexpr double ft_to_m {12.0 * in_to_m};

    double ret_val = 0.0;

    if (unit == "cm")
        ret_val = val * cm_to_m;
    else if (unit == "in")
        ret_val = val * in_to_m;
    else if (unit == "ft")
        ret_val = val * ft_to_m;
    else
        ret_val = val;

    return ret_val;
}

void PrintOutput(double curr_val, double val_in_meters, double largest, double smallest, string unit)
{
    if (val_in_meters == largest)
    {
        cout << "\nThe number is: " << curr_val << unit
                << " (" << val_in_meters << "m)"
                << "\nThe largest so far.";
    }
    else if (val_in_meters == smallest)
    {
        cout << "\nThe number is: " << curr_val << unit
                << " (" << val_in_meters << "m)"
                << "\nThe smallest so far.";
    }
    else
    {
        cout << "\nThe number is: " << curr_val << unit
                << " (" << val_in_meters << "m)";
    }

    return;
}

int main()
{
    cout << "\nEnter a number followed by unit of measurement (cm, m, in, ft): ";

    int num_vals    = 0;
    double curr_val = 0.0;
    double largest  = 0.0;
    double smallest = 0.0;
    double sum_vals = 0.0;
    string unit     = "";
    bool first_loop = true;

    vector<double> val_list {};

    while (cin >> curr_val >> unit)
    {
        double val_in_meters = 0.0;
        bool is_legal_unit = ValidateUnit(unit);

        if (is_legal_unit)
        {
            val_in_meters = ConvertToMeters(curr_val, unit);

            if (first_loop)
            {
                largest  = val_in_meters;
                smallest = val_in_meters;

                cout << "\nThe first number is: " << curr_val << unit
                     << " (" << val_in_meters << "m)"
                     << "\nThe smallest so far: " << smallest << "m"
                     << "\nThe largest so far: " << largest << "m";

                first_loop = false;
            }
            else
            {
                largest  = max(val_in_meters, largest);
                smallest = min(val_in_meters, smallest);

                PrintOutput(curr_val, val_in_meters, largest, smallest, unit);
            }

            num_vals += 1;
            sum_vals += val_in_meters;
            val_list.push_back(val_in_meters);
        }

        cout << "\n\nEnter a number followed by unit of measurement (cm, m, in, ft): ";
    }

    cout << "\n\nSmallest: "  << smallest << "m"
         << "\nLargest: "     << largest  << "m"
         << "\nNum of vals: " << num_vals
         << "\nSum of vals: " << sum_vals << "m";

    cout << '\n';
    sort(val_list);
    for (double val : val_list)
    {
        cout << val << "m ";
    }
    cout << '\n';

    return 0;
}