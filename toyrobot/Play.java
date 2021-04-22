package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.maze.*;
import za.co.wethinkcode.toyrobot.world.IWorld;
import za.co.wethinkcode.toyrobot.world.TextWorld;
import za.co.wethinkcode.toyrobot.world.TurtleWorld;

import java.util.Arrays;
import java.util.Scanner;

public class Play {
    static Scanner scanner;

    public static void main(String[] args) {
        Maze maze = null;
        Robot robot;
        IWorld world;
        Command command;

        if (args.length >= 1 && (args[0].toLowerCase().trim().equalsIgnoreCase("text") ||
                args[0].toLowerCase().trim().equalsIgnoreCase("turtle"))) {
            if (args.length == 1) {
                maze = new RandomMaze();
            }
            else {
                switch (args[1].toLowerCase().trim()){
                    case "designedmaze":
                        maze = new DesignedMaze();
                        break;
                    case "emptymaze":
                        maze = new EmptyMaze();
                        break;
                    case "simplemaze":
                        maze = new SimpleMaze();
                        break;
                    default:
                        maze = new RandomMaze();
                }
            }
            world = ((args[0].equalsIgnoreCase("turtle")) ?
                    new TurtleWorld(maze) : new TextWorld(maze));
        } else {
            world = new TextWorld(new RandomMaze());
        }

        scanner = new Scanner(System.in);

        String name = getInput("What do you want to name your robot?");
        robot = new Robot(name);
        robot.setWorld(world);
        System.out.println("Hello Kiddo!");
        System.out.println("Loaded " + maze.getClass().getSimpleName());

        if (maze.getObstacles().size() != 0) {
            System.out.println("There are some obstacles:");
            world.showObstacles();
        }

        System.out.println(robot.toString());

        boolean shouldContinue = true;
        do {
            String instruction = getInput(robot.getName() + "> What must I do next?").strip().toLowerCase();
            try {
                command = Command.create(instruction);
                shouldContinue = robot.handleCommand(command);
            } catch (IllegalArgumentException e) {
                robot.setStatus("Sorry, I did not understand '" + instruction + "'.");
            }
            System.out.println(robot);
        } while (shouldContinue);

        if (Arrays.stream(args).anyMatch("turtle"::equalsIgnoreCase)) {
            System.exit(0);
        }
    }

    private static String getInput(String prompt) {
        System.out.println(prompt);
        String input = scanner.nextLine();

        while (input.isBlank()) {
            System.out.println(prompt);
            input = scanner.nextLine();
        }
        return input;
    }

    public static void printOutput(Robot output){
        System.out.println(output);
    }
}
