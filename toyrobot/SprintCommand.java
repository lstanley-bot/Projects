package za.co.wethinkcode.toyrobot;

public class SprintCommand extends Command{
    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
        target.addCommand("sprint " + nrSteps);

        while (nrSteps > 0) {

            switch (target.getWorld().updatePosition(nrSteps)) {
                case SUCCESS:
                    target.setStatus("Moved forward by " + nrSteps + " steps.");
                    break;
                case FAILED_OUTSIDE_WORLD:
                    target.setStatus("Sorry, I cannot go outside my safe zone.");
                    return true;
                case FAILED_OBSTRUCTED:
                    target.setStatus("There is an obstacle in the way.");
                    return true;
            }
            if (nrSteps == 1) {
                break;
            }
            Play.printOutput(target);
            nrSteps -= 1;
        }
        return true;
    }
    public SprintCommand(String argument) {super("sprint", argument);}
}