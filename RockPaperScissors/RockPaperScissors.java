import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Intro
    System.out.println("Lets play a game:");
    System.out.println(" ---- Rock Paper Scissors ----");
    System.out.println("");

    System.out.println("Paper -> Rock");
    System.out.println("Scissors -> Paper");
    System.out.println("Rock -> Scissors");
    System.out.println("");

    // Player selection
    System.out.print("You: ");
    String player = scanner.nextLine();
    
    if (player.equals("Rock") || player.equals("Paper") || player.equals("Scissors")) {
      // Randomize CPU
      int rdn = (int) Math.round(Math.random() * 3);
      String cpu = "";

      if (rdn == 0)
        cpu = "Rock";
      else if (rdn == 1)
        cpu = "Paper";
      else
        cpu = "Scissors";

      System.out.println("CPU: " + cpu);

      // Check Winner
      System.out.println("");
      if (player.equals(cpu)) {
        System.out.println("Empate");
      } else if ((player.equals("Paper") && cpu.equals("Rock")) || (player.equals("Scissors") && cpu.equals("Paper"))
          || (player.equals("Rock") && cpu.equals("Scissors"))) {
        System.out.println("Player wins :)");
      } else {
        System.out.println("CPU wins :(");
      }

    } else {
      System.out.println("Option not available!");
    }

    scanner.close();
  }
}
