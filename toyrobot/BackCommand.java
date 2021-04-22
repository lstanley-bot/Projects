package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class BackCommand extends Command {
    /**
     * BackCommand constructor
     */
    public BackCommand(String argument) {
        super("back", argument);
    }

    /**
     * Instructs robot to move backwards
     *
     * @param target the current robot object
     * @return `true`
     */
    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
        IWorld.UpdateResponse r = target.getWorld().updatePosition(-nrSteps);
        if (r == IWorld.UpdateResponse.SUCCESS) {
            target.setStatus("Moved back by "+nrSteps+" steps.");
        } else if (r == IWorld.UpdateResponse.FAILED_OBSTRUCTED) {
            target.setStatus("There is an obstacle in the way.");
        } else {
            target.setStatus("Sorry, I cannot go outside my safe zone.");
        }
        return true;
    }
}
