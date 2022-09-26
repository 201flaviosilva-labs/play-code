import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    // Intro
    System.out.println("Lets play a game:");
    System.out.println(" ---- Guess The Number ----");
    System.out.println("");
    
    System.out.println("A number was hidden between 1 and 10");
    System.out.println("");

    // Generating number
    int rdn = (int) Math.round(Math.random() * 9) + 1; // 1 - 5
    
    // Player
    int attempts = 0;
    int playerGuess = 0;

    do {
      System.out.print("Number: ");
      playerGuess = scanner.nextInt(); 
      attempts++;

      if(rdn>playerGuess) System.out.println("Your number is too SMALL.");
      else if(rdn<playerGuess) System.out.println("Your number is too BIG.");
      else System.out.println("You got the number right. In " + attempts + "attempts.");
			
    } while (playerGuess != rdn);
  }
}
