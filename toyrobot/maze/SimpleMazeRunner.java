package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Command;
import za.co.wethinkcode.toyrobot.Play;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.Robot;
import za.co.wethinkcode.toyrobot.world.IWorld;

import java.util.Random;

public class SimpleMazeRunner implements MazeRunner{
    private final Robot robot;
    private final Maze maze;
    private final IWorld world;
    private int runCost;

    public SimpleMazeRunner(Robot target) {
        this.robot = target;
        this.world = this.robot.getWorld();
        this.maze = this.world.getMaze();
    }

    /**
     * Asks Mazerunner to start its mazerun.
     *
     * @param target        the instance of Robot to use to run the maze
     * @param edgeDirection the edge to try and reach, one of Direction.UP, RIGHT, DOWN, or LEFT
     * @return true if it was successful
     */
    public boolean mazeRun(Robot target, IWorld.Direction edgeDirection) {
        this.runCost = 0;
        moveTurtle(edgeDirection);
        return this.runCost < 20_000;
    }

    /**
     * Returns the cost for the previous mazerun attempt:
     * <p>
     * - Each command that involves moving 1 or more steps must count the number of steps taken in that command towards the total steps.
     * - Each time your robot turns, it also counts as 1 step.
     * - Commands that fails because it is blocked by an obstacle or an edge must also count the steps involved in the command towards the total number of steps.
     *
     * @return the total cost in steps of most recent mazerun
     */
    public int getMazeRunCost() {
        return runCost;
    }

    /**
     * Checks to see if taking one step forward would place the robot out of the allowed grid.
     *
     * @param directionModifier ; state in which direction to check
     *                          -1 - to the left
     *                          0  - straight
     *                          1  - to the right
     * @return true or false
     */
    public boolean nextOutOfBounds(int directionModifier) {
        int directionToCheck = world.getCurrentDirection().ordinal() + directionModifier;

        if (directionToCheck == 4) {
            directionToCheck = 0;
        } else if (directionToCheck == -1) {
            directionToCheck = 3;
        }

        if (directionToCheck == 0 && world.getPosition().getY() == 200) {
            return true;
        } else if (directionToCheck == 1 && world.getPosition().getX() == 100) {
            return true;
        } else if (directionToCheck == 2 && world.getPosition().getY() == -200) {
            return true;
        } else return directionToCheck == 3 && world.getPosition().getX() == -100;
    }

    /**
     * Checks to see if taking one step forward would place the robot within an obstacle.
     *
     * @param directionModifier ; state in which direction to check
     *                          -1 - to the left
     *                          0  - straight
     *                          1  - to the right
     * @return true or false
     */
    public boolean nextBlocked(int directionModifier) {
        int directionToCheck = world.getCurrentDirection().ordinal() + directionModifier;

        if (directionToCheck == 4) {
            directionToCheck = 0;
        } else if (directionToCheck == -1) {
            directionToCheck = 3;
        }

        if (directionToCheck == 0) {
            return maze.blocksPath(world.getPosition(), new Position(world.getPosition().getX(),
                    world.getPosition().getY() + 1));
        } else if (directionToCheck == 1) {
            return maze.blocksPath(world.getPosition(), new Position(world.getPosition().getX() + 1,
                    world.getPosition().getY()));
        } else if (directionToCheck == 2) {
            return maze.blocksPath(world.getPosition(), new Position(world.getPosition().getX(),
                    world.getPosition().getY() - 1));
        } else {
            return maze.blocksPath(world.getPosition(), new Position(world.getPosition().getX() - 1,
                    world.getPosition().getY()));
        }
    }

    /**
     * Checks if the robot is at one of the edges of the world
     *
     * @param direction ; which edge to check for
     *
     * @return true if the robot's current is on one of the 4 edges of the world
     */
    public boolean isAtEdge(IWorld.Direction direction) {
        switch (direction) {
            case UP:
                return world.getPosition().getY() == 200;
            case DOWN:
                return world.getPosition().getY() == -200;
            case LEFT:
                return world.getPosition().getX() == -100;
            default:
                return world.getPosition().getX() == 100;
        }
    }

    /**
     * Run logic for the maze runner.
     * Robot will move forward until it cannot.
     * Robot will then hug the wall until at the designated edge.
     * Every movement adds to the runCost
     *
     */
    public void moveTurtle(IWorld.Direction edge) {

        while (!nextBlocked(0) && !nextOutOfBounds(0)) {
            robot.handleCommand(Command.create("forward 1"));
            Play.printOutput(robot);
            runCost++;
        }

        while (!isAtEdge(edge) && this.runCost < 20_000) {

            if (nextBlocked(0) || nextOutOfBounds(0)) {
                Random random = new Random();
                int choose = random.nextInt(2);
                if (choose==1){
                    robot.handleCommand(Command.create("left"));
                    Play.printOutput(robot);
                    this.runCost++;
                } else if (choose==0) {
                    robot.handleCommand(Command.create("right"));
                    Play.printOutput(robot);
                    this.runCost++;
                } else {
                    robot.handleCommand(Command.create("back 1"));
                    Play.printOutput(robot);
                    robot.handleCommand(Command.create("left"));
                    Play.printOutput(robot);
                    robot.handleCommand(Command.create("left"));
                    Play.printOutput(robot);
                    this.runCost +=3;
                }

            } else if (nextBlocked(1) || nextOutOfBounds(1)) {
                robot.handleCommand(Command.create("forward 1"));
                Play.printOutput(robot);
                this.runCost++;
            } else {
                robot.handleCommand(Command.create("forward 1"));
                Play.printOutput(robot);
                this.runCost += 1;
            }
        }
    }
}
