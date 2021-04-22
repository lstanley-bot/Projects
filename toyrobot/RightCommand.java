package za.co.wethinkcode.toyrobot;

public class RightCommand extends Command{
    public RightCommand(){
        super("right");
    }

    /**
     * Makes robot turn 90 degrees right
     * @param target
     * @return
     */
    @Override
    public boolean execute(Robot target) {
        target.addCommand("right");
        target.getWorld().updateDirection(true);
        target.setStatus("Turned right.");
        return true;
    }
}
