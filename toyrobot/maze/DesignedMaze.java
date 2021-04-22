package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.SquareObstacle;

public class DesignedMaze extends AbstractMaze{
    public DesignedMaze(){
        drawXObstacles();
        drawYObstacles();
    }

    /**
     * Draws the obstacles on the x-axis
     */
    public void drawXObstacles(){
        for (int i = 0; i < 55; i += 5) {
            addToObstacleList(new SquareObstacle(-20 + i, 51));
        }
        for (int i = 0; i < 120; i += 5) {
            addToObstacleList(new SquareObstacle(-62 + i, -159));
        }
        for (int i = 0; i < 160; i += 5) {
            addToObstacleList(new SquareObstacle(-100 + i, 105));
        }
        for (int i = 0; i < 170; i += 5) {
            addToObstacleList(new SquareObstacle(-80 + i, -160));
        }
        for (int i = 0; i < 180; i += 5) {
            addToObstacleList(new SquareObstacle(-100 + i, 170));
        }
    }

    /**
     * Draws the obstacles on the y-axis
     */
    public void drawYObstacles(){
        for (int i = 0; i < 150; i += 5) {
            addToObstacleList(new SquareObstacle(1, -100 + i));
        }
        for (int i = 0; i < 205; i += 5) {
            addToObstacleList(new SquareObstacle(-50, -150 + i));
        }
        for (int i = 0; i < 270; i += 5) {
            addToObstacleList(new SquareObstacle(70, -150 + i));
        }
        for (int i = 0; i < 300; i += 5) {
            addToObstacleList(new SquareObstacle(-90, -180 + i));
        }
        for (int i = 0; i < 350; i += 5) {
            addToObstacleList(new SquareObstacle(90, -180 + i));
        }
    }
}
