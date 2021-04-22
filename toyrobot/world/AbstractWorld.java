package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.util.List;

public abstract class AbstractWorld implements IWorld {

    private Position position;
    private Direction currentDirection;
    private final Maze maze;

    /**
     * AbstractWorld constructor
     */
    public AbstractWorld(Maze maze) {
        this.maze = maze;
        this.position = CENTRE;
        this.currentDirection = Direction.UP;
    }

    /**
     * Checks if the robot is at one of the edges of the world
     *
     * @return true if the robot's current is on one of the 4 edges of the world
     */
    public boolean isAtEdge() {
        return (this.position.getX() == 100 || this.position.getX() == -100
                || this.position.getY() == 200 || this.position.getY() == -200);
    }

    /**
     * Gets the current direction the robot is facing in relation to a world edge.
     *
     * @return Direction.UP, RIGHT, DOWN, or LEFT
     */
    public Direction getCurrentDirection() {
        return this.currentDirection;
    }

    /**
     * Sets the current direction the robot is facing in relation to a world edge.
     */
    public void setCurrentDirection(Direction currentDirection) {
        this.currentDirection = currentDirection;
    }

    /**
     * Retrieves the current position of the robot
     */
    public Position getPosition() {
        return this.position;
    }

    /**
     * Checks if the new position will be allowed, i.e. falls within the constraints of the world.
     *
     * @param position the position to check
     * @return true if it is allowed, else false
     */
    public boolean isNewPositionAllowed(Position position) {
        return position.isIn(TOP_LEFT, BOTTOM_RIGHT);
    }

    /**
     * Sets the current position of the robot
     */
    public void setPosition(Position position) {
        this.position = position;
    }

    /**
     * @return the list of obstacles, or an empty list if no obstacles exist.
     */
    public List<Obstacle> getObstacles()    {
        return this.maze.getObstacles();
    }

    /**
     * @return maze that has been implemented
     */
    public Maze getMaze()   {
        return this.maze;
    }
}