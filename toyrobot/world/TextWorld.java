package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;


public class TextWorld extends AbstractWorld {

    /**
     * AbstractWorld constructor
     *
     * @param maze : the maze to be implemented
     */
    public TextWorld(Maze maze) {
        super(maze);
    }

    /**
     * Updates the position of your robot in the world by moving the nrSteps in the robots current direction.
     *
     * @param nrSteps steps to move in current direction
     * @return true if this does not take the robot over the world's limits, or into an obstacle.
     */
    public UpdateResponse updatePosition(int nrSteps) {
        int newX = getPosition().getX();
        int newY = getPosition().getY();
        int oldX = getPosition().getX();
        int oldY = getPosition().getY();

        switch (getCurrentDirection()) {
            case UP:
                newY = newY + nrSteps;
                break;
            case LEFT:
                newX = newX - nrSteps;
                break;
            case DOWN:
                newY = newY - nrSteps;
                break;
            case RIGHT:
                newX = newX + nrSteps;
                break;
        }

        Position newPosition = new Position(newX, newY);
        Position oldPosition = new Position(oldX, oldY);

        if (getMaze().blocksPath(newPosition, oldPosition)) {
            return UpdateResponse.FAILED_OBSTRUCTED;
        }

        if (isNewPositionAllowed(newPosition)) {

            setPosition(newPosition);
            return UpdateResponse.SUCCESS;
        }

        return UpdateResponse.FAILED_OUTSIDE_WORLD;
    }

    /**
     * Updates the current direction your robot is facing in the world by cycling through the directions UP, RIGHT, BOTTOM, LEFT.
     *
     * @param turnRight if true, then turn 90 degrees to the right, else turn left.
     */
    public void updateDirection(boolean turnRight) {
        Direction currentDirection = this.getCurrentDirection();
        int newDirectionIndex;

        if (turnRight) {

            newDirectionIndex = currentDirection.ordinal() + 1;
            if (newDirectionIndex == 4) {
                newDirectionIndex = 0;
            }
        } else {
            newDirectionIndex = currentDirection.ordinal() - 1;
            if (newDirectionIndex == -1) {
                newDirectionIndex = 3;
            }
        }
        this.setCurrentDirection(Direction.values()[newDirectionIndex]);
    }

    /**
     * Displays a list obstacles.
     */
    public void showObstacles() {
        for (Obstacle s : getObstacles()) {
            System.out.println("- At position " + s.getBottomLeftX() + ", " + s.getBottomLeftY() + " (to " + (s.getBottomLeftX() + 4) + ", " + (s.getBottomLeftY() + 4) + ")");
        }
    }

    /**
     * Reset the world by:
     * - moving current robot position to center 0,0 coordinate
     * - removing all obstacles
     * - setting current direction to UP
     */
    public void reset() {
        this.setCurrentDirection(Direction.UP);
        this.setPosition(CENTRE);
        getMaze().purgeList();
    }
}