package za.co.wethinkcode.toyrobot;

public class LeftCommand extends Command{
    /**
     * Constructor
     */
    public LeftCommand(){
        super("left");
    }

    /**
     * Make robot turn 90 degrees left
     * @param target
     * @return
     */
    @Override
    public boolean execute(Robot target) {
        target.addCommand("left");
        target.getWorld().updateDirection(false);
        target.setStatus("Turned left.");
        return true;
    }
}
