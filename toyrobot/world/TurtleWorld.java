package za.co.wethinkcode.toyrobot.world;

import org.turtle.StdDraw;
import org.turtle.Turtle;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.awt.*;

public class TurtleWorld extends AbstractWorld{
    private Turtle t;

    /**
     * Constructor for TurtleWorld
     *
     * @param maze
     */
    public TurtleWorld(Maze maze) {
        super(maze);
        setupTurtle();
        drawBorder();
        startingPoint();
    }

    private void setupTurtle() {
        double x = 1.0;
        double y = 5.0;
        double s = 10.0;
        t = new Turtle(x,y,s);
        StdDraw.setXscale(-250,250);
        StdDraw.setYscale(-250,250);
    }

    private void drawBorder(){
        t.setColor(Color.BLACK);
        t.setPosition(-101.0,-201.0);
        t.setAngle(0.0);
        t.forward(202);
        t.left(90.0);
        t.forward(402);
        t.left(90.0);
        t.forward(202);
        t.left(90.0);
        t.forward(402);
    }

    private void startingPoint(){
        t.setAngle(90.0);
        t.setPosition(0.0,0.0);
        t.setColor(Color.BLACK);
    }

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
            t.forward(nrSteps);
            return UpdateResponse.SUCCESS;
        }
        return UpdateResponse.FAILED_OUTSIDE_WORLD;
    }

    public void updateDirection(boolean turnRight) {
        Direction currentDirection = this.getCurrentDirection();
        int newDirectionIndex;

        if (turnRight) {
            newDirectionIndex = currentDirection.ordinal() + 1;
            if (newDirectionIndex == 4) {
                newDirectionIndex = 0;
            }
            t.right(90);
        } else {
            newDirectionIndex = currentDirection.ordinal() - 1;
            if (newDirectionIndex == -1) {
                newDirectionIndex = 3;
            }
            t.left(90);
        }
        this.setCurrentDirection(Direction.values()[newDirectionIndex]);
    }

    public void showObstacles() {
        for (Obstacle s : getObstacles()) {
            System.out.println("- At position " + s.getBottomLeftX() + ", " + s.getBottomLeftY() + " (to " + (s.getBottomLeftX() + 4) + ", " + (s.getBottomLeftY() + 4) + ")");
        }
        for (Obstacle s : getObstacles()) {
            t.setColor(Color.RED);
            t.setPosition(s.getBottomLeftX(), s.getBottomLeftY());
            t.forward(4);
            t.right(90);
            t.forward(4);
            t.right(90);
            t.forward(4);
            t.right(90);
            t.forward(4);
            t.right(90);
            t.forward(4);
            t.show();
        }
        startingPoint();
    }

    public void reset() {
        this.setCurrentDirection(Direction.UP);
        this.setPosition(CENTRE);
        getMaze().purgeList();
        StdDraw.clear();
        drawBorder();
        startingPoint();
    }
}
