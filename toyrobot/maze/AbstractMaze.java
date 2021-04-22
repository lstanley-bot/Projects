package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;

import java.util.ArrayList;
import java.util.List;

public class AbstractMaze implements Maze{
    private final List<Obstacle> obstacles = new ArrayList<>();

    /**
     * @return the list of obstacles or empty list
     */
    public List<Obstacle> getObstacles() {
        return obstacles;
    }

    /**
     * Checks if this maze has at least one obstacle that blocks the path that goes from coordinate (x1, y1) to (x2, y2).
     * Since our robot can only move in horizontal or vertical lines (no diagonals yet), we can assume that either x1==x2 or y1==y2.
     *
     * @param a first position
     * @param b second position
     * @return `true` if there is an obstacle is in the way
     */
    public boolean blocksPath(Position a, Position b) {
        for (Obstacle obs : this.getObstacles()) {
            if (obs.blocksPath(a, b)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Adds obstacles to a list
     * @param obstacle
     */
    public void addToObstacleList(Obstacle obstacle) {
        this.obstacles.add(obstacle);
    }

    /**
     * Iterates through the list of obstacles and removes each element form the list.
     */
    public void purgeList() {
        this.obstacles.removeAll(getObstacles());
    }
}
