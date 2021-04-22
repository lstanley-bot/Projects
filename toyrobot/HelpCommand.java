package za.co.wethinkcode.toyrobot;

public class HelpCommand extends Command {

    public HelpCommand() {
        super("help");
    }

    @Override
    public boolean execute(Robot target) {
        target.setStatus("I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\n" +
                "BACK - move back by specified number of steps, e.g. 'BACK 10'\n" +
                "RIGHT - moves right\n" +
                "LEFT - moves left\n" +
                "SPRINT - sprints by specified number of steps, e.g. 'SPRINT 10'\n" +
                "REPLAY - replay all previous movement commands, \n" +
                "REPLAY n - this will replay the last n commands, e.g. Replay 10 will replay the last 10 commands.\n" +
                "REPLAY n-m: this will replay the commands from n down to m.\n" +
                "REPLAY REVERSED - the reversed flag will reverse the order of the commands being replayed.\n" +
                "RESET - Sets robot direction to up, position to (0, 0) and removes obstacles.\n" +
                "MAZERUN - Robot finds his way to one of the edges, e.g. MAZERUN TOP.");
        return true;
    }
}
