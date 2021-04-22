package za.co.wethinkcode.toyrobot;


public class Robot {

    private final Position TOP_LEFT = new Position(-100,100);
    private final Position BOTTOM_RIGHT = new Position(100,-200);
    private Direction currentDirection;
    public static final Position CENTRE = new Position(0,0);

    private Position position;
    public String status;
    private String name;

    public Robot(String name) {
        this.name = name;
        this.status = "Ready";
        this.position = CENTRE;
        this.currentDirection = Direction.NORTH;
    }

    public String getStatus() {                                                                         //<5>
        return this.status;
    }


    public Direction getCurrentDirection() {                                                               //<8>
        return Direction.NORTH;
    }


    public boolean handleCommand(Command command) {
        return command.execute(this);
    }


    public boolean updatePosition(int nrSteps){
        int newY = this.position.getY();
        int newX = this.position.getX();

        if (Direction.NORTH.equals(this.currentDirection)) {
            newY = newY + nrSteps;
        }
        Position newPosition = new Position(newX, newY);
        if (newPosition.isIn(TOP_LEFT,BOTTOM_RIGHT)){
            this.position = newPosition;
            return true;

        }
        return false;
    }


    @Override
    public String toString() {
        return "[" + this.position.getX() + "," + this.position.getY() + "] "
                + "{" + this.currentDirection + "} "
                + this.name + "> " + this.status;
    }


    public Position getPosition() {
        return this.position;
    }


    public void setStatus(String s) {
        this.status = s;
    }
}