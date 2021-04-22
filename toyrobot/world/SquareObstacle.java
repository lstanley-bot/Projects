package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;

public class SquareObstacle implements Obstacle{
    private final Position obsPosition;
    private final int size;

    public SquareObstacle(int x, int y) {
        this.obsPosition = new Position(x,y);
        this.size = 5;
    }

    public int getBottomLeftX(){return this.obsPosition.getX();}

    public int getBottomLeftY(){return this.obsPosition.getY();}

    public int getSize(){return this.size;}

    public boolean blocksPosition(Position position){
        return ((getBottomLeftX() <= position.getX())) && (position.getX() <= (getBottomLeftX() + 4))
               && (getBottomLeftY() <= position.getY()) && (position.getY() <= getBottomLeftY() + 4);
    }

    public boolean blocksPath(Position pos1,Position pos2){
        if (pos1.getX() == pos2.getX()){
            for (int i = Math.min(pos1.getY(), pos2.getY()); i <= Math.max(pos1.getY(), pos2.getY()); i++){
                if (blocksPosition(new Position(pos1.getX(), i))){
                    return true;
                }
            }
        }else{
            for (int i = Math.min(pos1.getX(), pos2.getX()); i <= Math.max(pos1.getX(), pos2.getX()); i++){
                if (blocksPosition(new Position(i, pos1.getY()))){
                    return true;
                }
            }
        }
        return false;
    }
}
