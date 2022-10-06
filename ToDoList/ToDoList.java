import java.util.*;

// ------------------------ Utils ------------------------
class ArrayUtils {
  public static final String ANSI_RESET = "\u001B[0m";
  public static final String ANSI_RED_BACKGROUND = "\u001B[41m";

  public static String[] add(String[] originalArr, String text) {
    String newArr[] = new String[originalArr.length + 1];

    for (int i = 0; i < originalArr.length; i++) {
      newArr[i] = originalArr[i];
    }

    newArr[newArr.length - 1] = text;

    return newArr;
  }

  public static String[] remove(String[] originalArr, String item) {
    String newArr[] = new String[originalArr.length - 1];
    int index = findIndex(originalArr, item);

    for (int i = 0, k = 0; i < originalArr.length; i++) {
      if (i == index)
        continue;

      newArr[k++] = originalArr[i];
    }

    return newArr;
  }

  public static int findIndex(String[] originalArr, String item) {
    int index = 0;
    for (int i = 0; i < originalArr.length; i++) {
      String notCheckedTask = originalArr[i];

      if (checkMarkInText(notCheckedTask)) {
        notCheckedTask = notCheckedTask.replace(" ✔️", "");
      }

      if (notCheckedTask.equals(item))
        index = i;
    }

    return index;
  }

  public static void reverse(String[] originalArr) {
    int size = (int) (Math.floor(originalArr.length / 2));

    for (int i = 0; i < size; i++) {
      int index = originalArr.length - i - 1;
      String tempValue = originalArr[index];
      originalArr[index] = originalArr[i];
      originalArr[i] = tempValue;
    }
  }

  public static String[] reverseNewArray(String[] originalArr) {
    String reversedArray[] = new String[originalArr.length];

    for (int i = 0; i < originalArr.length; i++) {
      int index = originalArr.length - i - 1;
      reversedArray[i] = originalArr[index];
    }

    return reversedArray;
  }

  public static void sort(String[] originalArr) {
    Arrays.sort(originalArr);
  }

  public static void print(String[] originalArr) {
    for (String t : originalArr) {
      if (checkMarkInText(t)) {
        System.out.println(ANSI_RED_BACKGROUND + t + ANSI_RESET);
      } else {
        System.out.println(t);
      }
    }
  }

  public static boolean checkMarkInText(String text) {
    return text.contains("✔️");
  }
}

// ------------------------ To Do List ------------------------
public class ToDoList {
  static String tasks[] = { "T1", "T2 ✔️", "T3", "C", "Y", "A", "H", "F", "Z", "A", "B", "A" };

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("------ To Do List ------");

    int userMenuSelection = -1;
    while (userMenuSelection != 0) {
      System.out.println("");
      System.out.println("------------------------");
      System.out.println("[1] -> Print all tasks");
      System.out.println("[2] -> Add a new task");
      System.out.println("[3] -> Remove a task");
      System.out.println("[4] -> Mark task completed");
      System.out.println("[5] -> UnMarck completed task");
      System.out.println("[6] -> Sort A->Z");
      System.out.println("[0] -> Exit");
      System.out.println("------------------------");
      System.out.println("");

      System.out.print("Option: ");
      userMenuSelection = scanner.nextInt();

      handleUserMenuSelection(userMenuSelection);
    }

    scanner.close();
  }

  public static void handleUserMenuSelection(int userMenuSelection) {
    switch (userMenuSelection) {
      case 1:
        printTasks();
        break;

      case 2:
        addNewTask();
        break;

      case 3:
        removeTask();
        break;

      case 4:
        completeTask();
        break;

      case 5:
        unCompleteTask();
        break;

      case 6:
        sortTasks();
        break;

      case 0:
        System.out.println("Bye :(");
        break;

      default:
        System.out.println("Errorr......");
        break;
    }
  }

  public static void printTasks() {
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("All tasks listed here:");

    arrayUtils.print(tasks);
  }

  public static void addNewTask() {
    Scanner scanner = new Scanner(System.in);
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("Add a new task");

    System.out.print("Task name: ");
    String newTask = scanner.next();

    tasks = arrayUtils.add(tasks, newTask);
  }

  public static void removeTask() {
    Scanner scanner = new Scanner(System.in);
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("Remove a task");

    System.out.print("Task name: ");
    String task = scanner.next();

    tasks = arrayUtils.remove(tasks, task);
  }

  public static void completeTask() {
    Scanner scanner = new Scanner(System.in);
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("Mark task completed");

    System.out.print("Task name: ");
    String task = scanner.next();

    int index = arrayUtils.findIndex(tasks, task);

    if (index > -1) {
      if (!arrayUtils.checkMarkInText(tasks[index])) {
        tasks[index] = tasks[index] + " ✔️";
      } else {
        System.out.println("Error, task already marked!!");
      }
    }
  }

  public static void unCompleteTask() {
    Scanner scanner = new Scanner(System.in);
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("UnMarck completed task");

    System.out.print("Task name: ");
    String task = scanner.next();
    int index = arrayUtils.findIndex(tasks, task);

    if (index > -1) {
      if (!arrayUtils.checkMarkInText(tasks[index])) {
        System.out.println("Error, task not marked!!");
      } else {
        tasks[index] = tasks[index].replace(" ✔️", "");
      }
    }
  }

  public static void sortTasks() {
    ArrayUtils arrayUtils = new ArrayUtils();

    System.out.println("Tasks sorted alphabetically");

    arrayUtils.sort(tasks);

  }
}
