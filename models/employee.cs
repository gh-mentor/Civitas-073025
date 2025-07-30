using System;

namespace Models
{
    /// <summary>
    /// Represents an employee with identification, department, name, and hourly rate.
    /// </summary>
    public class Employee
    {
        private readonly int _employeeID;
        private readonly int _departmentID;
        private string _firstName;
        private string _lastName;
        private double _hourlyRate;

        /// <summary>
        /// Gets the unique identifier for the employee.
        /// </summary>
        public int EmployeeID => _employeeID;

        /// <summary>
        /// Gets the department identifier for the employee.
        /// </summary>
        public int DepartmentID => _departmentID;

        /// <summary>
        /// Gets or sets the first name of the employee.
        /// </summary>
        /// <exception cref="ArgumentException">Thrown if the value is null or empty.</exception>
        public string FirstName
        {
            get => _firstName;
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("First name cannot be null or empty.", nameof(value));
                _firstName = value;
            }
        }

        /// <summary>
        /// Gets or sets the last name of the employee.
        /// </summary>
        /// <exception cref="ArgumentException">Thrown if the value is null or empty.</exception>
        public string LastName
        {
            get => _lastName;
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Last name cannot be null or empty.", nameof(value));
                _lastName = value;
            }
        }

        /// <summary>
        /// Gets or sets the hourly rate for the employee.
        /// </summary>
        /// <exception cref="ArgumentOutOfRangeException">Thrown if the value is negative.</exception>
        public double HourlyRate
        {
            get => _hourlyRate;
            set
            {

                // TODO
                if (value < 0)
                    throw new ArgumentOutOfRangeException(nameof(value), "Hourly rate cannot be negative.");
                _hourlyRate = value;
            }
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="Employee"/> class.
        /// </summary>
        /// <param name="employeeID">The unique identifier for the employee. Must be positive.</param>
        /// <param name="departmentID">The department identifier (1-3).</param>
        /// <param name="firstName">The first name of the employee.</param>
        /// <param name="lastName">The last name of the employee.</param>
        /// <param name="hourlyRate">The hourly rate for the employee. Must be non-negative.</param>
        /// <exception cref="ArgumentOutOfRangeException">
        /// Thrown if <paramref name="employeeID"/> is not positive,
        /// <paramref name="departmentID"/> is not between 1 and 3,
        /// or <paramref name="hourlyRate"/> is negative.
        /// </exception>
        /// <exception cref="ArgumentException">
        /// Thrown if <paramref name="firstName"/> or <paramref name="lastName"/> is null or empty.
        /// </exception>
        public Employee(int employeeID, int departmentID, string firstName, string lastName, double hourlyRate)
        {
            if (employeeID <= 0)
                throw new ArgumentOutOfRangeException(nameof(employeeID), "EmployeeID must be positive.");
            if (departmentID < 1 || departmentID > 3)
                throw new ArgumentOutOfRangeException(nameof(departmentID), "DepartmentID must be between 1 and 3.");
            if (string.IsNullOrWhiteSpace(firstName))
                throw new ArgumentException("First name cannot be null or empty.", nameof(firstName));
            if (string.IsNullOrWhiteSpace(lastName))
                throw new ArgumentException("Last name cannot be null or empty.", nameof(lastName));
            if (hourlyRate < 0)
                throw new ArgumentOutOfRangeException(nameof(hourlyRate), "Hourly rate cannot be negative.");

            _employeeID = employeeID;
            _departmentID = departmentID;
            _firstName = firstName;
            _lastName = lastName;
            _hourlyRate = hourlyRate;
        }
    }
}