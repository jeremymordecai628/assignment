import java.util.Scanner;
public class Authenticity{
	// Constant declaration
	private static final int MAX_ATTEMPTS = 3;

	// Variable declaration
	private static String correctPassword = "java123";

	// Method to check password validity
	public static boolean checkPassword(String input) {
		return input.equals(correctPassword);
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int attempts = 0;
		boolean accessGranted = false;
		System.out.println("=== SIMPLE JAVA LOGIN SYSTEM ===");

		
		// Loop (for repetition)
		while (attempts < MAX_ATTEMPTS) {
			System.out.print("Enter your password: ");
			String userInput = scan.nextLine();
			try {
				// Selection statement (decision making)
				if (checkPassword(userInput)) {
					System.out.println("Access Granted ✅");
					accessGranted = true;
					break;
				} else {
					attempts++;
					System.out.println("Incorrect password. Attempts left: " + (MAX_ATTEMPTS - attempts));
				}
			} catch (Exception e) {
				// Error handling
				System.out.println("An unexpected error occurred: " + e.getMessage());
			}
		}
		if (!accessGranted) {
			System.out.println("Access Denied ❌ Too many failed attempts.");
		}
		scan.close();
	}
}
