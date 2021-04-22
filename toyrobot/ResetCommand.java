package za.co.wethinkcode.toyrobot;

public class ResetCommand extends Command{
    public ResetCommand(){
        super("reset");
    }

    /**
     * Rests the robots world
     * @param target
     * @return
     */
    @Override
    public boolean execute(Robot target){
        target.getWorld().reset();
        target.setStatus("The world has been reset.");
        return true;
    }
}
