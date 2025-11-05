/*
 * Temperature Converter Program
 * Demonstrates: variables, constants, methods, loops, selection statements, and error handling
 */

import java.util.Scanner;

public class TemperatureConverter {

    // Constant
    private static final String AUTHOR = "Ressen Labs";

    // Method to convert Celsius to Fahrenheit
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    // Method to convert Fahrenheit to Celsius
    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int choice = 0;

        System.out.println("=== TEMPERATURE CONVERTER ===");
        System.out.println("Author: " + AUTHOR);

        // Loop: keep running until user chooses Exit
        while (true) {
            System.out.println("\n1. Convert Celsius to Fahrenheit");
            System.out.println("2. Convert Fahrenheit to Celsius");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            try {
                choice = scan.nextInt();

                // Selection statement
                if (choice == 1) {
                    System.out.print("Enter temperature in Celsius: ");
                    double celsius = scan.nextDouble();
                    System.out.println("Temperature in Fahrenheit: " + celsiusToFahrenheit(celsius));

                } else if (choice == 2) {
                    System.out.print("Enter temperature in Fahrenheit: ");
                    double fahrenheit = scan.nextDouble();
                    System.out.println("Temperature in Celsius: " + fahrenheitToCelsius(fahrenheit));

                } else if (choice == 3) {
                    System.out.println("Goodbye 👋");
                    break;

                } else {
                    System.out.println("Invalid choice. Please try again.");
                }

            } catch (Exception e) {
                // Error handling
                System.out.println("Error: Invalid input. Please enter numbers only.");
                scan.nextLine(); // clear bad input
            }
        }

        scan.close();
    }
}

