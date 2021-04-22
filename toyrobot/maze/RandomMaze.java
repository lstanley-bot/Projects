package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.AbstractWorld;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;

import java.util.Random;

public class RandomMaze extends AbstractMaze{
    private final Random random = new Random();
    private final int obstacleCount;

    public RandomMaze(){
        this.obstacleCount = randomNumber(1,100);
        generateObstacles();
    }

    public int randomNumber(int min, int max) {
        return random.nextInt(max - min) + min;
    }

    public int getObstacleCount() {
        return obstacleCount;
    }

    /**
     * Generates the obstacles
     */
    public void generateObstacles() {
        Random rand = new Random();
        int obs_count = rand.nextInt(10+ 1);
        for (int i = 1; i < obs_count; i++){
            int randX  = rand.nextInt(AbstractWorld.BOTTOM_RIGHT.getX()
                    - AbstractWorld.TOP_LEFT.getX())
                    + AbstractWorld.TOP_LEFT.getX();
            int randY = rand.nextInt(AbstractWorld.TOP_LEFT.getY()
                    - AbstractWorld.BOTTOM_RIGHT.getY())
                    + AbstractWorld.BOTTOM_RIGHT.getY();
            Obstacle obstacle = new SquareObstacle(randX, randY);
            this.addToObstacleList(obstacle);
        }
    }

    /**
     * Chack if the obstacle is blocked
     * @param obstacle
     * @return false
     */
    public boolean obstacleBlocked(Obstacle obstacle) {
        for (Obstacle obs : getObstacles()) {
            if (obs.blocksPosition(new Position(obstacle.getBottomLeftX(), obstacle.getBottomLeftY())) ||
                    obs.blocksPosition(new Position(obstacle.getBottomLeftX() + 4, obstacle.getBottomLeftY())) ||
                    obs.blocksPosition(new Position(obstacle.getBottomLeftX(), obstacle.getBottomLeftY() + 4)) ||
                    obs.blocksPosition(new Position(obstacle.getBottomLeftX() + 4, obstacle.getBottomLeftY() + 4)) ||
                    obs.blocksPosition(new Position(0, 0))) {
                return true;
            }
        }
        return false;
    }
}
