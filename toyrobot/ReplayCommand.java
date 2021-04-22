package za.co.wethinkcode.toyrobot;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ReplayCommand extends Command{

    /**
     * Constructor for ReplayCommand
     * @param argument
     */
    public ReplayCommand(String argument) {
        super("replay", argument);
    }

    /**
     * Replays commands that have been inputted
     * @param target
     * @return true
     */
    @Override
    public boolean execute(Robot target) {
        boolean reversed = getArgument().contains("reversed");
        List<String> commands = getCommands(target, reversed);
        int nrCommands = commands.size();
        for (String command: commands){
            target.handleCommand(Command.create(command));
            target.getHistory().removeLast();
            Play.printOutput(target);
        }                                                                                             // if a then b, if not then c
        target.setStatus("replayed " + nrCommands + " commands.");
        return true;
    }

    /**
     *
     * Takes the list of commands entered and plays them in reverse
     * @param target
     * @param reversed
     * @return commands
     */
    private List<String> getCommands(Robot target, boolean reversed){
        int start = 0;
        int end;
        List<String> commands = new ArrayList<>(target.getHistory().getCommands());
        String argument = getArgument().replace("reversed","").replaceAll("\\s", "");
        if (argument.contains("-")){
            String[] arguments = argument.split("-");
            start = Integer.parseInt(arguments[1]);
            end = Integer.parseInt(arguments[0]);
        }else if (!argument.isBlank()){
            end = Integer.parseInt(argument);
        }else{
            end = commands.size();
        }
        Collections.reverse(commands);
        try {
            commands = commands.subList(start, end);
        }catch (IndexOutOfBoundsException e){
            throw new IndexOutOfBoundsException();
        }
//        System.out.println(commands);
        if (!reversed){
            Collections.reverse(commands);
//            System.out.println(commands);
        }
        return commands;
    }
}
