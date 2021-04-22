package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class ForwardCommand extends Command {
    /**
     * ForwardCommand constructor
     */
    public ForwardCommand(String argument) {
        super("forward", argument);
    }

    /**
     * Instructs robot to move forward
     *
     * @param target the current robot object
     * @return `true`
     */
    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
        IWorld.UpdateResponse r = target.getWorld().updatePosition(nrSteps);
        if (r == IWorld.UpdateResponse.SUCCESS) {
            target.setStatus("Moved forward by "+nrSteps+" steps.");
        } else if (r == IWorld.UpdateResponse.FAILED_OBSTRUCTED) {
            target.setStatus("There is an obstacle in the way.");
        } else {
            target.setStatus("Sorry, I cannot go outside my safe zone.");
        }
        return true;
    }
}