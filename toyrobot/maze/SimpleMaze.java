package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.SquareObstacle;

public class SimpleMaze extends AbstractMaze{
    public  SimpleMaze(){
        this.addToObstacleList(new SquareObstacle(1,1));
    }
}
